from fastmcp import FastMCP
import logging
from src.mcp.utils import get

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def register_applications_all_resource(mcp: FastMCP):
    """Register the static resource that lists all applications."""

    @mcp.resource("applications://all")
    def get_all_applications():
        """Get a list of all applications."""
        try:
            # Fetch all applications from the API
            response = get("/entities/application")

            # If we got a response, return it
            if response and isinstance(response, list):
                return {"applications": response}

            # Log error and return None if no response is received
            logger.error("No valid response received for all applications")
            return None
        except Exception as e:
            # Log the error and return None
            logger.error(f"Error fetching all applications: {e}")
            return None
