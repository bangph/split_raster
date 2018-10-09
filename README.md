# split_raster
Use gdal to split a big raster image to compressed tiles.

Usaged:
python split_raster.py ABSOLUTE_PATH_TO_YOUR_BIG_TIF_FILE (e.g: python split_raster.py /tmp/bigtiff.tif).

Output:
A new folder called /tmp/bigtiff/split_output is created with smaller tiff files with size 20000 x 20000.
