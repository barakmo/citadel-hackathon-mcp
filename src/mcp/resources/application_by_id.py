from fastmcp import FastMCP
import logging
from src.mcp.utils import get

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def register_application_by_id_resource(mcp: FastMCP):
    """Register the dynamic resource that gets an application by ID."""

    @mcp.resource("application://{id}")
    def get_application_by_id(id: str):
        """Get an application by ID."""
        try:
            # Fetch application data from the API
            response = get(f"/entities/application/{id}")

            # If we got a response, return it
            if response:
                return {"application": response}

            # Log error and return None if no response is received
            logger.error(f"No response received for application {id}")
            return None
        except Exception as e:
            # Log the error and return None
            logger.error(f"Error fetching application {id}: {e}")
            return None
