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
        try:
            # Fetch all access templates from the API
            response = get("/entities/access-template")

            # If we got a response, return it
            if response and isinstance(response, list):
                return {"accesstemplates": response}

            # Log error and return None if no response is received
            logger.error("No valid response received for all access templates")
            return None
        except Exception as e:
            # Log the error and return None
            logger.error(f"Error fetching all access templates: {e}")
            return None
