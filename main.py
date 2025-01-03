from carParkingCounter.pipeline.data_ingestion_stage import (
    DataIngestionTrainingPipeline,
)
from carParkingCounter.pipeline.data_validation_stage import (
    DataValidationTrainingPipeline, 
)
from carParkingCounter.pipeline.posfinder import (
    PosFinderPipeline
)
from carParkingCounter.pipeline.parking_counter import (
    ParkingCounterPipeline
)

from carParkingCounter import logger

STAGE_NAME = "Date Ingestion"


try:
    logger.info(f">>>>>>>>> Stage {STAGE_NAME} started <<<<<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>> Stage {STAGE_NAME} completed <<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Date Validation"

try:
    logger.info(f">>>>>>>>> Stage {STAGE_NAME} started <<<<<<<<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>>>>> Stage {STAGE_NAME} completed <<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "PosFinder"

try:
    logger.info(f">>>>>>>>> Stage {STAGE_NAME} started <<<<<<<<<<<<")
    posfinder = PosFinderPipeline()
    posfinder.main()
    logger.info(f">>>>>>>>> Stage {STAGE_NAME} completed <<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Parking Counter Stage"

try:
    logger.info(f">>>>>>>>> Stage {STAGE_NAME} started <<<<<<<<<<<<")
    parking_counter = ParkingCounterPipeline()
    parking_counter.main()
    logger.info(f">>>>>>>>> Stage {STAGE_NAME} completed <<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e
