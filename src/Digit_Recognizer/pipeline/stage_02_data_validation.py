from Digit_Recognizer.components.data_ingestion import DataIngestion
from Digit_Recognizer.components.data_validation import DataValidation
from Digit_Recognizer import logger
from Digit_Recognizer.config.configration import ConfigurationManager



STAGE_NAME = "Data validtion stage"


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.check_files_exist()
        data_validation.validate_shapes(config=data_validation_config)
        data_validation.validate_data_values(config=data_validation_config)
        data_validation.check_for_missing_values(config=data_validation_config)

        logger.info(f"Data Ingestion pipeline completed")



# if __name__ == '__main__':
#     try:
#         logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
#         obj = DataIngestionTrainingPipeline()
#         obj.main()
#         logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
#     except Exception as e:
#         logger.exception(e)
#         raise e