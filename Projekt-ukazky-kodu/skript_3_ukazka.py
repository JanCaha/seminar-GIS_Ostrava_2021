from pathlib import Path

from qgis.core import QgsApplication
import processing
from processing.core.Processing import Processing
from qgis.analysis import QgsNativeAlgorithms

app = QgsApplication([], False)
Processing.initialize()
app.processingRegistry().addProvider(QgsNativeAlgorithms())

column_for_dissolve = 'category'

path_data = Path(__file__).parent / "data" / "nc_result.gpkg"

path_data_output = path_data.parent / "nc_vor_poly.gpkg"

path_data_output_dissolve = path_data.parent / "nc_vor_poly_dissolve.gpkg"

res_vp = processing.run("qgis:voronoipolygons",
                        parameters={'INPUT': str(path_data),
                                    'BUFFER': 0,
                                    'OUTPUT': 'TEMPORARY_OUTPUT'})

print(res_vp)

params = {'INPUT': res_vp["OUTPUT"],
          'FIELD': [column_for_dissolve],
          'OUTPUT': str(path_data_output_dissolve)}

res = processing.run("native:dissolve",
                     parameters=params)

print(res)

