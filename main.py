from Digit_Recognizer import logger
from Digit_Recognizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Digit_Recognizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from Digit_Recognizer.pipeline.stage_03_data_transformation import DataTransformationPipeline
# from mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
# from mlProject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
# from mlProject.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline



STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_velidation = DataValidationTrainingPipeline()
   data_velidation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Data Transormation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_transformation = DataTransformationPipeline()
   data_transformation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
