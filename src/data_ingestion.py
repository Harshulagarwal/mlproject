import os
import sys
from exception import CustomException as CE
from logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data = os.path.join('artifacts', "train.csv")
    test_data = os.path.join('artifacts', "test.csv")
    raw_data = os.path.join('artifacts', "raw.csv")


class DataIngesion:

    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def ingestion_initiate(self):
        logging.info("ingestion initialized")
        try:
            # read data
            data = pd.read_csv("C:\\Users\\harsh\\Downloads\\pgdai\\ML1\\mediacompany.csv")
            logging.info("file read")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data), exist_ok=True)

            data.to_csv(self.ingestion_config.raw_data, index=False, header=True)

            train_set, test_set = train_test_split(data, test_size= 0.2, random_state = 42)
   
            train_set.to_csv(self.ingestion_config.train_data, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data, index=False, header=True)

            logging.info("ingestion complete")
            return (self.ingestion_config.train_data, self.ingestion_config.test_data)
        except Exception as e:
            raise CE(e, sys)


if __name__=="__main__":
    obj = DataIngesion()
    obj.ingestion_initiate()            



        


