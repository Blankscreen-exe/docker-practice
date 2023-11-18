import os
import json
import re

START_INDICATOR = "<!--contribution-guidelines-start-->"
END_INDICATOR = "<!--contribution-guidelines-end-->"

def format_content(text):
    pattern = r'`([^`]*)`'
    formatted_text = re.sub(pattern, r'<span class="code-item">\1</span>', text)
    return formatted_text
  
def parse_contrib_guidelines():
  """Reads and parses contribution guidelines inside README.md"""
  
  with open(os.path.dirname(__file__) + '/../README.md', 'r') as file:
        
        lines = file.readlines()
        
        content_found = False
        
        content_to_export = []
        
        content_counter = 1
        
        for index, line in enumerate(lines):
          # switches for table area location in README
          if START_INDICATOR in line:
            content_found = True
            print(f"==== \033[01;46mSTART FOUND at {index}\033[00m ====")
            continue
          if END_INDICATOR in line:
            print(f"==== \033[01;46mEND FOUND AT {index}\033[00m ====")
            break
          
          if content_found:
            # split the string by "|"
            data = line.strip().split("- [x] ")[1] 
            content = format_content(data)
            
            # fix elements of jso data before creating a json data pack 
            try:
              
              json_data = {
                  "id": content_counter,
                  "content": content
              }
              # append the data
              content_to_export.append(json_data)
              
              content_counter += 1
              
              print(f"==== Successfully appended list item at line number \033[93m({index})\033[00m ====")
              print(title)
              
            except:
              pass
        
        # write data to data.json file
        with open(os.path.dirname(__file__) + '/../data/contibution_guidelines.json', 'w') as data_file:
          data_file.write(json.dumps(content_to_export, indent=4))
          print(f"==== Successfully json data to docs/data/contibution_guidelines.json ====")
          

if __name__=="__main__":
  parse_contrib_guidelines()