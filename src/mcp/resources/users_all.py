from fastmcp import FastMCP
import logging
from src.mcp.utils import get

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def register_users_all_resource(mcp: FastMCP):
    """Register the static resource that lists all users."""

    @mcp.resource("users://all")
    def get_all_users():
        """Get a list of all users."""
        try:
            # Fetch all users from the API
            response = get("/entities/user")

            # If we got a response, return it
            if response and isinstance(response, list):
                return {"users": response}

            # Log error and return None if no response is received
            logger.error("No valid response received for all users")
            return None
        except Exception as e:
            # Log the error and return None
            logger.error(f"Error fetching all users: {e}")
            return None
