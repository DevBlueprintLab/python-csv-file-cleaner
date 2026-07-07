# 🧹 CSV File Cleaner

![Python Version](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Dependencies](https://img.shields.io/badge/Dependencies-csv%20%7C%20pathlib-orange)
![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen)
![License](https://img.shields.io/badge/License-MIT-green)

A Python CLI automation tool that cleans and standardizes CSV datasets by removing inconsistencies, eliminating duplicate records, and generating a cleaned output file.

The program processes CSV files non-destructively by preserving the original dataset, creating a cleaned copy, and generating a summary report of all modifications performed during execution.

---


---

## 🧠 Core Features & Architecture

* 🧹 **Automated Data Cleaning:** Removes blank rows and trims unnecessary whitespace from CSV records.
* 🔤 **Text Normalization:** Standardizes text formatting using Title Case for improved consistency.
* 🚫 **Duplicate Detection:** Identifies and removes duplicate records while preserving unique data.
* 💾 **Safe File Processing:** Preserves the original CSV file and saves a cleaned copy in a separate output directory.
* 📊 **Cleaning Report:** Generates a detailed report summarizing processed rows, removed duplicates, blank rows, and output statistics.
* 📁 **Automatic Output Management:** Creates the required output folder automatically when it does not exist.

---

## 🛠️ Tech Stack & Requirements

* **Core Language:** Python 3.x
* **CSV Processing:** `csv`
* **File Handling:** `pathlib`

---

## ⚡ Quick Start & Usage

### 1. Clone the repository

```bash
git clone https://github.com/DevBlueprintLab/python-csv-file-cleaner.git
cd python-csv-file-cleaner
```

### 2. Run the tool

```bash
python csv_file_cleaner.py
```

### 3. Execution example

```text
================
 CSV Cleaner
================

Reading and cleaning CSV file...
Creating cleaned CSV...

---------------
Cleaning completed successfully!
---------------

Rows processed: 120
Rows written: 113

Blank rows removed: 4
Duplicates removed: 3

✓ Cleaned file saved:
cleaned_data.csv

✓ Report saved:
report_data.txt
```

---
## 📁 Project Structure

```text
python-csv-file-cleaner/
├── csv_file_cleaner.py      # Main automation script
├── README.md                # Project documentation
└── images/
    ├── before.png
    ├── terminal.png
    └── after.png
```

---

## 🔮 Roadmap & Future Improvements

* Automatic delimiter detection (comma, semicolon, tab)
* Column-specific cleaning options
* Preserve capitalization for emails and unique identifiers
* Export cleaned data directly to Excel
* Support command-line arguments
* Add logging and execution history

---
Developed by **DevBlueprint Lab**
