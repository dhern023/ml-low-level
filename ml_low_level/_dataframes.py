# -*- coding: utf-8 -*-
"""
@author: Peanut
"""

class DataframeLowLevel():
    """
    low-level methods useful enough to be a part of any pandas toolkit
    """

    @staticmethod
    def construct_frequency_dict(dataframe, column):
        series = dataframe[column]
        return series.value_counts().to_dict()

    @staticmethod
    def set_column_to_dtype(dataframe, column, dtype = 'category'):
        """
        dtype : str, should be able to be interpreted by pandas astype()
        """    
        dataframe_processed = dataframe.copy()
        dataframe_processed[column] = dataframe_processed[column].astype(dtype)
        
        return dataframe_processed

    @staticmethod
    def check_has_nans(dataframe):
        mask_has_nans = dataframe.isnull()
        return mask_has_nans.sum() != 0

    @staticmethod
    def select_rows_with_value_in_column(dataframe, column, value):
        mask_has_value = dataframe[column] == value
        return dataframe[mask_has_value]
        
    @staticmethod
    def drop_nans_in_column(dataframe, column):
        valid_mask = dataframe[column].notnull()
        return dataframe[valid_mask]        

    @staticmethod
    def drop_valid_values_in_column(dataframe, column):
        null_mask = dataframe[column].isnull()
        return dataframe[null_mask]        

    @staticmethod
    def select_column_subset(dataframe, list_columns):
        return dataframe[list_columns]
        
    @staticmethod
    def count_nans_in_column(dataframe, column):
        # a mask is a True/False series
        nan_mask = dataframe[column].isna()
        
        # counts the number of true's
        return nan_mask.sum()

    @staticmethod    
    def check_column_has_nan(dataframe, column):
        # a mask is a True/False series
        nan_mask = dataframe[column].isna()
        bool_has_nan = nan_mask.any()
        
        return bool_has_nan

    @staticmethod
    def check_dataframe_equality(dataframe1, dataframe2):
        return (dataframe1 == dataframe2).any()
