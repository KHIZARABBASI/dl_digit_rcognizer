from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path  # Root directory for validation artifacts
    data_files: list[Path]  # List of paths to the data files to validate
    status_file: Path  # Path to save the validation status


@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    transformed_train_dir: Path
    transformed_test_dir: Path
    batch_size: int


@dataclass(frozen=True)
class ModelTrainingConfig:
    root_dir: Path
    model_dir: Path
    model_file: Path
    evaluation_file: Path
    epochs: int
    batch_size: int
    learning_rate: float
    transformed_train_dir: Path
    transformed_test_dir: Path