import os
import sys
from six.moves import urllib
import zipfile
from books_recommender.logger.log import logging
from books_recommender.exception.exception_handler import AppException
from books_recommender.config.configuration import AppConfiguration

class DataIngestion:

    def __init__(self, app_config = AppConfiguration()):
        """
        DataIngestion Intialization
        data_ingestion_config: DataIngestionConfig 
        """
        try:
            logging.info(f"{'='*20}Data Ingestion log started.{'='*20} ")
            self.data_ingestion_config= app_config.get_data_ingestion_config()
        except Exception as e:
            raise AppException(e, sys) from e
        