import os
import sys
import unittest

import numpy as np
import pandas as pd

from starfish import IntensityTable
from starfish.test.full_pipelines.cli._base_cli_test import CLITest
from starfish.types import Features


class TestWithDartfishData(CLITest, unittest.TestCase):

    @property
    def subdirs(self):
        return (
            "registered",
            "filtered",
            "results"
        )

    @property
    def stages(self):
        return (
            [
                sys.executable,
                "examples/get_cli_test_data.py",
                "https://d2nhj9g34unfro.cloudfront.net/20181005/DARTFISH-TEST/",
                lambda tempdir, *args, **kwargs: os.path.join(tempdir, "registered")
            ],
            [
                "starfish", "filter",
                "--input", lambda tempdir, *args, **kwargs: os.path.join(
                    tempdir, "registered/fov_001", "hybridization.json"),
                "--output", lambda tempdir, *args, **kwargs: os.path.join(
                    tempdir, "filtered", "scale_filtered.json"),
                "ScaleByPercentile",
                "--p", "100",
            ],
            [
                "starfish", "filter",
                "--input", lambda tempdir, *args, **kwargs: os.path.join(
                    tempdir, "filtered", "scale_filtered.json"),
                "--output", lambda tempdir, *args, **kwargs: os.path.join(
                    tempdir, "filtered", "zero_filtered.json"),
                "ZeroByChannelMagnitude",
                "--thresh", ".05",
            ],
            [
                "starfish", "detect_spots",
                "--input", lambda tempdir, *args, **kwargs: os.path.join(
                    tempdir, "filtered", "zero_filtered.json"),
                "--output", lambda tempdir, *args, **kwargs: os.path.join(
                    tempdir, "results", "spots.nc"),
                "--codebook", lambda tempdir, *args, **kwargs: os.path.join(
                    tempdir, "registered", "codebook.json"),
                "PixelSpotDetector",
                "--distance-threshold", "3",
                "--magnitude-threshold", ".5",
                "--min-area", "5",
                "--max-area", "30",
            ],
        )

    def verify_results(self, intensities):
        assert intensities[Features.PASSES_THRESHOLDS].sum()

        spots_df = IntensityTable(
            intensities.where(intensities[Features.PASSES_THRESHOLDS], drop=True)
        ).to_features_dataframe()
        spots_df['area'] = np.pi * spots_df['radius'] ** 2

        # verify number of spots detected
        spots_passing_filters = intensities[Features.PASSES_THRESHOLDS].sum()
        assert spots_passing_filters == 53  # TODO note, had to change this by 1

        # compare to benchmark data -- note that this particular part of the dataset
        # appears completely uncorrelated
        cnts_benchmark = pd.read_csv(
            'https://d2nhj9g34unfro.cloudfront.net/20181005/DARTFISH/fov_001/counts.csv')

        min_dist = 0.6
        cnts_starfish = spots_df[spots_df.distance <= min_dist].groupby('target').count()['area']
        cnts_starfish = cnts_starfish.reset_index(level=0)
        cnts_starfish.rename(columns={'target': 'gene', 'area': 'cnt_starfish'}, inplace=True)

        # get top 5 genes and verify they are correct
        high_expression_genes = cnts_starfish.sort_values('cnt_starfish', ascending=False).head(5)

        assert np.array_equal(
            high_expression_genes['cnt_starfish'].values,
            [7, 3, 2, 2, 2]
        )
        assert np.array_equal(
            high_expression_genes['gene'].values,
            ['MBP', 'MOBP', 'ADCY8', 'TRIM66', 'SYT6']
        )

        # verify correlation is accurate for this subset of the image
        benchmark_comparison = pd.merge(cnts_benchmark, cnts_starfish, on='gene', how='left')
        benchmark_comparison.head(20)

        x = benchmark_comparison.dropna().cnt.values
        y = benchmark_comparison.dropna().cnt_starfish.values
        corrcoef = np.corrcoef(x, y)
        corrcoef = corrcoef[0, 1]

        assert np.round(corrcoef, 5) == 0.04422
