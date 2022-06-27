import arcpy
import os
aprx = arcpy.mp.ArcGISProject("")
arcpy.env.workspace = ""
arcpy.env.overwriteOutput = True

oceans = r"\Shapefiles\ne_10m_ocean\ne_10m_ocean.shp"
countries = r"\Shapefiles\ne_10m_admin_0_countries\ne_10m_admin_0_countries.shp"
states = r"\Shapefiles\ne_10m_admin_1_states_provinces\ne_10m_admin_1_states_provinces.shp"
lakes = r"\Shapefiles\ne_10m_lakes\ne_10m_lakes.shp"

#add data from path
for m in aprx.listMaps("Map"):
    m.addDataFromPath(oceans)
    m.addDataFromPath(countries)
    m.addDataFromPath(states)
    m.addDataFromPath(lakes)
    
#create new feature classes from layers to be placed into project geodatabase
arcpy.FeatureClassToFeatureClass_conversion(oceans, arcpy.env.workspace, "Countries")
arcpy.FeatureClassToFeatureClass_conversion(states, arcpy.env.workspace, "States")
arcpy.FeatureClassToFeatureClass_conversion(lakes, arcpy.env.workspace, "Lakes")
arcpy.FeatureClassToFeatureClass_conversion(oceans, arcpy.env.workspace, "Oceans")

#remove original layers
lyr_1 = m.listLayers("ne_10m_lakes")[0]
m.removeLayer(lyr_1)
lyr_2 = m.listLayers("ne_10m_admin_1_states_provinces")[0]
m.removeLayer(lyr_2)
lyr_3 = m.listLayers("ne_10m_ocean")[0]
m.removeLayer(lyr_3)
lyr_4 = m.listLayers("ne_10m_admin_0_countries")[0]
m.removeLayer(lyr_4)

#apply definition query for states and lakes
for m in aprx.listMaps("Map"):
    for lyr in m.listLayers("Lakes"):
        lyr.definitionQuery = "name = 'Lake Michigan' Or name = 'Lake Huron' Or name = 'Lake Erie' Or name = 'Lake Superior' Or name = 'Lake Ontario'"
    for lyr in m.listLayers("Countries"):
        lyr.definitionQuery = "admin = 'United States of America'"

#change layers to assigned color scheme
for m in aprx.listMaps("Map"):
        for lyr in m.listLayers():
            if lyr.name == "Oceans":
                sym = lyr.symbology
                sym.renderer.symbol.color = {'RGB' : [219, 225, 237, 100]}
                sym.renderer.symbol.outlineColor = {'RGB' : [255, 255, 255, 0]}
                lyr.symbology = sym
for m in aprx.listMaps("Map"):
        for lyr in m.listLayers():
            if lyr.name == "States":
                sym = lyr.symbology
                sym.renderer.symbol.color = {'RGB' : [180, 180, 180, 100]}
                sym.renderer.symbol.outlineColor = {'RGB' : [204, 204, 204, 100]}
                lyr.symbology = sym
for m in aprx.listMaps("Map"):
        for lyr in m.listLayers():
            if lyr.name == "Countries":
                sym = lyr.symbology
                sym.renderer.symbol.color = {'RGB' : [205, 205, 205, 100]}
                sym.renderer.symbol.outlineColor = {'RGB' : [255, 255, 255, 0]}
                lyr.symbology = sym
for m in aprx.listMaps("Map"):
        for lyr in m.listLayers():
            if lyr.name == "Lakes":
                sym = lyr.symbology
                sym.renderer.symbol.color = {'RGB' : [219, 225, 237, 100]}
                sym.renderer.symbol.outlineColor = {'RGB' : [255, 255, 255, 0]}
                lyr.symbology = sym

# save the project
aprx.save()

del aprx

#print a completion statement
print("This script has successfully run.")
