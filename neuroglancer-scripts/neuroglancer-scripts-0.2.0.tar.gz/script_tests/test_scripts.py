# Copyright (c) CEA
# Copyright (c) 2018 Forschungszentrum Juelich GmbH
# Author: Yann Leprince <y.leprince@fz-juelich.de>
#
# This software is made available under the MIT licence, see LICENCE.txt.

import gzip
import json
import subprocess

import nibabel
import numpy as np
import pytest
import PIL.Image

from neuroglancer_scripts.mesh import read_precomputed_mesh


@pytest.fixture(scope="module")
def examples_dir(request):
    return request.fspath / ".." / ".." / "examples"


def test_jubrain_example_MPM(examples_dir, tmpdir):
    input_nifti = examples_dir / "JuBrain" / "MPM.nii.gz"
    # The file may be present but be a git-lfs pointer file, so we need to open
    # it to make sure that it is the actual correct file.
    try:
        gzip.open(str(input_nifti)).read(348)
    except OSError as exc:
        pytest.skip("Cannot find a valid example file {0} for testing: {1}"
                    .format(input_nifti, exc))

    output_dir = tmpdir / "MPM"
    assert subprocess.call([
        "volume-to-precomputed",
        "--generate-info",
        str(input_nifti),
        str(output_dir)
    ]) == 0
    assert subprocess.call([
        "generate-scales-info",
        "--type=segmentation",
        "--encoding=compressed_segmentation",
        str(output_dir / "info_fullres.json"),
        str(output_dir)
    ]) == 0
    assert subprocess.call([
        "volume-to-precomputed",
        str(input_nifti),
        str(output_dir)
    ]) == 0
    assert subprocess.call([
        "compute-scales",
        "--downscaling-method=stride",  # for test speed
        str(output_dir)
    ]) == 0
    assert subprocess.call([
        "scale-stats",
        str(output_dir),
    ]) == 0
    assert subprocess.call([
        "convert-chunks",
        "--copy-info",
        str(output_dir),
        str(output_dir / "copy")
    ]) == 0


def test_all_in_one_conversion(examples_dir, tmpdir):
    input_nifti = examples_dir / "JuBrain" / "colin27T1_seg.nii.gz"
    # The file may be present but be a git-lfs pointer file, so we need to open
    # it to make sure that it is the actual correct file.
    try:
        gzip.open(str(input_nifti)).read(348)
    except OSError as exc:
        pytest.skip("Cannot find a valid example file {0} for testing: {1}"
                    .format(input_nifti, exc))

    output_dir = tmpdir / "colin27T1_seg"
    assert subprocess.call([
        "volume-to-precomputed-pyramid",
        "--mmap",
        "--input-min", "50",
        "--input-max", "500",
        "--downscaling-method", "stride",
        str(input_nifti),
        str(output_dir)
    ]) == 0
    # TODO check the actual data for correct scaling, especially in combination
    # with --mmap / --load-full-volume


def test_slice_conversion(tmpdir):
    # Prepare dummy slices
    path_to_slices = tmpdir / "slices"
    path_to_slices.mkdir()
    size_x, size_y = 12, 16
    img_array = np.reshape(
        np.arange(size_x * size_y, dtype=np.float32),
        (size_y, size_x)
    )
    img = PIL.Image.fromarray(img_array)
    size_z = 2
    img.save(str(path_to_slices / "slice1.tiff"))
    img.save(str(path_to_slices / "slice2.tiff"))
    # Write minimal yet complete info
    path_to_converted = tmpdir / "conv"
    path_to_converted.mkdir()
    with (path_to_converted / "info_fullres.json").open("w") as f:
        json.dump({
            "data_type": "uint8",
            "num_channels": 1,
            "scales": [
                {
                    "resolution": [1e6, 1e6, 1e6],
                    "size": [size_x, size_y, size_z],
                    "voxel_offset": [0, 0, 0]
                }
            ]
        }, f)
    assert subprocess.call([
        "generate-scales-info",
        "--max-scales", "2",
        "--target-chunk-size", "8",
        str(path_to_converted / "info_fullres.json"),
        str(path_to_converted)
    ]) == 0
    # Run the converter
    assert subprocess.call([
        "slices-to-precomputed",
        str(path_to_slices),
        str(path_to_converted)
    ]) == 0
    # Downscale the data to check that it can be read successfully
    assert subprocess.call([
        "compute-scales",
        "--downscaling-method", "stride",
        str(path_to_converted)
    ]) == 0


def dummy_mesh(num_vertices=4, num_triangles=3):
    vertices = np.reshape(
        np.arange(3 * num_vertices, dtype=np.float32),
        (num_vertices, 3)
    )
    triangles = np.reshape(
        np.arange(3 * num_triangles, dtype=np.uint32),
        (num_triangles, 3)
    ) % num_vertices
    return vertices, triangles


def write_gifti_mesh(vertices, triangles, filename):
    gii = nibabel.gifti.GiftiImage()
    data_arr = nibabel.gifti.gifti.GiftiDataArray(
        vertices,
        "NIFTI_INTENT_POINTSET"
    )
    gii.add_gifti_data_array(data_arr)
    data_arr = nibabel.gifti.gifti.GiftiDataArray(
        triangles,
        "NIFTI_INTENT_TRIANGLE"
    )
    gii.add_gifti_data_array(data_arr)
    nibabel.save(gii, filename)


def test_mesh_conversion(tmpdir):
    vertices, triangles = dummy_mesh()
    dummy_gii_path = tmpdir / "dummy.surf.gii"
    write_gifti_mesh(vertices, triangles, str(dummy_gii_path))
    dummy_precomputed_path = tmpdir / "dummy_precomputed"
    assert subprocess.call([
        "mesh-to-precomputed",
        str(dummy_gii_path),
        str(dummy_precomputed_path)
    ]) == 0
    with gzip.open(str(dummy_precomputed_path) + ".gz", "rb") as file:
        vertices2, triangles2 = read_precomputed_mesh(file)
    assert np.array_equal(vertices * 1e6, vertices2)
    assert np.array_equal(triangles, triangles2)


def test_mesh_conversion_with_transform(tmpdir):
    vertices, triangles = dummy_mesh()
    dummy_gii_path = tmpdir / "dummy.surf.gii"
    write_gifti_mesh(vertices, triangles, str(dummy_gii_path))
    dummy_precomputed_path = tmpdir / "dummy_precomputed"
    assert subprocess.call([
        "mesh-to-precomputed",
        "--coord-transform", "0,1,0,0.2,1,0,0,0,0,0,-1,0.3",
        str(dummy_gii_path),
        str(dummy_precomputed_path)
    ]) == 0
