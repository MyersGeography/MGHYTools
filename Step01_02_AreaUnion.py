# -*- coding: utf-8 -*-
"""
Generated by ArcGIS ModelBuilder on : 2022-04-27 15:32:51
"""
import arcpy
from sys import argv

def Step01_02_AreaUnion(Plats_by_Lot="Lot", AreaUnion="\\\\GISFile\\gisdata\\Department\\MSO\\Projects\\Internal\\CHM_Gontwz_landuseSuitabilityRerun\\Gonterwitz_Suitability_Rerun2022\\RESULTS_GontzGrowthProcess.gdb\\Results_2022\\AreaUnion", Lawrence_ZOning="\\\\GISFile\\gisdata\\Department\\MSO\\Projects\\Internal\\CHM_Gontwz_landuseSuitabilityRerun\\Gonterwitz_Suitability_Rerun2022\\RESULTS_GontzGrowthProcess.gdb\\Results_2022\\Zoning2022", Workspace_GDB="\\\\GISFile\\gisdata\\Department\\MSO\\Projects\\Internal\\CHM_Gontwz_landuseSuitabilityRerun\\Gonterwitz_Suitability_Rerun2022\\RESULTS_GontzGrowthProcess.gdb\\Results_2022", Land_Use_and_Building_Permits_by_polygon="\\\\GISFile\\gisdata\\Department\\MSO\\Projects\\Internal\\CHM_Gontwz_landuseSuitabilityRerun\\Gonterwitz_Suitability_Rerun2022\\RESULTS_GontzGrowthProcess.gdb\\Results_2022\\LandUseBuildingPermits_type02"):  # Step01_02_AreaUnion

    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = False

    # Model Environment settings
    with arcpy.EnvManager(extent="2045727.39081031 209617.596123308 2138008.89555138 274945.453000143", outputCoordinateSystem="PROJCS["NAD_1983_StatePlane_Kansas_North_FIPS_1501_Feet",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Lambert_Conformal_Conic"],PARAMETER["False_Easting",1312333.333333333],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-98.0],PARAMETER["Standard_Parallel_1",38.71666666666667],PARAMETER["Standard_Parallel_2",39.78333333333333],PARAMETER["Latitude_Of_Origin",38.33333333333334],UNIT["Foot_US",0.3048006096012192]]", scratchWorkspace=r"\\GISFile\gisdata\Department\MSO\Projects\Internal\CHM_Gontwz_landuseSuitabilityRerun\Gonterwitz_Suitability_Rerun2022\RESULTS_GontzGrowthProcess.gdb\Results_2022", 
                          workspace=r"\\GISFile\gisdata\Department\MSO\Projects\Internal\CHM_Gontwz_landuseSuitabilityRerun\Gonterwitz_Suitability_Rerun2022\RESULTS_GontzGrowthProcess.gdb\Results_2022"):

        # Process: Feature Class To Feature Class (Feature Class To Feature Class) (conversion)
        PlatsCopy = arcpy.conversion.FeatureClassToFeatureClass(in_features=Plats_by_Lot, out_path=Workspace_GDB, out_name="PlatsCopy", where_clause="", field_mapping="SUBDIVISION \"Subdivision\" true true false 254 Text 0 0,First,#,Lot,SUBDIVISION,0,254;BLOCK \"Block\" true true false 20 Text 0 0,First,#,Lot,BLOCK,0,20;LOT1 \"Lot (Integer)\" true true false 0 Short 0 0,First,#,Lot,LOT1,-1,-1;LOT2 \"Lot (Text)\" true true false 50 Text 0 0,First,#,Lot,LOT2,0,50", config_keyword="")[0]

        # Process: Union (Union) (analysis)
        arcpy.analysis.Union(in_features=[[PlatsCopy, 1], [Lawrence_ZOning, 3], [Land_Use_and_Building_Permits_by_polygon, ""]], out_feature_class=AreaUnion, join_attributes="ALL", cluster_tolerance="", gaps="GAPS")

if __name__ == '__main__':
    Step01_02_AreaUnion(*argv[1:])
