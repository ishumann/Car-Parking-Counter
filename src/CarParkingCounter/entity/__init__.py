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
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: list


@dataclass(frozen=True)
class PosFinderConfig:
    image_dir: Path
    pickle_dir: Path
    box_height: int
    box_width: int


@dataclass(frozen=True)
class ParkingCounterConfig:
    root_dir: Path
    pickle_dir: Path
    video_dir: Path
    video_write_dir: Path
    box_height: int
    box_width: int
