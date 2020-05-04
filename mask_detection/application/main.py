"""
Main script of the application. Does the following:
 - load and clean iris dataset
 - perform a test prediction
 - save prediction results

To start the pipeline:

.. code-block:: shell

    $ . activate.sh
    $ python mask_detection/application/main.py
    # Or, Alternatively
    $ . activate.sh
    $ make pipeline

"""
import logging

from mask_detection.domain import load, clean
from mask_detection.infrastructure.files import FileManager
from mask_detection import settings

files = FileManager(settings.DATA_DIR)


def run():
    logging.info('Running main application script')
    do_cleaning()
    logging.info('Main application script completed.')


def do_cleaning():
    logging.debug('Doing cleaning')
    raw_filepath = files.get_filepath('raw/iris.csv')
    iris = load.load_iris(raw_filepath)
    iris = clean.clean_iris(iris)
    files.save(iris, 'clean/iris.pickle')
    logging.debug('Finished cleaning')


if __name__ == "__main__":
    run()
