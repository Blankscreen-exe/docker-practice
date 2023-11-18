import os
import json

TABLE_START_INDICATOR = "<!--tutorials-table-start-->"
TABLE_END_INDICATOR = "<!--tutorials-table-end-->"

def parse_markdown_table():
  """Reads and parses table inside README.md"""
  
  with open(os.path.dirname(__file__) + '/../README.md', 'r') as file:
        
        lines = file.readlines()
        
        table_found = False
        
        table_data_to_export = []
        
        for index, line in enumerate(lines):
          # switches for table area location in README
          if TABLE_START_INDICATOR in line:
            table_found = True
            print(f"==== \033[01;46mSTART FOUND at {index}\033[00m ====")
            continue
          if TABLE_END_INDICATOR in line:
            print(f"==== \033[01;46mEND FOUND AT {index}\033[00m ====")
            break
          
          if table_found:
            # split the string by "|"
            data = line.strip().split("|")
            # filter the list for any empty strings
            data = [item for item in data if item != ""]
            
            # fix elements of jso data before creating a json data pack 
            try:
              id = int(data[0])
              status = data[1].split('"')[1]
              title = data[2].strip().split("]")[0][1:]
              link = data[2].strip().split("(")[1][1:-2]
              tags =  [tag.strip() for tag in data[3].strip().replace("`", "").split(",")]
              
              json_data = {
                  "id": id,
                  "status": status,
                  "topic": {
                      "title": title,
                      "link": link
                  },
                  "tags": tags
              }
              # append the data
              table_data_to_export.append(json_data)
              print(f"==== Successfully appended list item with id \033[93m({id})\033[00m at line number \033[93m({index})\033[00m ====")
              print(title)
              
            except:
              pass
        
        # write data to data.json file
        with open(os.path.dirname(__file__) + '/../data/data.json', 'w') as data_file:
          data_file.write(json.dumps(table_data_to_export, indent=4))
          print(f"==== Successfully json data to docs/data/data.json ====")
          

if __name__=="__main__":
  parse_markdown_table()