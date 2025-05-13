from fastmcp import FastMCP
from typing import Optional
from src.mcp.utils import post, patch, delete

def register_accesstemplate_tools(mcp: FastMCP):
    """Register tools for creating, updating, and deleting access templates."""

    @mcp.tool()
    def create_access_template(name: str, description: str) -> dict:
        """Create a new access template.

        Args:
            name: The name of the access template.
            description: The description of the access template.

        Returns:
            A dictionary with a success message.
        """
        try:
            # Create access template data
            template_data = {
                "name": name,
                "description": description
            }

            # Call the API to create the access template
            response = post("/entities/access-template", template_data)

            if response:
                return {"message": f"Access template created: {name}", "accesstemplate": response}

            # Fallback message if the API call doesn't return data
            return {"message": f"Access template created: {name}"}
        except Exception as e:
            # Log the error and return a fallback message
            print(f"Error creating access template: {e}")
            return {"message": f"Error creating access template: {e}"}

    @mcp.tool()
    def update_access_template(id: str, name: Optional[str] = None, description: Optional[str] = None) -> dict:
        """Update an existing access template.

        Args:
            id: The ID of the access template to update.
            name: The new name of the access template (optional).
            description: The new description of the access template (optional).

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

            # Call the API to update the access template
            response = patch("/entities/access-template", update_data)

            if response:
                return {"message": f"Access template {id} updated", "accesstemplate": response}

            # Fallback message if the API call doesn't return data
            return {"message": f"Access template {id} updated"}
        except Exception as e:
            # Log the error and return a fallback message
            print(f"Error updating access template {id}: {e}")
            return {"message": f"Error updating access template {id}: {e}"}

    @mcp.tool()
    def delete_access_template(id: str) -> dict:
        """Delete an access template.

        Args:
            id: The ID of the access template to delete.

        Returns:
            A dictionary with a success message.
        """
        try:
            # Call the API to delete the access template
            delete(f"/entities/access-template/{id}")

            # Return success message
            return {"message": f"Access template {id} deleted"}
        except Exception as e:
            # Log the error and return a fallback message
            print(f"Error deleting access template {id}: {e}")
            return {"message": f"Error deleting access template {id}: {e}"}
