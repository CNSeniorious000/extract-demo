from pathlib import Path

from promplate import Template

root = Path(__file__).parent


classify_template = Template.read(root / "classify.j2")
extract_template = Template.read(root / "extract.j2")
