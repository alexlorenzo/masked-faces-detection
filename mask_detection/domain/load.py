import pandas as pd


def load_iris(filename):
    """Load iris dataset from filename

    Parameters
    ----------
    filename: str
        absolute path to iris dataset

    Returns
    -------
    iris: pd.DataFrame
    """
    dtype = {
        'sepal_length': float,
        'sepal_width': float,
        'petal_length': float,
        'petal_width': float,
        'species': str,
    }
    df = pd.read_csv(filename, sep=",", usecols=dtype.keys(), dtype=dtype)
    return df


def query_database():
    """
    This function is created in order to show an example of mock tests
    """
    raise NotImplementedError
