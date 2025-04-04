# Import system module
import arcpy

# set workspace environment
arcpy.env.workspace = r"C:\Users\tliu1\Documents\ArcGIS\Packages\GES393_Lab8_0409bb\commondata\part2"

# Local variables
streetLayer = arcpy.GetParameterAsText(0)   
expression = arcpy.GetParameterAsText(1)
buildingsLayer = arcpy.GetParameterAsText(2)
searchDist = arcpy.GetParameterAsText(3)
outTable = arcpy.GetParameterAsText(4)

arcpy.SelectLayerByAttribute_management(streetLayer, "NEW_SELECTION", expression)

arcpy.SelectLayerByLocation_management(buildingsLayer, "INTERSECT", streetLayer, searchDist, "NEW_SELECTION")

arcpy.CopyRows_management(buildingsLayer, outTable)
