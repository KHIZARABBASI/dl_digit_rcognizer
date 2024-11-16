from Digit_Recognizer.config.configration import ConfigurationManager
from Digit_Recognizer.components.model_training import ModelTraining
from Digit_Recognizer import logger

STAGE_NAME = "Model Training"

def main():
    config = ConfigurationManager()
    model_training_config = config.get_model_training_config()
    logger.info(f"Model Training pipeline started with configuration: {model_training_config}")

    model_training = ModelTraining(config=model_training_config)
    logger.info(f"Training model using configuration: {model_training_config}")
    model_training.train_model()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e