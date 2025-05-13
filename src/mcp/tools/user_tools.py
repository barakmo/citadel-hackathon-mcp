from fastmcp import FastMCP
from typing import Optional
from src.mcp.utils import post, patch, delete

def register_user_tools(mcp: FastMCP):
    """Register tools for creating, updating, and deleting users."""

    @mcp.tool()
    def create_user(name: str, email: str) -> dict:
        """Create a new user.

        Args:
            name: The name of the user.
            email: The email of the user.

        Returns:
            A dictionary with a success message.
        """
        try:
            # Create user data
            user_data = {
                "userId": email.split('@')[0],  # Use part of email as userId
                "name": name,
                "email": email
            }

            # Call the API to create the user
            response = post("/entities/user", user_data)

            if response:
                return {"message": f"User created: {name} ({email})", "user": response}

            # Fallback message if the API call doesn't return data
            return {"message": f"User created: {name} ({email})"}
        except Exception as e:
            # Log the error and return a fallback message
            print(f"Error creating user: {e}")
            return {"message": f"Error creating user: {e}"}

    @mcp.tool()
    def update_user(id: str, name: Optional[str] = None, email: Optional[str] = None) -> dict:
        """Update an existing user.

        Args:
            id: The ID of the user to update.
            name: The new name of the user (optional).
            email: The new email of the user (optional).

        Returns:
            A dictionary with a success message.
        """
        try:
            # Create update data, only including fields that are provided
            update_data = {"userId": id}
            if name:
                update_data["name"] = name
            if email:
                update_data["email"] = email

            # Call the API to update the user
            response = patch("/entities/user", update_data)

            if response:
                return {"message": f"User {id} updated", "user": response}

            # Fallback message if the API call doesn't return data
            return {"message": f"User {id} updated"}
        except Exception as e:
            # Log the error and return a fallback message
            print(f"Error updating user {id}: {e}")
            return {"message": f"Error updating user {id}: {e}"}

    @mcp.tool()
    def delete_user(id: str) -> dict:
        """Delete a user.

        Args:
            id: The ID of the user to delete.

        Returns:
            A dictionary with a success message.
        """
        try:
            # Call the API to delete the user
            delete(f"/entities/user/{id}")

            # Return success message
            return {"message": f"User {id} deleted"}
        except Exception as e:
            # Log the error and return a fallback message
            print(f"Error deleting user {id}: {e}")
            return {"message": f"Error deleting user {id}: {e}"}
