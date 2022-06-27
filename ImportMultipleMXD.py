#Import multiple MXDs from directory
import os
import arcpy

aprx = arcpy.mp.ArcGISProject("CURRENT")
arcpy.env.workspace = ""
arcpy.env.overwriteOutput = True

data_directory = ""
extension = ".mxd"

os.chdir(data_directory)
for item in os.listdir(data_directory):
    if item.endswith(extension):
        file_name = os.path.abspath(item)
        aprx.importDocument(file_name)
        print(item)

aprx.save()
del aprx
print("Shazam! This tool has run successfully.")
              
