from Digit_Recognizer.config.configration import ConfigurationManager
from Digit_Recognizer.components.data_transformation import DataTransformation
from Digit_Recognizer import logger

STAGE_NAME = "Data Transformation stage"




class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):

        config_manager = ConfigurationManager()
        data_transformation_config = config_manager.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.augment_and_save_data()
        # config = ConfigurationManager()
        # data_validation_config = config.get_validation_config()
        # data_validation = DataValidation(config=data_validation_config)
        # data_validation.check_files_exist()
        # data_validation.validate_shapes(config=data_validation_config)
        # data_validation.validate_data_values(config=data_validation_config)
        # data_validation.check_for_missing_values(config=data_validation_config)

        logger.info(f"Data Transforation pipeline completed")

