from fastmcp import FastMCP
import logging
from src.mcp.utils import get

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def register_grantflow_by_id_resource(mcp: FastMCP):
    """Register the dynamic resource that gets a grant flow by ID."""

    @mcp.resource("grantflow://{id}")
    def get_grantflow_by_id(id: str):
        """Get a grant flow by ID."""
        try:
            # Fetch grant flow data from the API
            response = get(f"/entities/grant-flow/{id}")

            # If we got a response, return it
            if response:
                return {"grantflow": response}

            # Log error and return None if no response is received
            logger.error(f"No response received for grant flow {id}")
            return None
        except Exception as e:
            # Log the error and return None
            logger.error(f"Error fetching grant flow {id}: {e}")
            return None
