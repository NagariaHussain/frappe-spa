import argparse
import subprocess

from pathlib import Path
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

template_dir = Path("templates")

if not template_dir.exists():
	raise AssertionError("Templates directory missing")

import os

if not Path(spa_name).exists():
	Path(spa_name).mkdir()

for root, dirs, files in os.walk("templates", topdown=True):
	base_path = Path(root.replace("templates", spa_name))

	for d in dirs:
		d_path = base_path / d
		if not d_path.exists():
			d_path.mkdir()

	for f in files:
		f_path = base_path / f
		if not f_path.exists():
			f_path.touch()

		with f_path.open("w") as new_file:
			temp_file_path = Path(root) / f
			if f in template_files:
				# render jinja template
				out = jenv.get_template(str(temp_file_path)).render(
					{"spa_name": spa_name, "app_name": app}
				)
				new_file.write(out)
				continue

			temp_file = open(temp_file_path, "r")
			new_file.write(temp_file.read())
			temp_file.close()

print("Installing packages...")
subprocess.Popen(["yarn", "install"], cwd=spa_name)

print("Staring dev server...")
subprocess.Popen(["yarn", "dev"], cwd=spa_name)