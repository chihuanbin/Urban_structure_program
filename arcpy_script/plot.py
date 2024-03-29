# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# plot.py
# Created on: 2018-08-10 17:25:49.00000
#   (generated by ArcGIS/ModelBuilder)
# Usage: plot <point_to_xly> <point_xly_FeatureToPoint_Spatia_null> 
# Description: 
# ---------------------------------------------------------------------------

# Set the necessary product code
# import arcinfo


# Import arcpy module
import arcpy

# Script arguments
point_to_xly = arcpy.GetParameterAsText(0)
if point_to_xly == '#' or not point_to_xly:
    point_to_xly = "D:\\zhangyan_gis_grid\\test.gdb\\point_to_xly" # provide a default value if unspecified

point_xly_FeatureToPoint_Spatia_null = arcpy.GetParameterAsText(1)
if point_xly_FeatureToPoint_Spatia_null == '#' or not point_xly_FeatureToPoint_Spatia_null:
    point_xly_FeatureToPoint_Spatia_null = "C:\\Users\\Administrator\\Documents\\ArcGIS\\Default.gdb\\point_xly_FeatureToPoint_Spatia_null" # provide a default value if unspecified

# Local variables:
输出要素类 = "C:\\Users\\Administrator\\Documents\\ArcGIS\\Default.gdb\\point_FeatureToPoint"
小流域（有排口）_shp = "D:\\zhangyan_gis_grid\\小流域\\小流域（有排口）.shp"

# Process: 要素转点
arcpy.FeatureToPoint_management(point_to_xly, 输出要素类, "CENTROID")

# Process: 空间连接
arcpy.SpatialJoin_analysis(输出要素类, 小流域（有排口）_shp, point_xly_FeatureToPoint_Spatia_null, "JOIN_ONE_TO_ONE", "KEEP_ALL", "出水口 \"出水口\" true true false 50 Text 0 0 ,First,#,D:\\zhangyan_gis_grid\\小流域\\小流域（有排口）.shp,出水口,-1,-1;编号 \"编号\" true true false 50 Text 0 0 ,First,#,D:\\zhangyan_gis_grid\\小流域\\小流域（有排口）.shp,编号,-1,-1;面积 \"面积\" true true false 19 Double 0 0 ,First,#,D:\\zhangyan_gis_grid\\小流域\\小流域（有排口）.shp,面积,-1,-1;X \"X\" true true false 19 Double 0 0 ,First,#,D:\\zhangyan_gis_grid\\小流域\\小流域（有排口）.shp,X,-1,-1;Y \"Y\" true true false 19 Double 0 0 ,First,#,D:\\zhangyan_gis_grid\\小流域\\小流域（有排口）.shp,Y,-1,-1;一级分区 \"一级分区\" true true false 50 Text 0 0 ,First,#,D:\\zhangyan_gis_grid\\小流域\\小流域（有排口）.shp,一级分区,-1,-1;积水站数 \"积水站数\" true true false 4 Short 0 4 ,First,#,D:\\zhangyan_gis_grid\\小流域\\小流域（有排口）.shp,积水站数,-1,-1;井液站数 \"井液站数\" true true false 4 Short 0 4 ,First,#,D:\\zhangyan_gis_grid\\小流域\\小流域（有排口）.shp,井液站数,-1,-1;雨量站数 \"雨量站数\" true true false 4 Short 0 4 ,First,#,D:\\zhangyan_gis_grid\\小流域\\小流域（有排口）.shp,雨量站数,-1,-1;STCD \"STCD\" true true false 254 Text 0 0 ,First,#,C:\\Users\\Administrator\\Documents\\ArcGIS\\Default.gdb\\point_FeatureToPoint,STCD,-1,-1;STNM \"STNM\" true true false 254 Text 0 0 ,First,#,C:\\Users\\Administrator\\Documents\\ArcGIS\\Default.gdb\\point_FeatureToPoint,STNM,-1,-1;LGTD \"LGTD\" true true false 8 Double 0 0 ,First,#,C:\\Users\\Administrator\\Documents\\ArcGIS\\Default.gdb\\point_FeatureToPoint,LGTD,-1,-1;LTTD \"LTTD\" true true false 8 Double 0 0 ,First,#,C:\\Users\\Administrator\\Documents\\ArcGIS\\Default.gdb\\point_FeatureToPoint,LTTD,-1,-1;TOTALNUM \"TOTALNUM\" true true false 4 Float 0 0 ,First,#,C:\\Users\\Administrator\\Documents\\ArcGIS\\Default.gdb\\point_FeatureToPoint,TOTALNUM,-1,-1;ORIG_FID \"ORIG_FID\" true true false 0 Long 0 0 ,First,#,C:\\Users\\Administrator\\Documents\\ArcGIS\\Default.gdb\\point_FeatureToPoint,ORIG_FID,-1,-1", "INTERSECT", "", "")

