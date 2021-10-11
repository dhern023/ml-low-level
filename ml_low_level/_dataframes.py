# -*- coding: utf-8 -*-
"""
low-level methods useful enough to be a part of any pandas toolkit

Those with the flavor tag extend the pandas API.
"""

import pandas
import pandas_flavor

def construct_frequency_dict(dataframe, column):
    series = dataframe[column]
    return series.value_counts().to_dict()

def check_has_nans(dataframe):
    mask_has_nans = dataframe.isnull()
    return mask_has_nans.sum() != 0

def count_nans_in_column(dataframe, column):
    # a mask is a True/False series
    nan_mask = dataframe[column].isna()
    
    # counts the number of true's
    return nan_mask.sum()

def check_column_has_nan(dataframe, column):
    # a mask is a True/False series
    nan_mask = dataframe[column].isna()
    bool_has_nan = nan_mask.any()
    
    return bool_has_nan

def check_dataframe_equality(dataframe1, dataframe2):
    return (dataframe1 == dataframe2).any()

def factorize_column(dataframe, column, **kwargs):
    """ 
    Replaces column with a categorical factorized column
    I'm not sure if it should be simply appended or replace 
    
    Returns dataframe with updated column, labels
    """
    series, labels = pandas.factorize(dataframe[column], **kwargs)
    dataframe.loc[:, column] = series
    dataframe[column] = dataframe[column].astype('category')

    return dataframe, labels

def defactorize_column(dataframe, column, labels):
    pass

def factorized_columns(dataframe, list_columns, **kwargs):
    """
    Adds a categorical & factorizes column (default),
    and returns a dataframe, dictionary { column : labels }
    """
    dict_labels = {}
    dataframe_p = dataframe.copy()
    for column in list_columns:
        series, labels = pandas.factorize(dataframe[column])
        dict_labels[column] = labels
        dataframe_p.loc[:, column] = series
        dataframe_p.loc[:, column] = dataframe_p[column].astype('category')
    
    return dataframe_p, dict_labels

# Flavored =====================================================

@pandas_flavor.register_dataframe_method
def set_column_to_dtype(dataframe, column, dtype = 'category'):
    """
    dtype : str, should be able to be interpreted by pandas astype()
    """    
    dataframe_processed = dataframe.copy()
    dataframe_processed[column] = dataframe_processed[column].astype(dtype)
    
    return dataframe_processed

@pandas_flavor.register_dataframe_method
def convert_column_to_datetime(dataframe, column):
    dataframe[column] = pandas.to_datetime(dataframe[column])
    return dataframe

# Filtering Columns ==============================

@pandas_flavor.register_dataframe_method
def select_column_subset(dataframe, list_columns):
    return dataframe[list_columns]

# Filtering Rows =================================

@pandas_flavor.register_dataframe_method
def select_rows_by_column_value(dataframe, column, value):
    mask_has_value = dataframe[column] == value
    return dataframe[mask_has_value]

@pandas_flavor.register_dataframe_method
def drop_rows_by_column_value(dataframe, column, value):
    mask_has_value = dataframe[column] == value
    return dataframe[mask_has_value]
        
@pandas_flavor.register_dataframe_method
def drop_nans_in_column(dataframe, column):
    valid_mask = dataframe[column].notnull()
    return dataframe[valid_mask]        

@pandas_flavor.register_dataframe_method
def drop_valid_values_in_column(dataframe, column):
    null_mask = dataframe[column].isnull()
    return dataframe[null_mask]        

# Numerical =======================================

@pandas_flavor.register_dataframe_method
def scale(dataframe, array_scaler=None):
    """
    Calls scaler function on dataframe.values,
    then creates new dataframe with same columns
    """
    if array_scaler is None:
        return dataframe

    list_columns = dataframe.columns.tolist()

    array = dataframe.values
    array_scaled = array_scaler(array)
    df = pandas.DataFrame(
        array_scaled, columns = list_columns)
    
    return df
