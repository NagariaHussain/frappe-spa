import json
import argparse
from pathlib import Path
from typing import Dict

# Setup Argument Parser
parser = argparse.ArgumentParser()
parser.add_argument("app", help="App to which the SPA should be added")
parser.add_argument("--add-spa", help="SPA directory/route name", action="store_true")

# Parse the arguments
args = parser.parse_args()

if args.add_spa:
	# spa_name = input("SPA name (directory and route): ")
	# js_framework = input("JS Framwork (vuejs/react): ")
	# css_library = input("CSS Option (tailwind/bootstrap/vuetify): ")
	pass

template_dir = Path('templates')

if not template_dir.exists():
	raise AssertionError("Templates directory missing")

# Recursive structure
with open("directory_schema.json", "r") as f:
	directory_structure = json.load(f)


def generate_directory(dir: Dict, root: Path):
	print(dir, root)

	d_path: Path = root / dir.get("name")

	if not d_path.exists():
		d_path.mkdir()

	# Create nested directories
	if dir.get("dirs"):
		for d in dir.get("dirs"):
			generate_directory(d, d_path)

	# Create files
	if dir.get("files"):
		for f in dir.get("files"):
			f_path: Path = d_path / f.get("name")

			if not f_path.exists():
				f_path.touch()


generate_directory(directory_structure, Path("."))
