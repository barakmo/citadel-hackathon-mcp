from fastmcp import FastMCP
from typing import Optional
from src.mcp.utils import post, patch, delete

def register_permission_tools(mcp: FastMCP):
    """Register tools for creating, updating, and deleting permissions."""

    @mcp.tool()
    def create_permission(name: str, description: str, app_id: str = "1", resource_id: str = "1", grant_flow_id: str = "1") -> dict:
        """Create a new permission.

        Args:
            name: The name of the permission.
            description: The description of the permission.
            app_id: The ID of the application (default: "1").
            resource_id: The ID of the resource (default: "1").
            grant_flow_id: The ID of the grant flow (default: "1").

        Returns:
            A dictionary with a success message.
        """
        try:
            # Create permission data
            permission_data = {
                "name": name,
                "technicalId": name.lower().replace(" ", "_"),  # Generate a technicalId from the name
                "description": description,
                "appId": int(app_id),
                "resourceId": int(resource_id),
                "grantFlowId": int(grant_flow_id)
            }

            # Call the API to create the permission
            response = post("/entities/permission", permission_data)

            if response:
                return {"message": f"Permission created: {name}", "permission": response}

            # Fallback message if the API call doesn't return data
            return {"message": f"Permission created: {name}"}
        except Exception as e:
            # Log the error and return a fallback message
            print(f"Error creating permission: {e}")
            return {"message": f"Error creating permission: {e}"}

    @mcp.tool()
    def update_permission(id: str, name: Optional[str] = None, description: Optional[str] = None, 
                         app_id: Optional[str] = None, resource_id: Optional[str] = None, 
                         grant_flow_id: Optional[str] = None) -> dict:
        """Update an existing permission.

        Args:
            id: The ID of the permission to update.
            name: The new name of the permission (optional).
            description: The new description of the permission (optional).
            app_id: The new application ID (optional).
            resource_id: The new resource ID (optional).
            grant_flow_id: The new grant flow ID (optional).

        Returns:
            A dictionary with a success message.
        """
        try:
            # Create update data, only including fields that are provided
            update_data = {"id": int(id)}
            if name:
                update_data["name"] = name
                update_data["technicalId"] = name.lower().replace(" ", "_")  # Update technicalId if name changes
            if description:
                update_data["description"] = description
            if app_id:
                update_data["appId"] = int(app_id)
            if resource_id:
                update_data["resourceId"] = int(resource_id)
            if grant_flow_id:
                update_data["grantFlowId"] = int(grant_flow_id)

            # Call the API to update the permission
            response = patch("/entities/permission", update_data)

            if response:
                return {"message": f"Permission {id} updated", "permission": response}

            # Fallback message if the API call doesn't return data
            return {"message": f"Permission {id} updated"}
        except Exception as e:
            # Log the error and return a fallback message
            print(f"Error updating permission {id}: {e}")
            return {"message": f"Error updating permission {id}: {e}"}

    @mcp.tool()
    def delete_permission(id: str) -> dict:
        """Delete a permission.

        Args:
            id: The ID of the permission to delete.

        Returns:
            A dictionary with a success message.
        """
        try:
            # Call the API to delete the permission
            delete(f"/entities/permission/{id}")

            # Return success message
            return {"message": f"Permission {id} deleted"}
        except Exception as e:
            # Log the error and return a fallback message
            print(f"Error deleting permission {id}: {e}")
            return {"message": f"Error deleting permission {id}: {e}"}
