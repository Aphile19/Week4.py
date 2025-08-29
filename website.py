def file_processing_program():
    """
    This program:
    1. Asks the user for a filename
    2. Handles errors if the file doesn't exist or can't be read
    3. Reads the file content
    4. Creates a modified version (uppercase text in this example)
    5. Writes the modified content to a new file
    """
    
    # Get filename from user
    filename = input("Please enter the filename you want to process: ")
    
    try:
        # Attempt to open and read the file
        with open(filename, 'r') as file:
            content = file.read()
            
        print(f"Successfully read from '{filename}'")
        
        # Create modified content (example: convert to uppercase)
        modified_content = content.upper()
        
        # Create output filename
        output_filename = f"modified_{filename}"
        
        # Write modified content to new file
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)
            
        print(f"Successfully created modified file: '{output_filename}'")
        print(f"Original file size: {len(content)} characters")
        print(f"Modified file size: {len(modified_content)} characters")
        
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found. Please check the filename and try again.")
    
    except PermissionError:
        print(f"Error: You don't have permission to read '{filename}'.")
    
    except IsADirectoryError:
        print(f"Error: '{filename}' is a directory, not a file.")
    
    except UnicodeDecodeError:
        print(f"Error: Cannot read '{filename}' as a text file. It may be a binary file.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

# Additional function with more modification options
def advanced_file_processor():
    """
    Enhanced version with more modification options
    """
    try:
        filename = input("Enter the filename to process: ")
        
        # Read the file
        with open(filename, 'r') as file:
            content = file.read()
        
        print("\nChoose modification option:")
        print("1. Convert to UPPERCASE")
        print("2. Convert to lowercase")
        print("3. Capitalize first letter of each word")
        print("4. Reverse the content")
        
        choice = input("Enter your choice (1-4): ")
        
        # Apply chosen modification
        if choice == '1':
            modified_content = content.upper()
            output_suffix = "_uppercase"
        elif choice == '2':
            modified_content = content.lower()
            output_suffix = "_lowercase"
        elif choice == '3':
            modified_content = content.title()
            output_suffix = "_titlecase"
        elif choice == '4':
            modified_content = content[::-1]
            output_suffix = "_reversed"
        else:
            print("Invalid choice. Using default (uppercase).")
            modified_content = content.upper()
            output_suffix = "_modified"
        
        # Create output filename
        if '.' in filename:
            name, ext = filename.rsplit('.', 1)
            output_filename = f"{name}{output_suffix}.{ext}"
        else:
            output_filename = f"{filename}{output_suffix}"
        
        # Write to new file
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)
        
        print(f"Success! Modified file saved as: {output_filename}")
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error processing file: {e}")

# Run the program
if __name__ == "__main__":
    print("=== File Processing Program ===")
    file_processing_program()
    
    print("\n=== Advanced File Processor ===")
    advanced_file_processor()
