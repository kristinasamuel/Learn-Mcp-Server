from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    name= "Employee Management MCP",
    stateless_http= True,
    )

@mcp.tool("calculate_salary")
def calculate_salary(employee_name: str, basic_salary: float, bonus_percent: float) -> dict:
    """
    Calculate total salary including bonus.
    """
    bonus_amount = (basic_salary * bonus_percent) / 100
    total_salary = basic_salary + bonus_amount

    return {
        "employee": employee_name,
        "basic_salary": basic_salary,
        "bonus_percent": bonus_percent,
        "bonus_amount": bonus_amount,
        "total_salary": total_salary
    }
mcp_app = mcp.streamable_http_app()
