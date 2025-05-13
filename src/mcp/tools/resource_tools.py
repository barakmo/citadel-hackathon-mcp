from fastmcp import FastMCP
from typing import Optional
from src.mcp.utils import post, patch, delete

def register_resource_tools(mcp: FastMCP):
    """Register tools for creating, updating, and deleting resources."""

    @mcp.tool()
    def create_resource(name: str, description: str, app_id: str = "1") -> dict:
        """Create a new resource.

        Args:
            name: The name of the resource.
            description: The description of the resource.
            app_id: The ID of the application (default: "1").

        Returns:
            A dictionary with a success message.
        """
        try:
            # Create resource data
            resource_data = {
                "name": name,
                "description": description,
                "appId": int(app_id)
            }

            # Call the API to create the resource
            response = post("/resources", resource_data)

            if response:
                return {"message": f"Resource created: {name}", "resource": response}

            # Fallback message if the API call doesn't return data
            return {"message": f"Resource created: {name}"}
        except Exception as e:
            # Log the error and return a fallback message
            print(f"Error creating resource: {e}")
            return {"message": f"Error creating resource: {e}"}

    @mcp.tool()
    def update_resource(id: str, name: Optional[str] = None, description: Optional[str] = None, app_id: Optional[str] = None) -> dict:
        """Update an existing resource.

        Args:
            id: The ID of the resource to update.
            name: The new name of the resource (optional).
            description: The new description of the resource (optional).
            app_id: The new application ID (optional).

        Returns:
            A dictionary with a success message.
        """
        try:
            # Create update data, only including fields that are provided
            update_data = {"id": int(id)}
            if name:
                update_data["name"] = name
            if description:
                update_data["description"] = description
            if app_id:
                update_data["appId"] = int(app_id)

            # Call the API to update the resource
            response = patch("/resources", update_data)

            if response:
                return {"message": f"Resource {id} updated", "resource": response}

            # Fallback message if the API call doesn't return data
            return {"message": f"Resource {id} updated"}
        except Exception as e:
            # Log the error and return a fallback message
            print(f"Error updating resource {id}: {e}")
            return {"message": f"Error updating resource {id}: {e}"}

    @mcp.tool()
    def delete_resource(id: str) -> dict:
        """Delete a resource.

        Args:
            id: The ID of the resource to delete.

        Returns:
            A dictionary with a success message.
        """
        try:
            # Call the API to delete the resource
            delete(f"/resources/{id}")

            # Return success message
            return {"message": f"Resource {id} deleted"}
        except Exception as e:
            # Log the error and return a fallback message
            print(f"Error deleting resource {id}: {e}")
            return {"message": f"Error deleting resource {id}: {e}"}
