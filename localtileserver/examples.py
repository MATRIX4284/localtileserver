import pathlib
from typing import Union

from localtileserver.server import TileClient


def get_data_path(name):
    dirname = pathlib.Path(__file__).parent
    return dirname / "data" / name


def get_pine_gulch_url():
    return "https://opendata.digitalglobe.com/events/california-fire-2020/pre-event/2018-02-16/pine-gulch-fire20/1030010076004E00.tif"


def get_blue_marble(port: Union[int, str] = "default", debug: bool = False):
    path = get_data_path("frmt_wms_bluemarble_s3_tms.xml")
    return TileClient(path, port=port, debug=debug)


def get_virtual_earth(port: Union[int, str] = "default", debug: bool = False):
    path = get_data_path("frmt_wms_virtualearth.xml")
    return TileClient(path, port=port, debug=debug)


def get_arcgis(port: Union[int, str] = "default", debug: bool = False):
    path = get_data_path("frmt_wms_arcgis_mapserver_tms.xml")
    return TileClient(path, port=port, debug=debug)


def get_elevation(port: Union[int, str] = "default", debug: bool = False):
    path = get_data_path("aws_elevation_tiles_prod.xml")
    return TileClient(path, port=port, debug=debug)


def get_bahamas(port: Union[int, str] = "default", debug: bool = False):
    path = get_data_path("bahamas_rgb.tif")
    return TileClient(path, port=port, debug=debug)


def get_pine_gulch(port: Union[int, str] = "default", debug: bool = False):
    path = get_pine_gulch_url()
    return TileClient(path, port=port, debug=debug)