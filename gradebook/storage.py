import json
import os
from .logger import get_logger

logger = get_logger(__name__)

DEFAULT_PATH = "data/gradebook.json"


def load_data(path=DEFAULT_PATH):
    """
    Load data from JSON file.

    Returns:
        dict: Loaded data or empty dict on failure.
    """
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
            logger.info("Data loaded")
            return data

    except FileNotFoundError:
        logger.info("No data file found, starting empty")
        return {}

    except json.JSONDecodeError:
        logger.error("Invalid JSON format")
        print("[ERROR] Invalid JSON file")
        return {}

    except Exception as error:
        logger.error(f"Load error: {error}")
        return {}


def save_data(data, path=DEFAULT_PATH):
    """
    Save data to JSON file.
    """
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)

        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        logger.info("Data saved")

    except Exception as error:
        logger.error(f"Save error: {error}")