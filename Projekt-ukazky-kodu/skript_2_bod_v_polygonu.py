from pathlib import Path

from qgis.core import (QgsVectorLayer,
                       QgsFields,
                       QgsFeatureIterator,
                       QgsVectorFileWriter,
                       QgsWkbTypes,
                       QgsCoordinateTransformContext,
                       QgsFeature,
                       QgsGeometry,
                       QgsCoordinateReferenceSystem)

path_data = Path(__file__).parent / "data" / "nc_projected.gpkg"

path_data_output = path_data.parent / "nc_result.gpkg"

precision = 1

layer = QgsVectorLayer(str(path_data))

crs: QgsCoordinateReferenceSystem = layer.crs()

print(crs)

if crs.isGeographic():
    raise TypeError("Cannot process data with geographic coordinate system.")

fields: QgsFields = layer.fields()

save_options = QgsVectorFileWriter.SaveVectorOptions()
save_options.fileEncoding = "UTF-8"

writer: QgsVectorFileWriter = QgsVectorFileWriter.create(str(path_data_output),
                                                         fields,
                                                         QgsWkbTypes.Point,
                                                         layer.crs(),
                                                         QgsCoordinateTransformContext(),
                                                         save_options)

features: QgsFeatureIterator = layer.getFeatures()

feature: QgsFeature

for feature in features:

    new_feature = QgsFeature(fields)

    old_geom: QgsGeometry = feature.geometry()

    new_geom: QgsGeometry = old_geom.poleOfInaccessibility(precision)[0]

    new_feature.setAttributes(feature.attributes())
    new_feature.setGeometry(new_geom)

    writer.addFeature(new_feature)

del writer
