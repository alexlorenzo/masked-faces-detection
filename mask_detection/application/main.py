"""
Main script of the application.

To start the pipeline:

.. code-block:: shell

    $ . activate.sh
    $ python mask_detection/application/main.py
"""
import logging
from mask_detection import settings as stg
from mask_detection.infrastructure.scrapping import SearchDownload


def run():
    logging.info('Scrap Images')
    SearchDownload.search_and_download(search_term=stg.SEARCH_TERM,
                                       driver_path=stg.DRIVER_PATH,
                                       target_path='../data/images',
                                       number_images=100)   