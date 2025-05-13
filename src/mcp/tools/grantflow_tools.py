from fastmcp import FastMCP
from typing import Optional
from src.mcp.utils import post, patch, delete

def register_grantflow_tools(mcp: FastMCP):
    """Register tools for creating, updating, and deleting grant flows."""

    @mcp.tool()
    def create_grant_flow(name: str, description: str) -> dict:
        """Create a new grant flow.

        Args:
            name: The name of the grant flow.
            description: The description of the grant flow.

        Returns:
            A dictionary with a success message.
        """
        try:
            # Create grant flow data
            flow_data = {
                "name": name,
                "flowId": name.lower().replace(" ", "_"),  # Generate a flowId from the name
                "description": description
            }

            # Call the API to create the grant flow
            response = post("/entities/grant-flow", flow_data)

            if response:
                return {"message": f"Grant flow created: {name}", "grantflow": response}

            # Fallback message if the API call doesn't return data
            return {"message": f"Grant flow created: {name}"}
        except Exception as e:
            # Log the error and return a fallback message
            print(f"Error creating grant flow: {e}")
            return {"message": f"Error creating grant flow: {e}"}

    @mcp.tool()
    def update_grant_flow(id: str, name: Optional[str] = None, description: Optional[str] = None) -> dict:
        """Update an existing grant flow.

        Args:
            id: The ID of the grant flow to update.
            name: The new name of the grant flow (optional).
            description: The new description of the grant flow (optional).

        Returns:
            A dictionary with a success message.
        """
        try:
            # Create update data, only including fields that are provided
            update_data = {"id": int(id)}
            if name:
                update_data["name"] = name
                update_data["flowId"] = name.lower().replace(" ", "_")  # Update flowId if name changes
            if description:
                update_data["description"] = description

            # Call the API to update the grant flow
            response = patch("/entities/grant-flow", update_data)

            if response:
                return {"message": f"Grant flow {id} updated", "grantflow": response}

            # Fallback message if the API call doesn't return data
            return {"message": f"Grant flow {id} updated"}
        except Exception as e:
            # Log the error and return a fallback message
            print(f"Error updating grant flow {id}: {e}")
            return {"message": f"Error updating grant flow {id}: {e}"}

    @mcp.tool()
    def delete_grant_flow(id: str) -> dict:
        """Delete a grant flow.

        Args:
            id: The ID of the grant flow to delete.

        Returns:
            A dictionary with a success message.
        """
        try:
            # Call the API to delete the grant flow
            delete(f"/entities/grant-flow/{id}")

            # Return success message
            return {"message": f"Grant flow {id} deleted"}
        except Exception as e:
            # Log the error and return a fallback message
            print(f"Error deleting grant flow {id}: {e}")
            return {"message": f"Error deleting grant flow {id}: {e}"}
