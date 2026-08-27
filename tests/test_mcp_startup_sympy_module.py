import subprocess
import os

def test_mcp_startup_sympy_module():
    """
    Regression test to ensure the MCP server starts correctly and does not
    throw a ModuleNotFoundError for 'sympy' due to using the wrong python executable.
    """
    env = os.environ.copy()
    
    # Run the MCP server startup script and pass EOF
    process = subprocess.Popen(
        ['./bin/run_mcp.sh'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        env=env
    )
    
    stdout, stderr = process.communicate(input="")
    
    # The server should exit cleanly on EOF (return code 0)
    assert process.returncode == 0, f"MCP server script failed. stderr: {stderr}"
    
    # Check that it didn't fail with the specific ModuleNotFoundError
    assert "ModuleNotFoundError: No module named 'sympy'" not in stderr
