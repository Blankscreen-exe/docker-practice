import re

input_data = "| 019 | <span title='Not Started'>🔴</span> | [Host CMS with backdrop]() | `Hosting`, `CMS` |"

# Define regular expressions to extract the data
id_pattern = r"\| (\d+) \|"
status_pattern = r"title='(.*?)'"
folder_link_pattern = r"\[(.*?)\]"
tags_pattern = r"`(.*?)`"

# Extract data using regular expressions
id_match = re.search(id_pattern, input_data)
status_match = re.search(status_pattern, input_data)
folder_link_match = re.search(folder_link_pattern, input_data)
tags_match = re.search(tags_pattern, input_data)

# Create a dictionary with the extracted data
parsed_data = {
    "id": int(id_match.group(1)) if id_match else None,
    "status": status_match.group(1) if status_match else None,
    "folderLink": folder_link_match.group(1) if folder_link_match else None,
    "topic": folder_link_match.group(1) if folder_link_match else None,
    "tags": [tag.strip() for tag in tags_match.group(1).split(',')] if tags_match else []
}