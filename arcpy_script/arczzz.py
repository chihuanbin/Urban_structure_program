# -*- coding: UTF-8 -*-
_author_ = 'zy'
_date_ = '2019/1/13 0013 13:14'
import arcpy

# A list of features and coordinate pairs
feature_info = [[[1, 2], [2, 4], [3, 7]],[[6, 8], [5, 7], [7, 2], [9, 5]]]

# A list that will hold each of the Polyline objects
features = []

for feature in feature_info:
    # Create a Polyline object based on the array of points
    # Append to the list of Polyline objects
    features.append(
        arcpy.Polyline(
            arcpy.Array([arcpy.Point(*coords) for coords in feature])))

# Persist a copy of the Polyline objects using CopyFeatures
arcpy.CopyFeatures_management(features, "polylines.shp")