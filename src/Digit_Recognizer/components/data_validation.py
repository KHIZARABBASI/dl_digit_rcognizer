from Digit_Recognizer.entity.config_entity import DataValidationConfig
import numpy as np
import os
from Digit_Recognizer.config.configration import ConfigurationManager

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config


    def check_files_exist(self ):
        config = self.config
        for file in self.config.data_files:
            if os.path.exists(file) and os.path.getsize(file) > 0:
                print(f"{file} is present and non-empty.")
            else:
                raise ValueError(f"{file} is missing or empty.")
            print(f"{file} is present and non-empty.")
            

# a = ConfigurationManager()
# valid = a.get_validation_config()
# obj =  DataValidation(valid)
# obj.check_files_exist()


