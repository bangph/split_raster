import os
import sys
import gdal
import subprocess

# Author: Bang Pham Huu - https://github.com/bangph
# Split big raster which rasdaman cannot import to tile with size 20000 x 20000
script_dir = os.path.dirname(os.path.realpath(__file__))

if len(sys.argv) == 1:
    print "Usage: python script.py ABSOLUTE_PATH_TO_BIG_TIF_FILE"
    exit(0)

# Split tile to this size 
tile_size_x = 20000
tile_size_y = 20000

big_file_path = sys.argv[1]

if not os.path.isabs(big_file_path):
    print "Path to input big tiff file must be absolute, given '{}'.".format(big_file_path)
    exit(1)

# Folder containing big tiff file
input_directory_path = os.path.dirname(big_file_path)

# File name (without extension)
big_file_name = os.path.splitext(os.path.basename(big_file_path))[0]
 
# Create output folder to store tiles of this big tiff file
out_path = input_directory_path + '/split_output/' + big_file_name.rsplit(".")[0] + "/"
if not os.path.exists(out_path):
    os.makedirs(out_path)

# As gdal_retile does not have problem to expand image's boundaries unnecessarily, use it to have the best performance
command = 'gdal_retile.py -targetDir {} {} -ps {} {} -co "COMPRESS=LZW" -co "PREDICTOR=2" -co "TILED=YES" -v'.format(out_path, big_file_path, tile_size_x, tile_size_y)
p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, error = p.communicate()

if p.returncode != 0:
    print "***Error*** when retiling big tif file. Reason: " + error
    exit(1)
else:
    print "Done for file '" + big_file_path + "'."


"""
Using gdal_translate to tile files (not good as the boundaries are extented from original files)

output_filename = 'tile_'
 
ds = gdal.Open(big_file_path)
band = ds.GetRasterBand(1)
xsize = band.XSize
ysize = band.YSize
 
for i in range(0, xsize, tile_size_x):
    for j in range(0, ysize, tile_size_y):
        tile_file_path = str(out_path) + str(output_filename) + str(i) + "_" + str(j) + ".tif"
        com_string = "gdal_translate -of GTIFF " + ' -co "COMPRESS=LZW" -co "PREDICTOR=2" -co "TILED=YES" -srcwin ' + str(i)+ ", " + str(j) + ", " + str(tile_size_x) + ", " + str(tile_size_y) + " " + big_file_path + " " + tile_file_path
        os.system(com_string)
"""
