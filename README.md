# JSON Converter for Pi to Ignition Integration

## Overview

This repository contains a Python script designed to convert CSV files into JSON format, specifically formatted for use with the PI System (OSIsoft) and Ignition. The script facilitates the transfer of site data from the PI System to Ignition by transforming CSV data into a JSON format compatible with Ignition's requirements.

## Features

- **CSV to JSON Conversion**: Converts CSV files into JSON format suitable for Ignition import.
- **Character Replacement**: Automatically replaces certain characters in tag names to ensure compatibility with Ignition.
- **Data Type Translation**: Maps data types and format strings to match Ignition’s and PI System’s expectations.

## Prerequisites

- **Python 3.x**: Ensure Python 3.x is installed on your system. [Download Python](https://www.python.org/).
- **No Additional Libraries Required**: The script uses only built-in Python libraries.

## Installation

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/yourusername/repository.git
    cd repository
    ```

2. **Set Up Environment**: No additional setup is required. Ensure Python 3.x is installed.

## Usage

To convert a CSV file to JSON, use the following command:

```bash
python csv_to_json.py path/to/yourfile.csv
Replace path/to/yourfile.csv with the path to your CSV file. The script will generate a JSON file with the same base name as the CSV file in the same directory.
```

Please ensure that the file you wish to convert is located in your project directory.

## Configuration

### Character Replacement

The `clean_name` function in the script replaces specific characters in tag names to ensure compatibility with Ignition:

- **`.`** is replaced with **`'`**
- **`/`** is replaced with **`)`**
- **`+`** is replaced with **`(`**
- **`@`** is replaced with **`:`**

**Note:** When converting JSON data back to PI System format, you will need to revert these character replacements. Ensure that any special characters, including the `+` sign, are properly restored to match the PI System's requirements.


### Data Type Translation

The script translates the following data types to match Ignition’s requirements:

- **`"Float32"`** is translated to **`"Float4"`**
- **`"Digital"`** is translated to **`"Boolean"`**
- Any other data types are translated to **`"Unknown"`**

These translations ensure that data types from the CSV file are converted to formats that are compatible with Ignition and the PI System.

## Format String Translation
The formatString values are mapped as follows:

- "3" to "00.000"
- "2" to "00.00"
- "1" to "00.0"
- "0" to "00"
- "-2" to "00"
- "-4" to "00.00"

## Integration Context
This script is specifically designed to assist in the integration of Ignition with the PI System by:

- Facilitating Data Transfer: Converting data exported from Ignition into a format that can be easily imported into the PI System.
- Ensuring Compatibility: Adjusting data types and formats to meet the requirements of both Ignition and the PI System.

## File Exclusions
The repository includes a .gitignore file to exclude .csv and .json files from version control. This prevents large or sensitive files from being tracked by Git.

## Contributing

Contributions are welcome! To contribute:

### How to Contribute

1. **Fork the Repository**

   Click the "Fork" button at the top-right of this page to create your own copy of the repository.

2. **Create a Branch**

   Create a new branch for your feature or bug fix:

   ```bash
   git checkout -b feature/your-feature
    ```

3. **Make Changes**
  
    Implement your changes or additions. Make sure to write clear and concise commit messages describing your changes.

4. **Commit Your Changes**

    ```bash
    git add .
    git commit -m 'Add a descriptive message about your changes'
    ```

5. **Push Your Branch**

    ```bash
    git push origin feature/your-feature
    ```

6. **Create a Pull Request**
   
    Navigate to the original repository and click "New Pull Request" to submit your changes.

### Pull Request Guidelines

To ensure a smooth review process, please adhere to the following guidelines when creating a pull request:

#### 1. **Title**

   - Provide a clear and descriptive title for your pull request. Use a format that quickly conveys the purpose, such as:
     - `Fix: Issue with data type translation`
     - `Feature: Add support for new CSV format`
     - `Docs: Update README with new instructions`

#### 2. **Description**

   - **Purpose**: Explain what changes you made and why they are necessary.
   - **Details**: Include any relevant information that reviewers need to understand your changes. This may include:
     - A summary of the issue or feature being addressed.
     - An overview of how your changes address the issue or implement the feature.
     - Links to related issues or documentation.

#### 3. **Testing**

   - **Tests**: Ensure your changes are tested. Describe the tests you have performed:
     - Unit tests
     - Integration tests
     - Manual tests
   - **Test Results**: Confirm that all tests pass and include any relevant information about the testing process.

#### 4. **Code Quality**

   - **Documentation**: Update or add documentation as needed to reflect changes.
   - **Clean Code**: Ensure your code is clean, well-organized, and free of unnecessary comments or debugging code.

#### 5. **Commit Messages**

   - **Clarity**: Write clear and concise commit messages that describe the changes made.


By following these guidelines, you help ensure that your pull request is reviewed efficiently and merged smoothly. Thank you for your contributions!

### License
This project is licensed under the MIT License. See the LICENSE file for details.

### Contact
For questions or feedback, please contact Hannah Sauber.
