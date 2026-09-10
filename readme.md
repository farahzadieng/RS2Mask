# RS 2 Mask

A Python utility for scanning DICOM directories and interactively selecting radiotherapy structure sets (RTSTRUCT files) from medical imaging data.

## Features

- Scans multiple directories for DICOM RTSTRUCT files
- Displays available structures (ROIs) from selected files
- Interactive CLI to choose a specific structure set
- Configuration-based directory management

## Usage

1. Configure directories in `config.ini`:
   ```ini
   [def]
   directory = /path/to/first/dicom/folder
   directory2 = /path/to/second/dicom/folder
   saveDir = /path/to/save/location
