import os
import shutil
from pathlib import Path

SOURCE_DIR = os.getcwd()  

FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.svg', '.ico'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.webm', '.flv', '.wmv'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx', '.csv'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac', '.m4a', '.wma'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.sh']
}

def create_folders(base_dir):
    """Create category folders if they don't exist."""
    for folder_name in FILE_TYPES.keys():
        folder_path = os.path.join(base_dir, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Created folder: {folder_name}")

def get_category(extension):
    """Return the category for a given file extension."""
    extension = extension.lower()
    for category, extensions in FILE_TYPES.items():
        if extension in extensions:
            return category
    return None

def organize_files(source_dir):
    """Move files to their respective folders."""
    create_folders(source_dir)
    
    files_moved = 0
    
    
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)
        
        if os.path.isdir(file_path):
            continue
        _, extension = os.path.splitext(filename)
        
        category = get_category(extension)
        
        if category:
            destination = os.path.join(source_dir, category, filename)
            
            shutil.move(file_path, destination)
            print(f"Moved: {filename} -> {category}/")
            files_moved += 1
        else:
            others_path = os.path.join(source_dir, 'Others')
            if not os.path.exists(others_path):
                os.makedirs(others_path)
            destination = os.path.join(others_path, filename)
            shutil.move(file_path, destination)
            print(f"Moved: {filename} -> Others/")
            files_moved += 1

    print("\n" + "="*40)
    print(f"✅ Organization complete! {files_moved} files sorted.")
    print("="*40)

if __name__ == "__main__":
    print(f"Organizing files in: {SOURCE_DIR}")
    organize_files(SOURCE_DIR)