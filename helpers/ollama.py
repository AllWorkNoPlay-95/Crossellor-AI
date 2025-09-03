import sys

import requests


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
            print(f"Downloading model {model_name}...")
            download = requests.post(f"{ollama_url}/api/pull", json={"name": model_name})

            if download.status_code != 200:
                print(f"Failed to download model {model_name}", file=sys.stderr)
                return False

            print(f"Model {model_name} downloaded successfully")

        elif response.status_code != 200:
            print(f"Failed to check model {model_name}", file=sys.stderr)
            return False

        return True

    except requests.exceptions.RequestException as e:
        print(f"Error connecting to Ollama server: {e}", file=sys.stderr)
        exit(1)
