from fastmcp import FastMCP
import logging
from src.mcp.utils import get

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def register_permission_by_id_resource(mcp: FastMCP):
    """Register the dynamic resource that gets a permission by ID."""

    @mcp.resource("permission://{id}")
    def get_permission_by_id(id: str):
        """Get a permission by ID."""
        try:
            # Fetch permission data from the API
            response = get(f"/entities/permission/{id}")

            # If we got a response, return it
            if response:
                return {"permission": response}

            # Log error and return None if no response is received
            logger.error(f"No response received for permission {id}")
            return None
        except Exception as e:
            # Log the error and return None
            logger.error(f"Error fetching permission {id}: {e}")
            return None
