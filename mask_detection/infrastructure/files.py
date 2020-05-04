"""
This module provides convenient function to load and save from the
application's `data/` folder (as defined in the config).
"""
import logging
import os

import pandas as pd


class FileManager:
    """Utility class to handle data files contained in a root folder

    Parameters
    ----------
    root: str
        absolute path to the root data folder


    >>> files = FileManager('/path/to/data/')
    >>> df = files.load('raw/iris.csv')
    # Loads dataframe from /path/to/data/raw/iris.csv
    >>> files.save(df, 'clean/iris.pickle')
    # saves to /path/to/data/clean/iris.pickle
    # end ensures 'clean' folder exists
    """

    def __init__(self, root):
        root = os.path.abspath(root)
        if not os.path.exists(root):
            raise ValueError('Provided path {} does not exist.'.format(root))
        self.root = root

    def get_filepath(self, relative_path, create_folders=False):
        """Returns absolute path from relative to ``data/`` folder"""
        path = os.path.abspath(os.path.join(self.root, relative_path))
        if create_folders:
            self.ensure_folder_exists(path)
        return path

    def ensure_folder_exists(self, abspath):
        """ creates subfolders if necessary """
        if not os.path.isabs(abspath):
            raise ValueError('path "{}" is not absolute'.format(abspath))

        path, extension = os.path.splitext(abspath)
        if extension:
            # if it was a file we only take the folder
            path = os.path.dirname(path)
        if not os.path.exists(path):
            os.makedirs(path)

    def save(self, thing, relative_path, *args, **kwargs):
        """Save object (usually dataframe) to file

        Additional ``*args`` and ``**kwargs`` are passed to the underlying function.


        >>> df = pd.DataFrame()
        >>> files.save(df, 'clean/iris.pickle')
        """
        path = self.get_filepath(relative_path, create_folders=True)
        _, extension = os.path.splitext(path)
        if extension == ".pickle":
            # assuming this is a pandas df
            logging.debug('Saving object to ' + path)
            thing.to_pickle(path, *args, **kwargs)
        else:
            logging.error('Cannot save to {}. Unkown extension: {}'.format(path, extension))
            raise NotImplementedError('Extension {} not handled by files.save()'.format(extension))

    def load(self, relative_path, *args, **kwargs):
        """Loads .pickle and .csv from file relative to  ``data/`` folder

        Parameters
        ----------
        relative_path: str
            path relative to the application ``data/`` folder
        args:
            those are passed to the inner load function
        kwargs:
            those are passed to the inner load function


        >>> # this loads the file /path/to/data/raw/iris.csv
        >>> df = files.load('raw/iris.csv', nrows=10, dtype='str')
        """
        path = self.get_filepath(relative_path)
        _, extension = os.path.splitext(path)
        logging.debug('Loading from: ' + path)
        if extension == ".pickle":
            return pd.read_pickle(path, *args, **kwargs)
        elif extension == ".csv":
            return pd.read_csv(path, *args, **kwargs)
        else:
            logging.error(
                'Impossible to load from {}. Unkown extention : {}'.format(path, extension)
            )
            raise NotImplementedError('Extension {} not handled by files.load()'.format(extension))
