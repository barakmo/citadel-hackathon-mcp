from fastmcp import FastMCP

# Import resource registration functions
from src.mcp.resources.users_all import register_users_all_resource
from src.mcp.resources.user_by_id import register_user_by_id_resource
from src.mcp.resources.applications_all import register_applications_all_resource
from src.mcp.resources.application_by_id import register_application_by_id_resource
from src.mcp.resources.grantflows_all import register_grantflows_all_resource
from src.mcp.resources.grantflow_by_id import register_grantflow_by_id_resource
from src.mcp.resources.permissions_all import register_permissions_all_resource
from src.mcp.resources.permission_by_id import register_permission_by_id_resource
from src.mcp.resources.permissions_by_app import register_permissions_by_app_resource
from src.mcp.resources.accesstemplates_all import register_accesstemplates_all_resource
from src.mcp.resources.accesstemplate_by_id import register_accesstemplate_by_id_resource
from src.mcp.resources.resources_all import register_resources_all_resource
from src.mcp.resources.resource_by_id import register_resource_by_id_resource
from src.mcp.resources.resources_by_app import register_resources_by_app_resource
from src.mcp.resources.user_permissions_by_resource import register_user_permissions_by_resource_resource

# Import tool registration functions
from src.mcp.tools.user_tools import register_user_tools
from src.mcp.tools.application_tools import register_application_tools
from src.mcp.tools.grantflow_tools import register_grantflow_tools
from src.mcp.tools.permission_tools import register_permission_tools
from src.mcp.tools.accesstemplate_tools import register_accesstemplate_tools
from src.mcp.tools.resource_tools import register_resource_tools
from src.mcp.tools.user_permission_tools import register_user_permission_tools

def register_all(mcp: FastMCP):
    """Register all MCP resources and tools."""

    # Register resources
    register_users_all_resource(mcp)
    register_user_by_id_resource(mcp)
    register_applications_all_resource(mcp)
    register_application_by_id_resource(mcp)
    register_grantflows_all_resource(mcp)
    register_grantflow_by_id_resource(mcp)
    register_permissions_all_resource(mcp)
    register_permission_by_id_resource(mcp)
    register_permissions_by_app_resource(mcp)
    register_accesstemplates_all_resource(mcp)
    register_accesstemplate_by_id_resource(mcp)
    register_resources_all_resource(mcp)
    register_resource_by_id_resource(mcp)
    register_resources_by_app_resource(mcp)
    register_user_permissions_by_resource_resource(mcp)

    # Register tools
    register_user_tools(mcp)
    register_application_tools(mcp)
    register_grantflow_tools(mcp)
    register_permission_tools(mcp)
    register_accesstemplate_tools(mcp)
    register_resource_tools(mcp)
    register_user_permission_tools(mcp)
