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


