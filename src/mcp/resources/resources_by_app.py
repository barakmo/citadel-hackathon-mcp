from fastmcp import FastMCP
import logging
from src.mcp.utils import get

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def register_resources_by_app_resource(mcp: FastMCP):
    """Register the dynamic resource that gets all resources of an app."""

    @mcp.resource("resources://app/{appId}")
    def get_resources_by_app(appId: str):
        """Get all resources of an app."""
        try:
            # Fetch resources for the app from the API
            response = get(f"/resources/app/{appId}")
            
            # If we got a response, return it
            if response and isinstance(response, list):
                return {"resources": response}
            
            # Log error and return None if no response is received
            logger.error(f"No valid response received for resources of app {appId}")
            return None
        except Exception as e:
            # Log the error and return None
            logger.error(f"Error fetching resources for app {appId}: {e}")
            return None