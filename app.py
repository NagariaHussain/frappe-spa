import json
import argparse

from pathlib import Path
from typing import Dict
from jinja2 import Environment, FileSystemLoader, select_autoescape

jenv = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())

# Setup Argument Parser
parser = argparse.ArgumentParser()
parser.add_argument("app", help="App to which the SPA should be added")
parser.add_argument("--add-spa", help="SPA directory/route name", action="store_true")

# Parse the arguments
args = parser.parse_args()

app = args.app

template_files = ["package.json", "vite.config.js", "index.js"]

if args.add_spa:
	spa_name = input("SPA name (directory and route): ")
	# js_framework = input("JS Framwork (vuejs/react): ")
	# css_library = input("CSS Option (tailwind/bootstrap/vuetify): ")
	pass

template_dir = Path("templates")

if not template_dir.exists():
	raise AssertionError("Templates directory missing")

# Recursive structure
with open("directory_schema.json", "r") as f:
	directory_structure = json.load(f)

# generate_directory(directory_structure, Path("."), spa_name)

import os

if not Path(spa_name).exists():
	Path(spa_name).mkdir()

for root, dirs, files in os.walk('templates', topdown=True):
	base_path = Path(root.replace('templates', spa_name))

	for d in dirs:
		d_path = base_path / d
		if not d_path.exists():
			print(d_path)
			d_path.mkdir()
	
	for f in files:
		f_path = base_path / f
		if not f_path.exists():
			f_path.touch()
		
		with f_path.open('w') as new_file:
			temp_file = open(Path(root) / f, 'r')
			new_file.write(temp_file.read())
			temp_file.close()
			
		


			
