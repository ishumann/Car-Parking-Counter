from carParkingCounter.pipeline.data_ingestion_stage import (
    DataIngestionTrainingPipeline,
)
# from carParkingCounter.pipeline.stage_02_data_validation import (
#     DataValidationTrainingPipeline,
# )
# from carParkingCounter.pipeline.stage_03_data_transformation import (
#     DataTransformationTrainingPipeline,
# )
# from carParkingCounter.pipeline.stage_04_model_pipeline import ModelTrainingPipeline
# from carParkingCounter.pipeline.stage_05_model_evaluation_pipeline import (
#     ModelEvaluationPipeline,
# )
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
