from fastmcp import FastMCP
import logging
from src.mcp.utils import get

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def register_resources_all_resource(mcp: FastMCP):
    """Register the static resource that lists all resources."""

    @mcp.resource("resources://all")
    def get_all_resources():
        """Get a list of all resources."""
        try:
            # Fetch all resources from the API
            response = get("/resources")

            # If we got a response, return it
            if response and isinstance(response, list):
                return {"resources": response}

            # Log error and return None if no response is received
            logger.error("No valid response received for all resources")
            return None
        except Exception as e:
            # Log the error and return None
            logger.error(f"Error fetching all resources: {e}")
            return None
