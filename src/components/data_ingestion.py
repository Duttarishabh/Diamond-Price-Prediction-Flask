import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

##initializd the data ingestion configuration
@dataclass
class DataIngestionconfig:
    train_data_path=os.path.join('artifacts','train.csv')
    test_data_path=os.path.join('artifacts','test.csv')
    raw_data_path=os.path.join('artifacts','raw.csv')



# initialize the data ingetion class     
class DataIngestion:
    def __init__(self):
     self.ingestion_config=DataIngestionconfig()
       

    def initiate_data_ingestion(self):
       logging.info('Data Ingestion starts')
       
       try:
        # Read dataset
        df = pd.read_csv(os.path.join('notebook/data', 'gemstone.csv'))
        logging.info("Data read as a pandas DataFrame")

        # Create directories if they don't exist
        os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
        
        # Save raw data
        df.to_csv(self.ingestion_config.raw_data_path, index=False)
        
        # Train-Test Split
        logging.info('Performing Train Test Split')
        train_set, test_set = train_test_split(df, test_size=0.30, random_state=42)

        # Save train and test datasets
        train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
        test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

        logging.info("Ingestion of data is completed")
        return self.ingestion_config.train_data_path, self.ingestion_config.test_data_path
       except Exception as e:
        logging.error(f"Error occurred in Data Ingestion: {str(e)}")
        raise e  # Raise the exception to avoid returning None
