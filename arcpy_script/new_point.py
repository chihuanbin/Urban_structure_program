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

# spatial_ref=arcpy.GetParameterAsText(2)
# if spatial_ref == '#' or not spatial_ref:
#     spatial_ref = 'D:\zhangyan_gis_grid\小流域\小流域（有排口）.shp'
# Create an empty Point object
#
point = arcpy.Point()
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

point_featuretopoint="C:\\Users\\Administrator\\Documents\\ArcGIS\\Default.gdb\\point_FeatureToPoint"
arcpy.DefineProjection_management(point_featuretopoint, 4490)
arcpy.SetParameter(2, point_featuretopoint) # Is not polygon
