import sys 
from HateSpeech.logger import logging
from HateSpeech.exception import CustomException
from HateSpeech.components.data_ingestion import DataIngestion
from HateSpeech.entity.config_entity import DataintegrationConfig
from HateSpeech.entity.artifact_entity import DataIngestionArtifacts


class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataintegrationConfig
    
    def start_data_ingestion(self) -> DataIngestionArtifacts:
        logging.info("Entered the start_data_ingestion method of TrainPipeline class")
        try:
            logging.info("Getting the data from GCLoud Storage bucket")
            data_ingestion = DataIngestion(data_ingestion_config = self.data_ingestion_config)

            data_ingestion_artifacts = data_ingestion.initiate_data_ingestion()
            logging.info("Got the train and valid from GCLoud Storage")
            logging.info("Exited the start_data_ingestion method of TrainPipeline class")
            return data_ingestion_artifacts

        except Exception as e:
            raise CustomException(e, sys) from e
        

    
    def run_pipeline(self):
        logging.info("Enter the running pipeline method of Training pipeline")

        try:
            data_ingestion_artifacts = self.start_data_ingestion()


            logging.info("Existed the run_pipeline method of Training pipeline class")
            

        
        except Exception as e:
            raise CustomException(e,sys) from e

