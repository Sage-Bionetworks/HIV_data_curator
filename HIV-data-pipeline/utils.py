# allows specifying explicit variable types
from typing import Any, Dict, Optional, Text

import pandas as pd

def update_df(existing_df:pd.DataFrame, new_df:pd.DataFrame, idx_key:str) -> pd.DataFrame:
    """ Updates an existing data frame with the entries of another dataframe on a given primary index

    Args: 
        existing_df : data frame to be updated
        new_df: data frame to update with
        idx_key: name of primary index column

    Returns: an updated data frame if the index column is present in both the existing and new data frames; ow returns the existing data frame w/o changes; the column set of the existing data frame are not updated (i.e. schema is preserved)
    """

    if not (idx_key in existing_df.columns and idx_key in new_df):
        return existing_df

    # merge the two data frames keeping all the resulting data in new and existing columns
    updated_df = pd.merge(existing_df, new_df, how = "outer", on = idx_key, suffixes = ("_existing", "_new"))

    # filter to keep only updated values when available across all columns in the schema
    for col in existing_df.columns:
        if col != idx_key:
            existing_col = col + "_existing"
            new_col = col + "_new"

            updated_df[col] = updated_df[existing_col].where(updated_df[new_col].isnull(), updated_df[new_col])

    # remove unnecessary columns and keep existing schema
    updated_df = updated_df[existing_df.columns]

    return updated_df


def execute_google_api_requests(service, requests_body, **kwargs):
    """
    Execute google API requests batch; attempt to execute in parallel
    Args:
        service: google api service; for now assume google sheets service that is instantiated and authorized
        service_type: default batchUpdate; TODO: add logic for values update
        kwargs: google API service parameters
    Return: google API response
    """

    if "spreadsheet_id" in kwargs and "service_type" in kwargs and kwargs["service_type"] == "batch_update":

        # execute all requests

        response = service.spreadsheets().batchUpdate(spreadsheetId=kwargs["spreadsheet_id"], body = requests_body).execute()
        
        return response
