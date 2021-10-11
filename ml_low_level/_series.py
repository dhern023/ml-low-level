# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 08:13:54 2021

@author: Peanut
"""

import pandas
import pandas_flavor

# Series
# convert_to_datetime already exists
# astype already exists

@pandas_flavor.register_series_method
def create_rolling_window_mean_series(series, window_size = 25):
    """ https://en.wikipedia.org/wiki/Moving_average """
    return series.rolling(window_size).mean()

# Filtering =================================

@pandas_flavor.register_series_method
def select_value(series, value):
    mask_has_value = series == value
    return series[mask_has_value]

@pandas_flavor.register_series_method
def drop_value(series, value):
    mask_has_value = series == value
    return series[mask_has_value]

@pandas_flavor.register_series_method
def drop_nans(series):
    valid_mask = series.notnull()
    return series[valid_mask]

@pandas_flavor.register_series_method
def drop_valid_values(series):
    null_mask = series.isnull()
    return series[null_mask]