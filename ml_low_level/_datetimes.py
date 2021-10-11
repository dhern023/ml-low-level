"""
Handles situations in which date data within a dataframe
are stored as individual items (e.g. year, month, date, or stored as text
"""

import datetime
import numpy
import pandas

def get_day_of_year(date_object):
    """
    Gets the day of the year from the timestamp object
    January 1 = 0

    pandas dayofyear returns 1-366 depending on leap year
    
    returns 0-365 depending on leap year
    """
    if isinstance(date_object, datetime.date):
        return date_object.timetuple().tm_yday - 1

    if isinstance(date_object, pandas.Timestamp):
        return date_object.dayofyear - 1
    
    #default error
    return 366

def create_day_of_year_array(date_series):
    """ Low level version of construct_day_of_year_column() """
    day_of_year = numpy.zeros(len(date_series), dtype = numpy.int)

    for index in date_series.index:
        day_of_year[index] = get_day_of_year(date_series[index])
    return day_of_year
