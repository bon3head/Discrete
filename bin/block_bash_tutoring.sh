#!/bin/bash
# PreToolUse hook: blocks direct tutor CLI bypass attempts.
# Receives tool call context as JSON on stdin.
# If CommandLine contains tutor/cli.py or -m tutor.cli, deny.
# Otherwise allow.
input=$(cat)
cmdline=$(echo "$input" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('toolCall',{}).get('args',{}).get('CommandLine',''))" 2>/dev/null || echo "")
if echo "$cmdline" | grep -qE '(tutor/cli\.py|-m tutor\.cli)'; then
  echo '{"decision": "deny", "reason": "Direct tutor CLI bypass is forbidden. Use the ads-tutor MCP server endpoint instead."}'
  exit 0
fi
echo '{"decision": "allow"}'
exit 0
