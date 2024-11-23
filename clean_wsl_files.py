import os
import pathlib

def remove_zone_identifier_files(start_path='.'):
    """
    Recursively walk through directories starting from start_path
    and remove all files containing 'Zone.Identifier' in their name.
    
    Args:
        start_path (str): The directory to start searching from. Defaults to current directory.
    """
    # Convert count variables to lists to allow modification in nested function
    counts = {'found': 0, 'removed': 0, 'errors': 0}
    error_files = []

    def process_directory(path):
        try:
            # Recursively walk through directory
            for root, dirs, files in os.walk(path):
                for file in files:
                    if 'Zone.Identifier' in file:
                        counts['found'] += 1
                        full_path = os.path.join(root, file)
                        try:
                            os.remove(full_path)
                            counts['removed'] += 1
                            print(f"Removed: {full_path}")
                        except (OSError, PermissionError) as e:
                            counts['errors'] += 1
                            error_files.append((full_path, str(e)))
                            print(f"Error removing {full_path}: {e}")

        except Exception as e:
            print(f"Error accessing directory {path}: {e}")
            return

    # Start the cleanup process
    print(f"Starting cleanup from: {os.path.abspath(start_path)}")
    process_directory(start_path)

    # Print summary
    print("\nCleanup Summary:")
    print(f"Files found: {counts['found']}")
    print(f"Files successfully removed: {counts['removed']}")
    print(f"Errors encountered: {counts['errors']}")

    # Print error details if any
    if error_files:
        print("\nError Details:")
        for file, error in error_files:
            print(f"- {file}: {error}")

if __name__ == "__main__":
    # Get current directory as default or accept command line argument
    import sys
    start_directory = sys.argv[1] if len(sys.argv) > 1 else '.'
    
    # Confirm with user before proceeding
    abs_path = os.path.abspath(start_directory)
    print(f"This will remove all 'Zone.Identifier' files from: {abs_path}")
    response = input("Do you want to proceed? (y/n): ").lower()
    
    if response == 'y':
        remove_zone_identifier_files(start_directory)
    else:
        print("Operation cancelled.")