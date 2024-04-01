# Grades Auto-Filler

## Overview

This project is designed to assist Teaching Assistants (TAs) and Professors in automating the process of filling and correcting grades electronically. It comprises two main modules: one for processing handwritten grades sheets and another for correcting multiple-choice bubble sheets.

### Module 1: Grades Sheet

#### Input via GUI
- A photo of a printed grades sheet, captured using a mobile camera.

#### Output
- An Excel sheet containing the grades data with the following features:
  - Handling skewed or rotated images.
  - Recognizing different ink colors or clear pencils.
  - Dealing with various formats of the grades sheet, such as different sizes for rows and columns.
  - Recognizing different handwritings and the number of students.

#### Conversion of Data to Text
- Printed Student ID:
  - Users can choose between OCR-based (Option 1) or feature-based with a classifier (Option 2) methods.
- Symbols:
  - ✓: Converted to 5.
  - 𐄂: Converted to 0.
  - -: Converted to 0.
  - Empty cell: Remains empty.
  - Stacked Vertical lines (|||): Converted to the number of lines.
  - Stacked Horizontal lines (-): Converted to (5 - the number of lines).
  - ?: Empty cell with a red background.
  - Numeric values: Users can choose between OCR-based (Option 1) or feature-based with a classifier (Option 2) methods.


#### Example

| Input  | Output                                      |
|-----------|-----------------------------------------------|
| ![3](https://github.com/ahmedibrahim404/grades-auto-filler/assets/34144004/6c9e45a5-527a-4479-ab7c-8cc6e891368a)| ![image](https://github.com/ahmedibrahim404/grades-auto-filler/assets/34144004/2672a9db-652c-48ce-840a-079e2bc00790) |

### Module 2: Bubble Sheet Correction

#### Input via GUI
- Bubble sheets with student IDs.
- Model answer.

#### Output
- Spreadsheet with grades sheet for all students along with answers sheet for each student.


#### Cases
- Handling choosing multiple answers

#### Example

| Input  | Output                                      |
|-----------|-----------------------------------------------|
|![ebb35754-124c-4e35-8ba6-8c6056823e3a](https://github.com/ahmedibrahim404/grades-auto-filler/assets/34144004/6b71d2df-062b-4c10-b1df-0232c750efbe) | ![corrected paper](https://github.com/ahmedibrahim404/grades-auto-filler/assets/34144004/5c415e1f-00ca-4a36-afda-f515541b0f4f) |
| ![8c4d45de-dce5-49ae-9a4d-26f7814d123b](https://github.com/ahmedibrahim404/grades-auto-filler/assets/34144004/0ab6b42c-cc3c-4208-b524-3a67a89f0e89) | ![corrected paper](https://github.com/ahmedibrahim404/grades-auto-filler/assets/34144004/f1a766b9-324f-4dfe-ac99-758f480439f8) |


