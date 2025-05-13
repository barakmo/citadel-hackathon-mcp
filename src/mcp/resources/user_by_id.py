from fastmcp import FastMCP
import logging
from src.mcp.utils import get

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def register_user_by_id_resource(mcp: FastMCP):
    """Register the dynamic resource that gets a user by ID."""

    @mcp.resource("user://{id}")
    def get_user_by_id(id: str):
        """Get a user by ID."""
        try:
            # Fetch user data from the API
            response = get(f"/entities/user/{id}")

            # If we got a response, return it
            if response:
                return {"user": response}

            # Log error and return None if no response is received
            logger.error(f"No response received for user {id}")
            return None
        except Exception as e:
            # Log the error and return None
            logger.error(f"Error fetching user {id}: {e}")
            return None
