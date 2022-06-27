#combine mosaic into new raster
import arcpy

aprx = arcpy.mp.ArcGISProject(r"C:\Users\...\Desktop\Demo\Norway_Demo\Norway_Demo.aprx")
arcpy.env.workspace = r"C:\Users\...\Desktop\Demo\Norway_Demo\Norway_Demo.gdb"
arcpy.env.overwriteOutput = True

#get rasters from workspace
dataset = arcpy.ListRasters()

#select the raster you want through index and convert to string
selected_rasters = dataset[8:-1]
raster_string ='; '.join(selected_rasters)
print(raster_string)

#perform raster comination
arcpy.MosaicToNewRaster_management(raster_string,
                                   arcpy.env.workspace,
                                   "Norway_All.tif",
                                    None,
                                   "8_BIT_UNSIGNED",
                                   None,
                                   "3",
                                   "LAST",
                                   "FIRST") 

aprx.save()

print("Shazam! This script has run successfully!")

