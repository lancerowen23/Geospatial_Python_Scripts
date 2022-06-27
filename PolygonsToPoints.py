import arcpy
import os
aprx = arcpy.mp.ArcGISProject()
arcpy.env.workspace = 
arcpy.env.overwriteOutput = True
polygons =

#Add Field for Centroid XY
arcpy.management.AddFields(polygons, [["X_Centroid", "LONG"], ["Y_Centroid", "LONG"]])

#Calculate Field for Centroids
arcpy.management.CalculateGeometryAttributes(polygons, "X_Centroid CENTROID_X;Y_Centroid CENTROID_Y", '', '', None)

#XY in Table to Point
arcpy.management.XYTableToPoint(polygons, "XYpoints",
                                "X_Centroid", "Y_Centroid", "", arcpy.SpatialReference(insert CRS))







