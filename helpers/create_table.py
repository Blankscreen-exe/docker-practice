import os

README_FILEPATH = os.path.join( "..", "README.md") 

def parse_markdown_table():
  with open(file_path, 'r') as file:
        lines = file.readlines()
