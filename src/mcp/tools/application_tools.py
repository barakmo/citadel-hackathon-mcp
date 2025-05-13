from fastmcp import FastMCP
from typing import Optional
from src.mcp.utils import post, patch, delete

def register_application_tools(mcp: FastMCP):
    """Register tools for creating, updating, and deleting applications."""

    @mcp.tool()
    def create_application(name: str, description: str) -> dict:
        """Create a new application.

        Args:
            name: The name of the application.
            description: The description of the application.

        Returns:
            A dictionary with a success message.
        """
        try:
            # Create application data
            app_data = {
                "name": name,
                "description": description
            }

            # Call the API to create the application
            response = post("/entities/application", app_data)

            if response:
                return {"message": f"Application created: {name}", "application": response}

            # Fallback message if the API call doesn't return data
            return {"message": f"Application created: {name}"}
        except Exception as e:
            # Log the error and return a fallback message
            print(f"Error creating application: {e}")
            return {"message": f"Error creating application: {e}"}

    @mcp.tool()
    def update_application(id: str, name: Optional[str] = None, description: Optional[str] = None) -> dict:
        """Update an existing application.

        Args:
            id: The ID of the application to update.
            name: The new name of the application (optional).
            description: The new description of the application (optional).

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

            # Call the API to update the application
            response = patch("/entities/application", update_data)

            if response:
                return {"message": f"Application {id} updated", "application": response}

            # Fallback message if the API call doesn't return data
            return {"message": f"Application {id} updated"}
        except Exception as e:
            # Log the error and return a fallback message
            print(f"Error updating application {id}: {e}")
            return {"message": f"Error updating application {id}: {e}"}

    @mcp.tool()
    def delete_application(id: str) -> dict:
        """Delete an application.

        Args:
            id: The ID of the application to delete.

        Returns:
            A dictionary with a success message.
        """
        try:
            # Call the API to delete the application
            delete(f"/entities/application/{id}")

            # Return success message
            return {"message": f"Application {id} deleted"}
        except Exception as e:
            # Log the error and return a fallback message
            print(f"Error deleting application {id}: {e}")
            return {"message": f"Error deleting application {id}: {e}"}
