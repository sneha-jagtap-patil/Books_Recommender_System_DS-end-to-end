import os
import sys
import shutil
import zipfile
from six.moves import urllib
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
        
    

    def download_data(self):
        """
        Fetch the data from the url or copy from local path
        """
        try:
            dataset_source = self.data_ingestion_config.dataset_download_url
            raw_data_dir = self.data_ingestion_config.raw_data_dir
            os.makedirs(raw_data_dir, exist_ok=True)

            if dataset_source.startswith(('http://', 'https://')):
                data_file_name = os.path.basename(dataset_source)
                zip_file_path = os.path.join(raw_data_dir, data_file_name)
                logging.info(f"Downloading data from {dataset_source} into file {zip_file_path}")
                urllib.request.urlretrieve(dataset_source, zip_file_path)
                logging.info(f"Downloaded data from {dataset_source} into file {zip_file_path}")
                return zip_file_path, True
            else:
                # Assuming it's a local directory path
                logging.info(f"Copying data from local path {dataset_source} into {raw_data_dir}")
                for file_name in os.listdir(dataset_source):
                    if file_name.endswith('.csv'):
                        shutil.copy(os.path.join(dataset_source, file_name), raw_data_dir)
                logging.info(f"Copied CSV files from {dataset_source} to {raw_data_dir}")
                return raw_data_dir, False

        except Exception as e:
            raise AppException(e, sys) from e


    def extract_zip_file(self, zip_file_path: str):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        """
        try:
            ingested_dir = self.data_ingestion_config.ingested_dir
            os.makedirs(ingested_dir, exist_ok=True)
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(ingested_dir)
            logging.info(f"Extracting zip file: {zip_file_path} into dir: {ingested_dir}")
        except Exception as e:
            raise AppException(e, sys) from e

    
    def initiate_data_ingestion(self):
        try:
            source_path, is_zip = self.download_data()
            if is_zip:
                self.extract_zip_file(zip_file_path=source_path)
            else:
                # If it was a local directory, files are already in raw_data_dir, 
                # move/copy them to ingested_dir if necessary
                ingested_dir = self.data_ingestion_config.ingested_dir
                os.makedirs(ingested_dir, exist_ok=True)
                for file_name in os.listdir(source_path):
                    if file_name.endswith('.csv'):
                        shutil.copy(os.path.join(source_path, file_name), ingested_dir)
                logging.info(f"Data moved to {ingested_dir}")
            
            logging.info(f"{'='*20}Data Ingestion log completed.{'='*20} \n\n")
        except Exception as e:
            raise AppException(e, sys) from e