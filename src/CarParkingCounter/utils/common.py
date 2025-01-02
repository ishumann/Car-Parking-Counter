import os

from box.exceptions import BoxValueError

import yaml  # to read yaml file
from carParkingCounter import logger  # our custom logger fuction

import json  # to read json file

# import joblib
from ensure import ensure_annotations

from box import ConfigBox

from pathlib import Path

# from typing import Any

import base64

import pickle


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns


    Args:

        path_to_yaml (str): path like input


    Raises:

        ValueError: if yaml file is empty

        e: empty file


    Returns:

        ConfigBox: ConfigBox type
    """

    try:

        with open(path_to_yaml) as yaml_file:

            content = yaml.safe_load(yaml_file)

            logger.info(f"yaml file: {path_to_yaml} loaded successfully")

            return ConfigBox(content)

    except BoxValueError:

        raise ValueError("yaml file is empty")

    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories


    Args:
        path_to_directories (list): list of path of directories

        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:

        os.makedirs(path, exist_ok=True)

        if verbose:

            logger.info(f"created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data"""

    with open(path, "w") as f:

        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data


    Args:

        path (Path): path to json file


    Returns:

        ConfigBox: data as class attributes instead of dict
    """

    try:

        with open(path) as f:

            content = json.load(f)

        logger.info(f"json file loaded successfully from: {path}")

        return ConfigBox(content)

    except BoxValueError:

        raise ValueError("json file is empty")

    except Exception as e:
        raise e


@ensure_annotations
def load_pickle(path: Path):
    """load pickle files data


    Args:

        path (Path): path to pickle file


    Returns:

        ConfigBox: data as class attributes instead of dict
    """

    try:

        with open(path, "rb") as f:

            content = pickle.load(f)

            return content

    except BoxValueError:

        raise ValueError("loading pickle file has failed")

    except Exception as e:
        raise e


@ensure_annotations
def save_pickle(path: Path, data):
    """save pickle data

    Args:

        path (Path): path to pickle file


    Returns:

        ConfigBox: data as class attributes instead of dict
    """

    with open(path, "wb") as f:

        pickle.dump(data, f)


@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"


# @ensure_annotations

# def save_Video(path: Path, cap ):

#     """save pickle data"""

#     with open(path, "wb") as f:

#         pickle.dump(posList, f)
