import os
import pandas
import shutil

# start_path = r'\\utilities\engineering\Shared\GPS_Surveys'
start_path = r'\\GISFile\gisdata'
file_extension = '.job'  # Change this to the desired file extension
#result = find_files(start_path, file_extension)

file_paths = []

for root, dirs, files in os.walk(start_path):
    for file in files:
        if file.endswith(file_extension):
            file_path = os.path.join(root, file)
            file_paths.append(file_path)

cols = ['filepath', 'name']
df = pandas.DataFrame()
df['Filepaths'] = file_paths
df.to_csv(r"\\GISFile\gisdata\Department\MSO\Projects\Internal\CHM_editMaps\19 GPS shot imports 2023 MASTER\00 JOB redux\JOB archive\SourcesList_AllGISFILE.csv", index=False)

outputLocation = r"\\GISFile\gisdata\Department\MSO\Projects\Internal\CHM_editMaps\19 GPS shot imports 2023 MASTER\00 JOB redux\JOB archive"
continueCue = input(f"Add all these files to {outputLocation}? Type 'Yes' if so ...\n")

if continueCue == "Yes":
    for item in file_paths:
        shutil.copy2(item, outputLocation)