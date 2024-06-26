import os
import sys
from HateSpeech.logger import logging
from zipfile import ZipFile
from HateSpeech.exception import CustomException
from HateSpeech.configuration.GCP_syncer import GCloudSync
from HateSpeech.entity.config_entity import DataintegrationConfig
from HateSpeech.entity.artifact_entity import DataIngestionArtifacts


class DataIngestion:
    def __init__(self, data_ingestion_config: DataintegrationConfig):
        
        self.data_ingestion_config = DataintegrationConfig
        self.gcloud = GCloudSync

    def get_data_from_gcloud(self) ->None:
        try:
            logging.info("enter the get_data_from_gcloud method from DataIngestion class ")
            os.makedirs(self.data_ingestion_config.DATA_INGESTION_ARTIFACTS_DIR,exist_ok=True)
            self.gcloud.sync_folder_from_gcloud(self.data_ingestion_config.BUCKET_NAME,
                                                self.data_ingestion_config.ZIP_FILE_NAME,
                                                self.data_ingestion_config.DATA_INGESTION_ARTIFACTS_DIR)
            
            logging.info("Exited the get_data_from_gcloud method of data ingestion class")
        except Exception as e:
            raise  CustomException(e,sys) from e
        

    def unzip_and_clean(self):
        logging.info("Entered the unzip_and_clean method of data ingestion class ")

        try:
            with ZipFile(self.data_ingestion_config.ZIP_FILE_PATH,'r') as zip_ref:
                zip_ref.extractall(self.data_ingestion_config.ZIP_FILE_DIR)

            logging.info("exited the unzip_and_clean method of class data ingestion class ")

            return self.data_ingestion_config.DATA_ARTIFACTS_DIR,self.data_ingestion_config.NEW_DATA_ARTIFACTS_DIR


        
        except Exception as e:
            
            raise CustomException(e,sys) from e

    def initite_data_ingestion_config(self):
        logging.info("enter the data initiate_data_ingestion method of Data ingestion class")

        try:
            self.get_data_from_gcloud()
            logging.info("Fetched the data from S3 bucket")
            imbalance_data_file_path, raw_data_file_path = self.unzip_and_clean()

            logging.info("Unzipped file and split into train and valid")

            data_ingestion_artifacts = DataIngestionArtifacts(imbalance_data_file_path=imbalance_data_file_path,
                                                              raw_data_file_path=raw_data_file_path)

            logging.info("Exited the initiate_data_ingestion method of Data ingestion class")

            logging.info(f"Data ingestion artifact: {data_ingestion_artifacts}")

            return data_ingestion_artifacts

        except Exception as e:
            raise CustomException(e, sys) from e
        