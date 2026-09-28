#!/bin/bash
# Enforce Antigravity MCP Constraints

# 1. Ban raw print() statements in the MCP server to prevent JSON-RPC corruption
if grep -q -E "\bprint\s*\(" tutor/mcp_server.py 2>/dev/null; then
    echo "ERROR: raw print() statement detected in tutor/mcp_server.py!"
    echo "Antigravity stdio transport requires strict JSON-RPC. Use ctx.info() instead."
    exit 1
fi

# 2. Ban boolean enums in schemas (primitive check)
if grep -q -E "enum.*(true|false|True|False)" tutor/mcp_server.py 2>/dev/null; then
    echo "ERROR: Boolean enum detected in tool schema!"
    echo "This will trigger INVALID_ARGUMENT gateway errors in Antigravity."
    exit 1
fi

echo "Constraints check passed."
exit 0
