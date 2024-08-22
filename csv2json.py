import csv
import json
import argparse
import os

def clean_name (Name):
    replacements = {
        ".": "'",
        "@": ":",
        "/": ")",
        "+": "("
    }

    for old_char, new_char in replacements.items():
        Name = Name.replace(old_char, new_char)

    return Name

def csv_to_json(csv_file_path):
    # Generate the JSON file path by changing the extension from .csv to .json
    base, _ = os.path.splitext(csv_file_path)
    json_file_path = base + '.json'
    
    # Initialize the JSON structure
    json_data = {
        "name": "",
        "tagType": "Provider",
        "tags": []
    }
    
    # Read the CSV file
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        # assign a number for tracking in the console
        tcount = 0

        # Process each row in the CSV file
        for row in csv_reader:
            # assign a number for tracking in the console
            tcount += 1
            # Create a tag dictionary for each row
            tag = {
                "name": clean_name(row.get("Name", "")),
                "formatString": row.get("displaydigits",""),
                "engUnit": row.get("engunits", ""),
                "dataType": row.get("pointtype", ""),
                "valueSource": row.get("valueSource", "OPC"),
                "opcItemPath": row.get("instrumenttag", ""),
                "opcServer": row.get("opcServer","")
            }

            #Translate the Datatype to one accepted by Ignition
            if tag["dataType"] == "Float32":
                tag["dataType"] = "Float4"
            elif tag["dataType"] == "Digital":
                tag["dataType"] = "Boolean"
            else:
                tag["dataType"] = "Unknown"

            #Translate the displayDigits to a format accepted by ignition
            if tag["formatString"] == "3":
                tag["formatString"] = "00.000"
            elif tag["formatString"] == "2":
                tag["formatString"] = "00.00"
            elif tag["formatString"] == "1":
                tag["formatString"] = "00.0"
            elif tag["formatString"] == "0":
                tag["formatString"] = "00"
            elif tag["formatString"] == "-2":
                tag["formatString"] = "00"
            elif tag["formatString"] == "-4":
                tag["formatString"] = "00.00"    
            else:
                tag["formatString"] = "00.000"

             

            # Check for special case for _types_ tag
            if tag["name"] == "_types_":
                tag["tagType"] = "Folder"
            
            json_data["tags"].append(tag)

    # Write the JSON data to a file
    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, indent=4)  # indent=4 for pretty-printing
    
    print(f'JSON file created: {json_file_path}')
    print(f'Total Data tags {tcount}\n')

    
def process_all_csv_files():
    """
    Process all CSV files in the directory where the script is located.
    """
    script_dir = os.path.dirname(__file__)
    csv_count = 0
    # Iterate over all files in the script directory
    for file_name in os.listdir(script_dir):
        if file_name.endswith('.csv'):
            csv_file_path = os.path.join(script_dir, file_name)
            csv_to_json(csv_file_path)
            csv_count += 1
    print(f'Total Number of Files Translated: {csv_count}\n')
if __name__ == '__main__':
    #main()
    process_all_csv_files()