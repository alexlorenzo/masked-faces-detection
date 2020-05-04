from mask_detection.domain import load
from mask_detection.infrastructure import technical_cleaning


def clean_iris(iris):
    """Cleans the iris dataset

    Parameters
    ----------
    iris: pd.DataFrame
        at least with with columns 'SEPAL_WIDTH', 'SEPAL_LENGTH',
        'PETAL_LENGTH', 'PETAL_WIDTH'

    Returns
    -------
    iris: pd.DataFrame
        same shape as input. Columns are uppercase, no missing values
    """
    iris = technical_cleaning.upper_cased_header(iris)
    columns = ['SEPAL_WIDTH', 'SEPAL_LENGTH', 'PETAL_LENGTH', 'PETAL_WIDTH']
    iris = technical_cleaning.fillna_mean(iris, columns)
    return iris


def clean_data_from_database(columns):
    """clean data from a database.

    Note: query_database() return a dataframe with data from database.

    Returns
    -------
    cleaned_data: pd.dataframe
        cleaned dataframe
    """
    data = load.query_database()
    cleaned_df = technical_cleaning.fillna_mean(data, columns)
    return cleaned_df
