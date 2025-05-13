from fastmcp import FastMCP
import logging
from src.mcp.utils import post, delete, get

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def register_user_permission_tools(mcp: FastMCP):
    """Register tools for managing user permissions."""

    @mcp.tool()
    def add_permission_to_user(userId: str, permissionId: str, appId: str = "1") -> dict:
        """Add a permission to a user.

        Args:
            userId: The ID of the user.
            permissionId: The ID of the permission.
            appId: The ID of the application (default: "1").

        Returns:
            A dictionary with a success message.
        """
        try:
            # Call the API to add a permission to a user
            response = post(f"/user-permissions/user/{userId}/permission/{permissionId}/app/{appId}", {})

            if response:
                return {"message": f"Permission {permissionId} added to user {userId}"}

            # Log error and return None if no response is received
            logger.error(f"No response received when adding permission {permissionId} to user {userId}")
            return None
        except Exception as e:
            # Log the error and return None
            logger.error(f"Error adding permission {permissionId} to user {userId}: {e}")
            return None

    @mcp.tool()
    def remove_permission_from_user(userId: str, permissionId: str, appId: str = "1") -> dict:
        """Remove a permission from a user.

        Args:
            userId: The ID of the user.
            permissionId: The ID of the permission.
            appId: The ID of the application (default: "1").

        Returns:
            A dictionary with a success message.
        """
        try:
            # Call the API to remove a permission from a user
            response = delete(f"/user-permissions/user/{userId}/permission/{permissionId}/app/{appId}")

            if response is not None:
                return {"message": f"Permission {permissionId} removed from user {userId}"}

            # Log error and return None if no response is received
            logger.error(f"No response received when removing permission {permissionId} from user {userId}")
            return None
        except Exception as e:
            # Log the error and return None
            logger.error(f"Error removing permission {permissionId} from user {userId}: {e}")
            return None

    @mcp.tool()
    def add_permission_to_resource(resourceId: str, permissionId: str) -> dict:
        """Add a permission to a resource.

        Args:
            resourceId: The ID of the resource.
            permissionId: The ID of the permission.

        Returns:
            A dictionary with a success message.
        """
        # This endpoint is not implemented in the API
        logger.error(f"Endpoint to add permission to resource is not implemented")
        return None

    @mcp.tool()
    def remove_permission_from_resource(resourceId: str, permissionId: str) -> dict:
        """Remove a permission from a resource.

        Args:
            resourceId: The ID of the resource.
            permissionId: The ID of the permission.

        Returns:
            A dictionary with a success message.
        """
        # This endpoint is not implemented in the API
        logger.error(f"Endpoint to remove permission from resource is not implemented")
        return None

    @mcp.tool()
    def add_permission_to_access_template(templateId: str, permissionId: str, appId: str = "1") -> dict:
        """Add a permission to an access template.

        Args:
            templateId: The ID of the access template.
            permissionId: The ID of the permission.
            appId: The ID of the application (default: "1").

        Returns:
            A dictionary with a success message.
        """
        try:
            # Call the API to add a permission to an access template
            response = post(f"/user-permissions/template/{templateId}/permission/{permissionId}/app/{appId}", {})

            if response:
                return {"message": f"Permission {permissionId} added to access template {templateId}"}

            # Log error and return None if no response is received
            logger.error(f"No response received when adding permission {permissionId} to access template {templateId}")
            return None
        except Exception as e:
            # Log the error and return None
            logger.error(f"Error adding permission {permissionId} to access template {templateId}: {e}")
            return None

    @mcp.tool()
    def remove_permission_from_access_template(templateId: str, permissionId: str, appId: str = "1") -> dict:
        """Remove a permission from an access template.

        Args:
            templateId: The ID of the access template.
            permissionId: The ID of the permission.
            appId: The ID of the application (default: "1").

        Returns:
            A dictionary with a success message.
        """
        try:
            # Call the API to remove a permission from an access template
            response = delete(f"/user-permissions/template/{templateId}/permission/{permissionId}/app/{appId}")

            if response is not None:
                return {"message": f"Permission {permissionId} removed from access template {templateId}"}

            # Log error and return None if no response is received
            logger.error(f"No response received when removing permission {permissionId} from access template {templateId}")
            return None
        except Exception as e:
            # Log the error and return None
            logger.error(f"Error removing permission {permissionId} from access template {templateId}: {e}")
            return None

    @mcp.tool()
    def add_access_template_to_user(userId: str, templateId: str) -> dict:
        """Add an access template to a user.

        Args:
            userId: The ID of the user.
            templateId: The ID of the access template.

        Returns:
            A dictionary with a success message.
        """
        try:
            # Call the API to add an access template to a user
            response = post(f"/user-permissions/user/{userId}/template/{templateId}", {})

            if response:
                return {"message": f"Access template {templateId} added to user {userId}"}

            # Log error and return None if no response is received
            logger.error(f"No response received when adding access template {templateId} to user {userId}")
            return None
        except Exception as e:
            # Log the error and return None
            logger.error(f"Error adding access template {templateId} to user {userId}: {e}")
            return None

    @mcp.tool()
    def remove_access_template_from_user(userId: str, templateId: str) -> dict:
        """Remove an access template from a user.

        Args:
            userId: The ID of the user.
            templateId: The ID of the access template.

        Returns:
            A dictionary with a success message.
        """
        try:
            # Call the API to remove an access template from a user
            response = delete(f"/user-permissions/user/{userId}/template/{templateId}")

            if response is not None:
                return {"message": f"Access template {templateId} removed from user {userId}"}

            # Log error and return None if no response is received
            logger.error(f"No response received when removing access template {templateId} from user {userId}")
            return None
        except Exception as e:
            # Log the error and return None
            logger.error(f"Error removing access template {templateId} from user {userId}: {e}")
            return None

    @mcp.tool()
    def assign_grant_flow_to_permission(permissionId: str, grantFlowId: str, appId: str = "1") -> dict:
        """Assign a grant flow to a permission.

        Args:
            permissionId: The ID of the permission.
            grantFlowId: The ID of the grant flow.
            appId: The ID of the application (default: "1").

        Returns:
            A dictionary with a success message.
        """
        try:
            # Call the API to assign a grant flow to a permission
            response = post(f"/user-permissions/permission/{permissionId}/grant-flow/{grantFlowId}/app/{appId}", {})

            if response:
                return {"message": f"Grant flow {grantFlowId} assigned to permission {permissionId}"}

            # Log error and return None if no response is received
            logger.error(f"No response received when assigning grant flow {grantFlowId} to permission {permissionId}")
            return None
        except Exception as e:
            # Log the error and return None
            logger.error(f"Error assigning grant flow {grantFlowId} to permission {permissionId}: {e}")
            return None

    @mcp.tool()
    def check_user_permission(userId: str, permissionId: str, applicationId: str) -> dict:
        """Check if a user has a permission in an application.

        Args:
            userId: The ID of the user.
            permissionId: The ID of the permission.
            applicationId: The ID of the application.

        Returns:
            A dictionary with the result of the check.
        """
        try:
            # Call the API to check if a user has a permission
            response = get(f"/user-permissions/user/{userId}/has-permission/{permissionId}/app/{applicationId}")

            if response is not None:
                has_permission = bool(response)
                return {
                    "message": f"User {userId} {'has' if has_permission else 'does not have'} permission {permissionId} in application {applicationId}"
                }

            # Log error and return None if no response is received
            logger.error(f"No response received when checking if user {userId} has permission {permissionId}")
            return None
        except Exception as e:
            # Log the error and return None
            logger.error(f"Error checking if user {userId} has permission {permissionId}: {e}")
            return None
