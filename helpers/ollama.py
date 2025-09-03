import sys

import requests

from helpers.cli import print_info
from helpers.cli import print_ok, print_err


def assert_model(ollama_url: str, model_name: str) -> bool:
    """
    Check if model is downloaded, download if not available
    Args:
        ollama_url (str): Ollama server URL
        model_name (str): Name of the model to check
    Returns:
        bool: True if model is available/downloaded, False if failed
    """
    try:
        # Check if model exists
        response = requests.post(f"{ollama_url}/api/show", json={"name": model_name})

        if response.status_code == 404:
            # Model not found, initiate download
            print_info(f"Downloading model {model_name}...")
            download = requests.post(f"{ollama_url}/api/pull", json={"name": model_name})

            if download.status_code != 200:
                print_err(f"Failed to download model {model_name}")
                return False

            print_ok(f"Model {model_name} downloaded successfully")

        elif response.status_code != 200:
            print_err(f"Failed to check model {model_name}")
            return False
        print_ok(f"{model_name} is available on this machine")
        return True

    except requests.exceptions.RequestException as e:
        print_err(f"Error connecting to Ollama server: {e}")
        sys.exit(1)
