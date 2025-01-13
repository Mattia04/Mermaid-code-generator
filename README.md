# Mermaid-code-generator

Generate the mermaid code for a directory using a python script.

## Usage:

On the command line: `python3 script.py`

There are no requirements, just > python3.8.

## Known issues

- It works on macos, it does not on windows and I do not know if it works on linux (I think it will, but I'm not sure).
- There is no error checking (in particular for the settings file) giving the user the same experience of using windows 8.
- There is no depth limit making the graph huge for some directories.
- The variable `output` in `script.pu` should be a str not a list.
- The `.ignore` file is not the best, I would prefer making something like .gitignore (for reference of what I'm thinking, something similar to [https://gist.github.com/jstnlvns/ebaa046fae16543cc9efc7f24bcd0e31](this page).
- There is only graph LR available, I want to add at least mindmap.
- I would like to also add a mermaid code generator given a directory with cpp/python code to create the graph of class structures but this is much harder. Then repeat for the whole code library/package.
