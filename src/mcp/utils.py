import requests
import logging
from typing import Dict, Any, Optional

# Base URL for the Citadel API
BASE_URL = "http://localhost:3001"

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get(endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Make a GET request to the Citadel API.
    
    Args:
        endpoint: The API endpoint to call (without the base URL).
        params: Optional query parameters.
        
    Returns:
        The JSON response from the API.
    """
    url = f"{BASE_URL}{endpoint}"
    logger.info(f"Making GET request to {url}")
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for 4XX/5XX responses
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error making GET request to {url}: {e}")
        # Return an empty dict or raise the exception depending on your error handling strategy
        return {}

def post(endpoint: str, data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Make a POST request to the Citadel API.
    
    Args:
        endpoint: The API endpoint to call (without the base URL).
        data: The data to send in the request body.
        
    Returns:
        The JSON response from the API.
    """
    url = f"{BASE_URL}{endpoint}"
    logger.info(f"Making POST request to {url}")
    
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Raise an exception for 4XX/5XX responses
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error making POST request to {url}: {e}")
        # Return an empty dict or raise the exception depending on your error handling strategy
        return {}

def patch(endpoint: str, data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Make a PATCH request to the Citadel API.
    
    Args:
        endpoint: The API endpoint to call (without the base URL).
        data: The data to send in the request body.
        
    Returns:
        The JSON response from the API.
    """
    url = f"{BASE_URL}{endpoint}"
    logger.info(f"Making PATCH request to {url}")
    
    try:
        response = requests.patch(url, json=data)
        response.raise_for_status()  # Raise an exception for 4XX/5XX responses
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error making PATCH request to {url}: {e}")
        # Return an empty dict or raise the exception depending on your error handling strategy
        return {}

def delete(endpoint: str) -> Dict[str, Any]:
    """
    Make a DELETE request to the Citadel API.
    
    Args:
        endpoint: The API endpoint to call (without the base URL).
        
    Returns:
        The JSON response from the API.
    """
    url = f"{BASE_URL}{endpoint}"
    logger.info(f"Making DELETE request to {url}")
    
    try:
        response = requests.delete(url)
        response.raise_for_status()  # Raise an exception for 4XX/5XX responses
        # DELETE requests might not return JSON, so handle that case
        if response.text:
            return response.json()
        return {}
    except requests.exceptions.RequestException as e:
        logger.error(f"Error making DELETE request to {url}: {e}")
        # Return an empty dict or raise the exception depending on your error handling strategy
        return {}