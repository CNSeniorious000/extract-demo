from pathlib import Path

from promplate import Template

root = Path(__file__).parent


prompt_template = Template.read(root / "prompt.j2")
