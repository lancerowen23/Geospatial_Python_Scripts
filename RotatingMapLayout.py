# ROTATING A MAP WITHIN A MAP FRAME (SEE LINE STARTING AT 43)
# ALSO RESCALING A MAP (SEE LINE 32-36)
# In addition to importing arcpy, you'll also import os, which will allow you to have code to open pdf at the end
# of the script.
import arcpy
import os
arcpy.env.overwriteOutput = True

# First, you need to set the project variable with the mapping module:
aprx = arcpy.mp.ArcGISProject(r"C:\LPA\Projects\LayoutProject\LayoutProject.aprx")

# Second, you need set a variable for the map object:
mapx = aprx.listMaps("Map")[0]

#  Third, you need to set a variable for the layer object:
# (Note that this is mapx.listLayers, not aprx.listLayers
countriesLayer = mapx.listLayers("Countries")[0]

# Fourth, you need to set a variable for the layout object:
lyt = aprx.listLayouts()[0]

# Fifth, you need to set the map frames:
mapFrame = lyt.listElements('MAPFRAME_ELEMENT', "Map Frame")[0]
# map frame width is 20 millimeters less than the page width
mapFrame.elementWidth = lyt.pageWidth - 20
# map frame height is same as width--in other words, the map is square
mapFrame.elementHeight = mapFrame.elementWidth
# remembering that the anchor point for this map is the lower left, we'll put the x position 10mm in from
# left-hand edge.
mapFrame.elementPositionX = 10
# and we'll put the y position a quarter of the way up the page.
mapFrame.elementPositionY = lyt.pageHeight / 4
# Change Scale
mapFrame.camera.scale = 15000000
# Quick print of map's scale
print(mapFrame.camera.scale)

# Mapsurround object
northArrow = lyt.listElements("MAPSURROUND_ELEMENT", "North Arrow")[0]
northArrow.elementHeight = 30
northArrow.elementPositionX = lyt.pageWidth - 40
northArrow.elementPositionY = 40
# TO ROTATE MAP WITHIN MAP FRAME, USE CAMERA OBJECT AND CHANGE HEADING PROPERTY
# NB: Negative numbers are used for clockwise rotations.
mapFrame.camera.heading = -25

# Export to PDF and open in Adobe Acrobat Reader
# Note that you must create a folder in which the file will be placed if such a file does not exist.
lyt.exportToPDF(r"C:\LPA\PDFs\test.pdf")
os.startfile(r"C:\LPA\PDFs\test.pdf")

# Delete project object
del aprx

print("\nScript completed.")
