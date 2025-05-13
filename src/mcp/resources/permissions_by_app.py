from fastmcp import FastMCP
import logging
from src.mcp.utils import get

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def register_permissions_by_app_resource(mcp: FastMCP):
    """Register the dynamic resource that gets all permissions of an app."""

    @mcp.resource("permissions://app/{appId}")
    def get_permissions_by_app(appId: str):
        """Get all permissions of an app."""
        try:
            # Fetch permissions for the app from the API
            response = get(f"/entities/permission/app/{appId}")
            
            # If we got a response, return it
            if response and isinstance(response, list):
                return {"permissions": response}
            
            # Log error and return None if no response is received
            logger.error(f"No valid response received for permissions of app {appId}")
            return None
        except Exception as e:
            # Log the error and return None
            logger.error(f"Error fetching permissions for app {appId}: {e}")
            return None