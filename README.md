# 🧹 CSV File Cleaner

![Python Version](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Dependencies](https://img.shields.io/badge/Dependencies-csv%20%7C%20pathlib-orange)
![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen)
![License](https://img.shields.io/badge/License-MIT-green)

A Python CLI automation tool that cleans and standardizes CSV datasets by removing inconsistencies, eliminating duplicate records, and generating a cleaned output file.

The program processes CSV files non-destructively by preserving the original dataset, creating a cleaned copy, and generating a summary report of all modifications performed during execution.

---

## 🖥️ Pipeline Lifecycle & Live Demo

### Ingestion ➔ Processing ➔ Output

<p align="center">
  <img src="images/before.png" width="380" alt="Original CSV Dataset" />
  <img src="images/terminal.png" width="380" alt="CSV Cleaning Process" />
</p>

<p align="center">
  <img src="images/after.png" width="765" alt="Cleaned CSV Output" />
</p>

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
