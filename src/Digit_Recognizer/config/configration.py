from Digit_Recognizer.constants import *
from Digit_Recognizer.utils.common import read_yaml, create_directories
from Digit_Recognizer.entity.config_entity import (DataIngestionConfig,
                                                   DataValidationConfig,
                                                   DataTransformationConfig,
                                                   ModelTrainingConfig)


class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
    
    def get_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir= config.root_dir,
            data_files=config.data_files,
            status_file= config.stats_file
        )

        return data_validation_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        create_directories([config.root_dir, config.transformed_train_dir, config.transformed_test_dir])

        return DataTransformationConfig(
            root_dir=Path(config.root_dir),
            transformed_train_dir=Path(config.transformed_train_dir),
            transformed_test_dir=Path(config.transformed_test_dir),
            batch_size=config.batch_size
        )

    

    def get_model_training_config(self) -> ModelTrainingConfig:
        config = self.config.model_training

        create_directories([config.root_dir, config.model_dir])

        model_training_config = ModelTrainingConfig(
            root_dir=Path(config.root_dir),
            model_dir=Path(config.model_dir),
            model_file=Path(config.model_dir) / config.model_file,
            evaluation_file=Path(config.root_dir) / config.evaluation_file,
            epochs=config.epochs,
            batch_size=config.batch_size,
            learning_rate=config.learning_rate,
            transformed_train_dir= config.transformed_train_dir,
            transformed_test_dir= config.transformed_test_dir
        )

        return model_training_config
