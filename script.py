"""
Tree to Mermaid Diagram Generator

Created by: 
@ Mattia Ballico

This Python script generates a Mermaid graph visualization of a directory's tree structure. 
It uses custom styles and icons for different file types, which are based on file extensions, 
and can be configured using an external settings file.

Features:
	- Customizable styles and icons for files based on extensions (e.g., .py, .txt, .csv, etc.).
	- Supports ignoring files listed in a `.ignore` file.
	- Visualizes the directory structure in a left-to-right (LR) Mermaid graph format.
	- Outputs the Mermaid code for easy integration with Markdown in a .txt file.

Usage:
	1. Configure `settings.json` to adjust styles, icons, root directory.
	2. Run the script to generate Mermaid code.
	3. Visualize the result in: "mermaid_code.txt"
"""

import os
from functools import lru_cache

import settings as st

@lru_cache()
def get_ignores():
	with open(".ignore", "r") as file:
		return {line.strip() for line in file.readlines()}

def is_ignored(file_name) -> bool:
	ignores = get_ignores()

	if os.path.isdir(file_name):
		return any(i in file_name for i in ignores)

	return any(i in file_name for i in ignores)

def get_class_style() -> str:
	style = "graph LR\n"

	for extension in st.extension_styles.values():
		style += f"{extension}\n"

	style += f"node0({st.dir_path.split("/")[-1]})\n"

	return style

def get_style(file_name: str) -> str:
	for extension in st.extension_styles:
		if extension in file_name:
			return extension.strip(".")

	return "txt"

def get_icon(root: str, name: str) -> str:
	full_path = root + "/" + name

	if os.path.isdir(full_path):
		return "📂"

	for extension in st.extension_icons:
		if extension in name:
			return st.extension_icons[extension]

	return "📄"

def concatenate(l: list) -> str:
	string = ""

	for elem in l:
		string += elem
	return string

def main():
	ignores = get_ignores()

	output = list(get_class_style())

	node_number = 1
	root_number = {st.dir_path : 0}

	for root, dirs, files in os.walk(st.dir_path):
		if is_ignored(root):
			continue

		files = (file for file in files if not is_ignored(file))
		dirs = (dir_ for dir_ in dirs if not is_ignored(dir_))

		for dir_ in dirs:
			output.append(f"node{root_number[root]} --> node{node_number}({get_icon(root, dir_)} {dir_}):::dir\n")
			root_number[root + "/" + dir_] = node_number
			node_number += 1
			
		for file_ in files:
			output.append(f"node{root_number[root]} --> node{node_number}[{get_icon(root, file_)} {file_}]:::{get_style(file_)}\n")
			node_number += 1

	with open("mermaid_code.txt", "w") as file:
		file.write(concatenate(output))

if __name__ == '__main__':
	main()















