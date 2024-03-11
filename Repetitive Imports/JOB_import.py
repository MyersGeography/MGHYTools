import arcpy

# Set the workspace (path to your geodatabase)
arcpy.env.workspace = r'C:\Path\to\Your\Geodatabase.gdb'

# Set the name of the feature class to which you want to append points
feature_class = 'YourFeatureClass'

# Create a list of points (X, Y coordinates) - replace these with your actual points
points = [(100, 200), (150, 250), (200, 300)]

# Create a new InsertCursor to append points to the feature class
with arcpy.da.InsertCursor(feature_class, ['SHAPE@XY']) as cursor:
    for point in points:
        cursor.insertRow([point])

print("Points appended successfully.")