try:
    from cartotools.crs import *  # noqa: F401 F403
    from cartotools.osm import location
    from cartotools.osm.nominatim import Nominatim

    cartotools = True
except ImportError:
    # cartotools provides a few more basic projections
    from cartopy.crs import *  # noqa: F401 F403

    # Basic version of the complete cached requests included in cartotools
    from .location import location  # noqa: F401

    cartotools = False

from cartopy.feature import NaturalEarthFeature
from cartopy.mpl.geoaxes import GeoAxesSubplot

from ..core.mixins import ShapelyMixin


def countries(**kwargs):
    params = {
        "category": "cultural",
        "name": "admin_0_countries",
        "scale": "10m",
        "edgecolor": "#524c50",
        "facecolor": "none",
        "alpha": .5,
        **kwargs,
    }
    return NaturalEarthFeature(**params)


def rivers(**kwargs):
    params = {
        "category": "physical",
        "name": "rivers_lake_centerlines",
        "scale": "10m",
        "edgecolor": "#226666",
        "facecolor": "none",
        "alpha": .5,
        **kwargs,
    }
    return NaturalEarthFeature(**params)


def lakes(**kwargs):
    params = {
        "category": "physical",
        "name": "lakes",
        "scale": "10m",
        "edgecolor": "#226666",
        "facecolor": "#226666",
        "alpha": .2,
        **kwargs,
    }
    return NaturalEarthFeature(**params)


def ocean(**kwargs):
    params = {
        "category": "physical",
        "name": "ocean",
        "scale": "10m",
        "edgecolor": "#226666",
        "facecolor": "#226666",
        "alpha": .2,
        **kwargs,
    }
    return NaturalEarthFeature(**params)


def _set_default_extent(self):
    """Helper for a default extent limited to the projection boundaries."""
    west, south, east, north = self.projection.boundary.bounds
    self.set_extent((west, east, south, north), crs=self.projection)


GeoAxesSubplot.set_default_extent = _set_default_extent


def _set_extent(self, shape):
    if isinstance(shape, ShapelyMixin):
        return self._set_extent(shape.extent)
    if cartotools and isinstance(shape, Nominatim):
        return self._set_extent(shape.extent)
    self._set_extent(shape)


GeoAxesSubplot._set_extent = GeoAxesSubplot.set_extent
GeoAxesSubplot.set_extent = _set_extent
