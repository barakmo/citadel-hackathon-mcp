from fastmcp import FastMCP
import logging
from src.mcp.utils import get

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def register_grantflows_all_resource(mcp: FastMCP):
    """Register the static resource that lists all grant flows."""

    @mcp.resource("grantflows://all")
    def get_all_grantflows():
        """Get a list of all grant flows."""
        try:
            # Fetch all grant flows from the API
            response = get("/entities/grant-flow")

            # If we got a response, return it
            if response and isinstance(response, list):
                return {"grantflows": response}

            # Log error and return None if no response is received
            logger.error("No valid response received for all grant flows")
            return None
        except Exception as e:
            # Log the error and return None
            logger.error(f"Error fetching all grant flows: {e}")
            return None
