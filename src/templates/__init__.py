from pathlib import Path

from promplate import Template

root = Path(__file__).parent  # noqa: RUF067


classify_template = Template.read(root / "classify.j2")  # noqa: RUF067
extract_template = Template.read(root / "extract.j2")  # noqa: RUF067
