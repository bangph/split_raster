import os
import sys
import glob2

# Author: Bang Pham Huu - https://github.com/bangph
# Split all rasters in an input folder to different split output folders containing tile size 20000 x 20000

script_dir = os.path.dirname(os.path.realpath(__file__))

if len(sys.argv) != 3:
    print "Usage: python script.py ABSOLUTE_PATH_TO_FOLDER_CONTAINING_BIG_TIFF_FILES RASTER_EXTENSION (e.g: tiff or tif)"
    exit(0)

# Folder containing big tiff file
input_directory_path = sys.argv[1]
raster_extension = "." + sys.argv[2]

if not os.path.isdir(input_directory_path):
    print "Input is not a folder, given '{}'.".format(input_directory_path)
    exit(1)

if not os.path.isabs(input_directory_path):
    print "Input folder is not absolute, given '{}'.".format(input_directory_path)
    exit(1)

# Collect all raster files by extension (e.g: *.tiff) inside the folder
glob_path = input_directory_path + "/*" + raster_extension
raster_files = sorted(glob2.glob(glob_path))

if len(raster_files) == 0:
    print "No input files from glob path '{}'.".format(glob_path)
    exit(1)

for raster_file in raster_files:
    print "Splitting tiles for file '{}'...".format(raster_file)
    print ""
    command = "nohup python {}/split_raster.py {} &".format(script_dir, raster_file)
    result = os.system(command)
    if result != 0:
        print "Error splitting tiles."
        exit(1)
