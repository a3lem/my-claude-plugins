#!/usr/bin/env uv run python

import os
from pathlib import Path

INSTRUCTIONS_TEMPLATE = """
<system-reminder>
# claudeMd (continued)
Contents of {claude_plugin_root}/rules/python.md:
{rule_content}
</system-reminder>
""".strip()

claude_plugin_root = Path(os.environ["CLAUDE_PLUGIN_ROOT"])

style_rule_content = (
    claude_plugin_root / "_skills/python-prefs/references/STYLE.md"
).read_text()
tooling_rule_content = (
    claude_plugin_root / "_skills/python-prefs/references/TOOLING.md"
).read_text()

instructions = INSTRUCTIONS_TEMPLATE.format(
    claude_plugin_root=claude_plugin_root,
    rule_content="\n".join([style_rule_content, tooling_rule_content]),
)

print(instructions)
