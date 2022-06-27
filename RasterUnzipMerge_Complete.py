#Unzip, convert to geodatabase, combine into single raster

import arcpy
import os
import zipfile

aprx = arcpy.mp.ArcGISProject(r"C:\Users\....\Desktop\Demo\Norway_Demo\Norway_Demo.aprx")
arcpy.env.workspace = r"C:\Users\....\Desktop\Demo\Norway_Demo\Norway_Demo.gdb"
arcpy.env.overwriteOutput = True
Source_Directory = r"C:\Users\....\Norway\SatellittdataSentenielSkyfritt2018"

#Unzip
for item in os.listdir(Source_Directory): # loop through items in dir
    if item.endswith(extension): # check for ".zip" extension
        file_name = os.path.abspath(item) # get full path of files
        zip_ref = zipfile.ZipFile(file_name) # create zipfile object
        zip_ref.extractall(dir_name) # extract file to dir
        zip_ref.close() # close file
        os.remove(file_name) # delete zipped file

#Add rasters to geodatabase
tif_list = os.listdir(Source_Directory)
print(tif_list)
tif_string = "; ".join(tif_list)
print(tif_string)
arcpy.RasterToGeodatabase_conversion(tif_string, arcpy.env.workspace)


