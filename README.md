# File Processing and Error Handling Program

A Python program that demonstrates comprehensive file handling with robust error management. This application reads files, creates modified versions, and gracefully handles various file-related exceptions.

## Features

### Core Functionality
- **File Reading**: Safely reads text files with proper encoding handling
- **Content Modification**: Transforms file content using multiple options:
  - Convert to uppercase
  - Convert to lowercase
  - Title case formatting
  - Content reversal
- **File Writing**: Creates new files with modified content
- **Smart Naming**: Automatically generates appropriate output filenames

### Error Handling
The program handles these common file operation errors:
- `FileNotFoundError` - When the specified file doesn't exist
- `PermissionError` - When the user lacks file access permissions
- `IsADirectoryError` - When a directory is provided instead of a file
- `UnicodeDecodeError` - When attempting to read binary files as text
- General exceptions with meaningful error messages

## Requirements

- Python 3.6+
- No external dependencies required

## Usage

### Basic Version
```bash
python file_processor.py
