def upper_cased_header(df):
    df.columns = [header.upper() for header in df.columns]
    return df


def fillna_mean(df, columns):
    """Fill missing values with mean of a given column.

    Parameters
    ----------
    df: pd.DataFrame
        dataframe to apply cleaning
    columns: list of str
        list with the name of the columns to clean

    Returns
    -------
    df: pd.DataFrame
        dataframe

    """
    for column in columns:
        mean = df[column].mean()
        df[column].fillna(mean, inplace=True)
    return df
