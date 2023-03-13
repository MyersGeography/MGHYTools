# -*- coding: utf-8 -*-
import arcpy
from sys import argv

def Step01_01_LandUseBuildingPermits(Building_Permit_Points="BuildingPermits - Building Permit", Land_Use="\\\\GISFile\\gisdata\\Department\\MSO\\Projects\\Internal\\CHM_Gontwz_landuseSuitabilityRerun\\Gonterwitz_Suitability_Rerun2022\\Gonterwitz_Suitability_Rerun2022.gdb\\LandUse2021", Building_Footprints="\\\\GISFile\\gisdata\\Department\\MSO\\Projects\\Internal\\CHM_Gontwz_landuseSuitabilityRerun\\Gonterwitz_Suitability_Rerun2022\\Gonterwitz_Suitability_Rerun2022.gdb\\BuildingFootprints", LandUseBuildingPermits_type02="\\\\GISFile\\gisdata\\Department\\MSO\\Projects\\Internal\\CHM_Gontwz_landuseSuitabilityRerun\\Gonterwitz_Suitability_Rerun2022\\RESULTS_GontzGrowthProcess.gdb\\Results_2022\\LandUseBuildingPermits_type02", Workspace_GDB="\\\\GISFile\\gisdata\\Department\\MSO\\Projects\\Internal\\CHM_Gontwz_landuseSuitabilityRerun\\Gonterwitz_Suitability_Rerun2022\\RESULTS_GontzGrowthProcess.gdb\\Results_2022"):  # Step01_01_LandUseBuildingPermits

    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = True

    arcpy.ImportToolbox(r"c:\program files\arcgis\pro\Resources\ArcToolbox\toolboxes\Analysis Tools.tbx.tbx")
    # Model Environment settings
    with arcpy.EnvManager(extent="2045727.39081031 209617.596123308 2138008.89555138 274945.453000143", outputCoordinateSystem="PROJCS["NAD_1983_StatePlane_Kansas_North_FIPS_1501_Feet",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Lambert_Conformal_Conic"],PARAMETER["False_Easting",1312333.333333333],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-98.0],PARAMETER["Standard_Parallel_1",38.71666666666667],PARAMETER["Standard_Parallel_2",39.78333333333333],PARAMETER["Latitude_Of_Origin",38.33333333333334],UNIT["Foot_US",0.3048006096012192]]", scratchWorkspace=r"\\GISFile\gisdata\Department\MSO\Projects\Internal\CHM_Gontwz_landuseSuitabilityRerun\Gonterwitz_Suitability_Rerun2022\RESULTS_GontzGrowthProcess.gdb\Results_2022", 
                          workspace=r"\\GISFile\gisdata\Department\MSO\Projects\Internal\CHM_Gontwz_landuseSuitabilityRerun\Gonterwitz_Suitability_Rerun2022\RESULTS_GontzGrowthProcess.gdb\Results_2022"):

        
        # Process: Feature Class To Feature Class (4) (Feature Class To Feature Class) (conversion)
        LU2021 = arcpy.conversion.FeatureClassToFeatureClass(in_features=Land_Use, out_path=Workspace_GDB, out_name="LU2021", where_clause="", #, config_keyword="")[0]

        
        # Process: Feature Class To Feature Class (2) (Feature Class To Feature Class) (conversion)
        BuildingFootprints = arcpy.conversion.FeatureClassToFeatureClass(in_features=Building_Footprints, out_path=Workspace_GDB, out_name="BuildingFootprints", where_clause="", #, config_keyword="")[0]

        
        # Process: Summarize Within (Summarize Within) (analysis)
        LandUseBuildings = "\\\\GISFile\\gisdata\\Department\\MSO\\Projects\\Internal\\CHM_Gontwz_landuseSuitabilityRerun\\Gonterwitz_Suitability_Rerun2022\\RESULTS_GontzGrowthProcess.gdb\\Results_2022\\LandUseBuildings"
        Output_Grouped_Table = ""
        arcpy.analysis.SummarizeWithin(in_polygons=LU2021, in_sum_features=BuildingFootprints, out_feature_class=LandUseBuildings, keep_all_polygons="KEEP_ALL", sum_fields=[["Shape_Area", "Sum"]], sum_shape="ADD_SHAPE_SUM", shape_unit="SQUAREFEET", group_field="", add_min_maj="NO_MIN_MAJ", add_group_percent="NO_PERCENT", out_group_table=Output_Grouped_Table)

        
        # Process: Feature Class To Feature Class (3) (Feature Class To Feature Class) (conversion)
        NewPermitsResidential = arcpy.conversion.FeatureClassToFeatureClass(in_features=Building_Permit_Points, out_path=Workspace_GDB, out_name="NewPermitsResidential", where_clause="Issued >= timestamp '2021-01-01 11:21:11' And Classification IN ('COMMERCIAL NEW MULTI-FAMILY', 'RESIDENTIAL NEW DUPLEX', 'RESIDENTIAL NEW SINGLE FAMILY')", #, config_keyword="")[0]

        
        # Process: Spatial Join (Spatial Join) (analysis)
        LandUseBuildingPermits_type01 = "\\\\GISFile\\gisdata\\Department\\MSO\\Projects\\Internal\\CHM_Gontwz_landuseSuitabilityRerun\\Gonterwitz_Suitability_Rerun2022\\RESULTS_GontzGrowthProcess.gdb\\Results_2022\\LandUseBuildingPermits_type01"
        arcpy.analysis.SpatialJoin(target_features=LandUseBuildings, join_features=NewPermitsResidential, out_feature_class=LandUseBuildingPermits_type01, join_operation="JOIN_ONE_TO_ONE", join_type="KEEP_ALL", #, match_option="INTERSECT", search_radius="", distance_field_name="")

        
        # Process: Spatial Join (3) (Spatial Join) (analysis)
        arcpy.analysis.SpatialJoin(target_features=LU2021, join_features=NewPermitsResidential, out_feature_class=LandUseBuildingPermits_type02, join_operation="JOIN_ONE_TO_ONE", join_type="KEEP_ALL", #, match_option="INTERSECT", search_radius="", distance_field_name="")

if __name__ == '__main__':
    Step01_01_LandUseBuildingPermits(*argv[1:])
