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
        # Note: The API doesn't have a specific endpoint to get all permissions
        logger.error("Endpoint to get all permissions is not implemented")
        return None
