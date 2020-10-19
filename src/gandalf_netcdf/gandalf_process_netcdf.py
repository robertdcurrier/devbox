#!/usr/bin/env python3
import sys
import xarray
import pandas as pd

def read_nc_file(nc_file):
    """
    Name: read_nc_file
    Created: 2020-06-04
    Modified: 2020-10-09
    Author: robertdcurrier@gmail.com
    Notes: Opens NetCDF file and uses xarray and pandas
    to create a slimmed down data frame. The new data frame is returned.
    """
    print('read_nc_file(): Attempting to read %s into data frame' % nc_file)
    try:
        data_set = xarray.open_dataset(nc_file)
        print('read_nc_file(): Successfully loaded %s' % nc_file)
        return data_set

    except IOError as error:
        print('read_nc_file(): Error %s. Aborting.' % error)
        sys.exit()

if __name__ == '__main__':
    data_set = read_nc_file(sys.argv[1])
    print(data_set)
