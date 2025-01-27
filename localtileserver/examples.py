from functools import wraps
from typing import Union

from localtileserver.client import TileClient
from localtileserver.tileserver import get_data_path, get_pine_gulch_url, get_sf_bay_url


def _get_example_client(
    port: Union[int, str] = "default",
    debug: bool = False,
    client_port: int = None,
    client_host: str = None,
    client_prefix: str = None,
):
    raise NotImplementedError


@wraps(_get_example_client)
def get_blue_marble(*args, **kwargs):
    path = get_data_path("frmt_wms_bluemarble_s3_tms.xml")
    return TileClient(path, *args, **kwargs)


@wraps(_get_example_client)
def get_virtual_earth(*args, **kwargs):
    path = get_data_path("frmt_wms_virtualearth.xml")
    return TileClient(path, *args, **kwargs)


@wraps(_get_example_client)
def get_arcgis(*args, **kwargs):
    path = get_data_path("frmt_wms_arcgis_mapserver_tms.xml")
    return TileClient(path, *args, **kwargs)


@wraps(_get_example_client)
def get_elevation(*args, **kwargs):
    path = get_data_path("aws_elevation_tiles_prod.xml")
    return TileClient(path, *args, **kwargs)


@wraps(_get_example_client)
def get_bahamas(*args, **kwargs):
    path = get_data_path("bahamas_rgb.tif")
    return TileClient(path, *args, **kwargs)


@wraps(_get_example_client)
def get_pine_gulch(*args, **kwargs):
    path = get_pine_gulch_url()
    return TileClient(path, *args, **kwargs)


@wraps(_get_example_client)
def get_landsat(*args, **kwargs):
    path = get_data_path("landsat.tif")
    return TileClient(path, *args, **kwargs)


@wraps(_get_example_client)
def get_san_francisco(*args, **kwargs):
    path = get_sf_bay_url()
    return TileClient(path, *args, **kwargs)
