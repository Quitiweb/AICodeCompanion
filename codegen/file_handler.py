import os

def save_files(filename, code_content, test_filename, test_content):
    try:
        # Save main code file
        with open(filename, 'w') as f:
            f.write(code_content)
            
        # Save test file
        with open(test_filename, 'w') as f:
            f.write(test_content)
            
    except Exception as e:
        raise Exception(f"Failed to save files: {str(e)}")
