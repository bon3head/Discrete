# Antigravity MCP Integration Sync Report

## Overview
Based on the live Antigravity documentation and MCP integration constraints, we need to adjust our Context7 plugin architecture to ensure stable communication with the Antigravity IDE.

## Key Findings & Constraints
1. **STDIO Transport Stability:** Antigravity relies heavily on strict JSON-RPC communication over `stdio`. A common failure mode ("Improper Format Stop Reason") occurs when an MCP server outputs unexpected data (e.g., debug logs) to `stdout` or `stderr`, which the IDE misinterprets as part of the MCP protocol.
2. **Parallel Execution Limits:** There are known stability issues when performing parallel tool calls alongside native system tools. This can also result in "Improper Format" errors.
3. **Total Tool Limit:** Antigravity enforces a hard limit of approximately 100 tools across all active MCP servers.
4. **Schema Validation:** Using boolean types in `enum` fields within tool JSON schemas can cause `INVALID_ARGUMENT` errors with certain LLM gateways. 

## Architectural Adjustments for Context7
Our current architecture uses `await ctx.info()` to stream IDE logs, returns `CallToolResult` with `is_error=True`, and outputs `TextContent` (including Mermaid graphs). Based on the constraints, we must apply the following adjustments:

* **Log Streaming (CRITICAL):** Using `await ctx.info()` to stream IDE logs must be handled carefully. We must guarantee that these logs do not leak into raw `stdout` or `stderr`. If `ctx.info()` writes to stdout, it will corrupt the JSON-RPC stream and break Antigravity's protocol parser. We should ensure `ctx.info()` routes exclusively through proper JSON-RPC notification messages (like `notifications/message`). Standard `print()` statements must be absolutely banned in the server code.
* **Tool Parallelism:** We should restrict or serialize parallel tool executions in our plugin to avoid triggering Antigravity's concurrency instability.
* **Schema Definitions:** We must audit our tool schemas to ensure we do not use boolean values inside `enum` fields. 
* **Payload Size / Tool Count:** Ensure our plugin does not bloat the Antigravity tool registry (keep well under the 100 total tool limit) and that `TextContent` blocks containing large Mermaid graphs are properly escaped and returned strictly within the `CallToolResult` JSON payload.
