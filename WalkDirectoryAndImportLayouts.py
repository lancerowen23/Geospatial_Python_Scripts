#Import select files from a directory with specific extension.
#ConvertLayoutFileToLayout creates an in-memory project and therefore 
#can't be used to import layouts into the current application or other existing projects. 
#To do this, use the importDocument method on the ArcGISProject class instead.

aprx = arcpy.mp.ArcGISProject("CURRENT")
import os

for root, dirs, files in os.walk(r""):
    for file in files:
        if file.endswith(".pagx"):
            x = os.path.join(root, file)
            aprx.importDocument(x)
	    print(x + " has been imported.")