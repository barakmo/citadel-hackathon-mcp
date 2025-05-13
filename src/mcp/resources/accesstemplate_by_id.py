from fastmcp import FastMCP
import logging
from src.mcp.utils import get

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def register_accesstemplate_by_id_resource(mcp: FastMCP):
    """Register the dynamic resource that gets an access template by ID."""

    @mcp.resource("accesstemplate://{id}")
    def get_accesstemplate_by_id(id: str):
        """Get an access template by ID."""
        try:
            # Fetch access template data from the API
            response = get(f"/entities/access-template/{id}")

            # If we got a response, return it
            if response:
                return {"accesstemplate": response}

            # Log error and return None if no response is received
            logger.error(f"No response received for access template {id}")
            return None
        except Exception as e:
            # Log the error and return None
            logger.error(f"Error fetching access template {id}: {e}")
            return None
