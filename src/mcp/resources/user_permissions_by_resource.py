from fastmcp import FastMCP
import logging
from src.mcp.utils import get

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def register_user_permissions_by_resource_resource(mcp: FastMCP):
    """Register the dynamic resource that gets all permissions of a user grouped by resource."""

    @mcp.resource("userpermissions://{userId}")
    def get_user_permissions_by_resource(userId: str):
        """Get all permissions of a user grouped by resource."""
        try:
            # Fetch user permissions grouped by resource from the API
            response = get(f"/user-permissions/user/{userId}/permissions-by-resource")

            # If we got a response, return it
            if response and isinstance(response, list):
                return {"permissions": response}

            # Log error and return None if no response is received
            logger.error(f"No valid response received for user permissions by resource for user {userId}")
            return None

        except Exception as e:
            # Log the error and return None
            logger.error(f"Error fetching permissions for user {userId}: {e}")
            return None
