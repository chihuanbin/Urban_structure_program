# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2019/8/10 17:48'
import arcpy

# A list of coordinate pairs
#
#pointList = [[1,2],[3,5],[7,3]]

x = arcpy.GetParameterAsText(0)
if x == '#' or not x:
    x= 119.28357396656681#,26.059927635968275" # provide a default value if unspecified

y = arcpy.GetParameterAsText(1)
if y == '#' or not y:
    y = 26.059927635968275

# Create an empty Point object
#
point = arcpy.Point()

# A list to hold the PointGeometry objects
#

# For each coordinate pair, populate the Point object and create
#  a new PointGeometry

#for pt in pointList:
point.X = x
point.Y = y

pointGeometry = arcpy.PointGeometry(point)
    #pointGeometryList.append(pointGeometry)

# Create a copy of the PointGeometry objects, by using pointGeometryList
#  as input to the CopyFeatures tool.
arcpy.CopyFeatures_management(pointGeometry,"C:\\Users\\Administrator\\Documents\\ArcGIS\\Default.gdb\\point_FeatureToPoint")

arcpy.SetParameter(2, pointGeometry) # Is not polygon
