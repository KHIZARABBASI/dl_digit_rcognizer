from Digit_Recognizer.entity.config_entity import DataValidationConfig
import numpy as np
import os
from Digit_Recognizer.config.configration import ConfigurationManager
from Digit_Recognizer import logger

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config


    def write_status(self, message):
        # Write a message to the status file
        with open(self.config.status_file, "a") as f:
            f.write(message + "\n")


    def check_files_exist(self ):
        # config = self.config
        for file in self.config.data_files:
            if os.path.exists(file) and os.path.getsize(file) > 0:
                print(f"{file} is present and non-empty.")
                logger.info(f"{file} is present and non-empty.")
                self.write_status(f"{file} is present and non-empty.")
            else:
                self.write_status(f"{file} is missing or empty.")
                logger.error(f"{file} is missing or empty.")#include <iostream>
                raise ValueError(f"{file} is missing or empty.")
            print(f"{file} is present and non-empty.")
            logger.info(f"{file} is present and non-empty.")
            self.write_status(f"{file} is present and non-empty.")
        


    def validate_shapes(self, config):
        # Load files using paths from the config
        x_train = np.load(config.data_files[0])
        y_train = np.load(config.data_files[1])
        x_test = np.load(config.data_files[2])
        y_test = np.load(config.data_files[3])

        # Perform shape validation
        assert x_train.shape == (60000, 28, 28), f"x_train shape mismatch: {x_train.shape}"
        assert x_test.shape == (10000, 28, 28), f"x_test shape mismatch: {x_test.shape}"
        assert y_train.shape == (60000,), f"y_train shape mismatch: {y_train.shape}"
        assert y_test.shape == (10000,), f"y_test shape mismatch: {y_test.shape}"

        print("All data shapes are correct.")
        logger.info("All data shapes are correct.")
        self.write_status("All data shapes are correct.")


    def validate_data_values(self,config):
        # Load files using paths from the config
        x_train = np.load(config.data_files[0])
        y_train = np.load(config.data_files[1])
        x_test = np.load(config.data_files[2])
        y_test = np.load(config.data_files[3])

        # Pixel values should be between 0 and 255
        assert x_train.min() >= 0 and x_train.max() <= 255, "x_train pixel values out of range."
        assert x_test.min() >= 0 and x_test.max() <= 255, "x_test pixel values out of range."

        # Labels should be integers between 0 and 9
        assert y_train.min() >= 0 and y_train.max() <= 9, "y_train labels out of range."
        assert y_test.min() >= 0 and y_test.max() <= 9, "y_test labels out of range."

        print("Data values are within expected ranges.")

        logger.info("Data values are within expected ranges.")
        self.write_status("Data values are within expected ranges.")


    def check_for_missing_values(self,config):
        # Load files using paths from the config
        x_train = np.load(config.data_files[0])
        y_train = np.load(config.data_files[1])
        x_test = np.load(config.data_files[2])
        y_test = np.load(config.data_files[3])

        assert not np.isnan(x_train).any(), "x_train contains NaN values."
        assert not np.isnan(x_test).any(), "x_test contains NaN values."
        assert not np.isnan(y_train).any(), "y_train contains NaN values."
        assert not np.isnan(y_test).any(), "y_test contains NaN values."

        print("No missing values detected.")
        logger.info("No missing values detected.")
        self.write_status("No missing values detected.")




# a = ConfigurationManager()
# valid = a.get_validation_config()
# obj =  DataValidation(valid)
# obj.check_files_exist()


