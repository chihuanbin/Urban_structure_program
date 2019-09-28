# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2019/8/10 20:19'
import arcpy
# Get the feature class from the tool.
#
spatial_join_result = arcpy.GetParameterAsText(0)

cursor=arcpy.da.SearchCursor(spatial_join_result,["编号","出水口"])

arcpy.AddMessage(cursor)

id_result=''
for row in cursor:
    id_result=row[0]

arcpy.AddMessage(id_result)

arcpy.SetParameterAsText(1, id_result) # Is not polygon