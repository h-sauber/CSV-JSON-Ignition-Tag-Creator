import csv
import json
import argparse
import os

def clean_name(name):
    replacements = {
        ".": "'",
        "@": ":",
        "/": ")",
        "+": "("
    }
    for old_char, new_char in replacements.items():
        name = name.replace(old_char, new_char)
    return name

def csv_to_json(csv_file_path, output_folder):
    base, _ = os.path.splitext(csv_file_path)
    json_file_path = os.path.join(output_folder, os.path.basename(base)+'.json')
    
    file_name = os.path.basename(base)
    print(f'File Name: {file_name}')
    
    json_data = {
        "name": "",
        "tagType": "Provider",
        "tags": []
    }

    # Try different encodings
    encodings = ['utf-8', 'latin1', 'windows-1252']
    for encoding in encodings:
        try:
            with open(csv_file_path, mode='r', encoding=encoding) as csv_file:
                csv_reader = csv.DictReader(csv_file)

                tcount = 0

                for row in csv_reader:
                    tcount += 1
                    tag = {
                        "name": clean_name(row.get("Name", "")),
                        "formatString": row.get("displaydigits", ""),
                        "engUnit": row.get("engunits", ""),
                        "dataType": row.get("pointtype", ""),
                        "valueSource": row.get("valueSource", "OPC"),
                        "opcItemPath": row.get("instrumenttag", ""),
                        "opcServer": row.get("opcServer", "")
                    }

                    if tag["dataType"] == "Float32":
                        tag["dataType"] = "Float4"
                    elif tag["dataType"] == "Digital":
                        tag["dataType"] = "Boolean"
                    else:
                        tag["dataType"] = "Unknown"

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

                    if tag["name"] == "_types_":
                        tag["tagType"] = "Folder"
                    
                    json_data["tags"].append(tag)

            with open(json_file_path, mode='w', encoding='utf-8') as json_file:
                json.dump(json_data, json_file, indent=4)

            print(f'JSON file created: {json_file_path}')
            print(f'Total Data tags {tcount}\n')
            break  # Exit loop if file is read successfully
        except UnicodeDecodeError:
            print(f"Failed to decode file with encoding {encoding}. Trying next encoding.")
        except Exception as e:
            print(f"An error occurred: {e}")
            break

def process_all_csv_files():
    script_dir = os.path.dirname(__file__)
    input_folder = os.path.join(script_dir, 'input')
    output_folder = os.path.join(script_dir, 'output')
    
    csv_count = 0
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.csv'):
            csv_file_path = os.path.join(input_folder, file_name)
            csv_to_json(csv_file_path, output_folder)
            csv_count += 1
    print(f'Total Number of Files Translated: {csv_count}\n')

if __name__ == '__main__':
    process_all_csv_files()
