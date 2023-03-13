# -*- coding: utf-8 -*-
import arcpy
from arcpy.management import SelectLayerByAttribute
from arcpy.management import SelectLayerByLocation
from arcpy.conversion import TableToExcel

gdb = r"\\GISFile\gisdata\Department\MSO\Projects\Internal\CHM_analysisProjects\2022\04 Lashley mailing lists\LashleyMailings.gdb"


def parcel_export():
    arcpy.env.overwriteOutput = True

    # arcpy.ImportToolbox(r"c:\program files\arcgis\pro\Resources\ArcToolbox\toolboxes\Conversion Tools.tbx.tbx")

    Parcels = r"https://gisweb.lawrenceks.org/hosting/rest/services/Basemap/Parcels/FeatureServer/0"
    InterestArea = gdb + "\ProjectAreas"

    # asking for the input value for querying the shape name and then naming the excel table.
    ShapeName = input('Which selection area are we generating an excel table for?')

    # Select Layer By Attribute (Select Layer By Attribute) (management)
    IsolatedArea, count = SelectLayerByAttribute(in_layer_or_view=InterestArea, selection_type="NEW_SELECTION",
                                             where_clause=f"name = '{ShapeName}'")
    print('Looking for a Selection Polygon ...')
    # Select Layer By Location (Select Layer By Location) (management)

    if int(count) > 0:
        ParcelsSelected = SelectLayerByLocation(in_layer=Parcels,
                                           overlap_type="INTERSECT",
                                           select_features=IsolatedArea,
                                           search_distance="",
                                           selection_type="NEW_SELECTION",
                                           invert_spatial_relationship="NOT_INVERT")
    else:
        print("Nothing was selected under the Selection Shape")

    # Table To Excel (Table To Excel) (conversion)
    OutputExcelTable = f"\\\\GISFile\\gisdata\\Department\\MSO\\Projects\\Internal\\CHM_analysisProjects\\2022\\04 Lashley mailing lists\\09 September Requests\\02 excel exports raw\\{ShapeName}_table.xls"

    TableToExcel(Input_Table=ParcelsSelected, Output_Excel_File=OutputExcelTable,
                 Use_field_alias_as_column_header="NAME", Use_domain_and_subtype_description="CODE")

    print("Making the Excel table")


if __name__ == '__main__':
    # Global Environment settings
    with arcpy.EnvManager(scratchWorkspace=gdb, workspace=gdb):
        parcel_export()
