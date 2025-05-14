from fastmcp import FastMCP
import logging
from src.mcp.utils import get

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def register_permissions_all_resource(mcp: FastMCP):
    """Register the static resource that lists all permissions."""

    @mcp.resource("permissions://all")
    def get_all_permissions():
        """Get a list of all permissions."""
        try:
            # Fetch all permissions from the API
            response = get("/entities/permission")

            # If we got a response, return it
            if response and isinstance(response, list):
                return {"permissions": response}

            # Log error and return None if no response is received
            logger.error("No valid response received for all permissions")
            return None
        except Exception as e:
            # Log the error and return None
            logger.error(f"Error fetching all permissions: {e}")
            return None
