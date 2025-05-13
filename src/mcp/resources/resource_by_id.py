from fastmcp import FastMCP
import logging
from src.mcp.utils import get

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def register_resource_by_id_resource(mcp: FastMCP):
    """Register the dynamic resource that gets a resource by ID."""

    @mcp.resource("resource://{id}")
    def get_resource_by_id(id: str):
        """Get a resource by ID."""
        try:
            # Fetch resource data from the API
            response = get(f"/resources/{id}")

            # If we got a response, return it
            if response:
                return {"resource": response}

            # Log error and return None if no response is received
            logger.error(f"No response received for resource {id}")
            return None
        except Exception as e:
            # Log the error and return None
            logger.error(f"Error fetching resource {id}: {e}")
            return None
