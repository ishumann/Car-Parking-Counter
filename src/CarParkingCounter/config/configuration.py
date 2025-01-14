from carParkingCounter.constants import *

from carParkingCounter.utils.common import read_yaml, create_directories

from carParkingCounter.entity import (

    DataIngestionConfig,

    DataValidationConfig,

    PosFinderConfig,

    ParkingCounterConfig

)


# PrepareBaseModelConfig, TrainingConfig, EvaluationConfig)

import os 

class ConfigurationManager:

    def __init__(self, config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)

        self.params = read_yaml(params_filepath)

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

    def get_data_validation_config(self) -> DataValidationConfig:

        config = self.config.data_validation

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(

            root_dir=config.root_dir,

            STATUS_FILE=config.STATUS_FILE,

            ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES,

        )

        return data_validation_config

    def get_posfinder_config(self) -> PosFinderConfig:
        config = self.config.posfinder

        create_directories([config.root_dir])

        posfinder_config = PosFinderConfig(

            image_dir=config.image_dir,

            pickle_dir=config.pickle_dir,

            box_width=self.params.box_width,

            box_height=self.params.box_height,

        )

        return posfinder_config

    def get_parking_counter_config(self) -> ParkingCounterConfig:

        config = self.config.parking_counter

        create_directories([config.root_dir])

        parking_counter_config = ParkingCounterConfig(
            root_dir=config.root_dir,
            pickle_dir=config.pickle_dir,
            video_dir=config.video_dir,
            video_write_dir=config.video_write_dir,
            box_width=self.params.box_width,
            box_height=self.params.box_height,
        )

        return parking_counter_config
