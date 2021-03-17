# typování v Pythonu https://docs.python.org/3.9/library/typing.html
import typing
from pathlib import Path

from osgeo import gdal, ogr, osr

# tyto importy od GDAL 3.2. generují chybu
# import gdal
# import ogr

from qgis.core import QgsVectorLayer


def get_first_layer(ds: ogr.DataSource) -> ogr.Layer:
    return ds.GetLayer()


path_data = Path(__file__).parent / "data" / "nc.gpkg"

ds: ogr.DataSource = ogr.Open(str(path_data))

layer: ogr.Layer = ds.GetLayer()

print(layer.GetName())
print(layer.GetFeatureCount())

crs: osr.SpatialReference = layer.GetSpatialRef()

print(crs.GetAuthorityCode(None))
print(crs.ExportToWkt())

lyr = get_first_layer(ds)

print(lyr.GetName())
