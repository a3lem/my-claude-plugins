---
description: Enable spoken notifications when Claude needs your input
---

# Talk to Me

The user wants to enable spoken TTS notifications so Claude can alert them audibly when input is needed.

## Instructions

1. Use the `enable_talk_to_me` MCP tool to enable the feature
2. Confirm to the user that spoken notifications are now enabled
3. Explain that you will speak to them (via TTS) when you need their input to continue

If the MCP server is not running, inform the user they need to start it first:

```bash
cd <plugin-directory> && uv run talk-to-me-server
```

The server runs on `http://127.0.0.1:8347` by default.
