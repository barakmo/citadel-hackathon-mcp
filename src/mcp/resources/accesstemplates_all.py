from fastmcp import FastMCP
import logging
from src.mcp.utils import get

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def register_accesstemplates_all_resource(mcp: FastMCP):
    """Register the static resource that lists all access templates."""

    @mcp.resource("accesstemplates://all")
    def get_all_accesstemplates():
        """Get a list of all access templates."""
        # Note: The API doesn't have a specific endpoint to get all access templates
        logger.error("Endpoint to get all access templates is not implemented")
        return None
