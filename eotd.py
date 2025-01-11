import os
import random
from datetime import datetime
import hashlib
import subprocess
import frontmatter
import utils

def find_unsolved_markdown_files(directory):
    unsolved_files = []
    
    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                try:
                    # Read the frontmatter metadata
                    post = frontmatter.load(file_path)
                    # Check if status exists and is unsolved
                    if post.metadata.get('status') == 'unsolved':
                        unsolved_files.append(file_path)
                except:
                    continue
    
    return sorted(unsolved_files)  # Sort for consistency

def select_random_file(directory):
    # Get all unsolved markdown files
    unsolved_files = find_unsolved_markdown_files(directory)
    
    if not unsolved_files:
        return "No unsolved markdown files found!"
    
    # Get today's date and use it as seed
    today = datetime.now()
    date_string = f"{today.year}-{today.month}-{today.day}"
    hash_value = int(hashlib.sha256(date_string.encode()).hexdigest(), 16)
    random.seed(hash_value)
    
    # Select and return a random file
    random_file = random.choice(unsolved_files)
    return random_file

# Usage example
if __name__ == "__main__":
    # Replace with your Obsidian vault directory
    obsidian_dir = "/home/oferyehuda/physics_exercises/Purcell/6/"
    subprocess.run(['git', 'pull'], cwd="/home/oferyehuda/physics_exercises/")
    random_file = select_random_file(obsidian_dir)
    md = frontmatter.load(random_file)
    title = f"Ex of the day: {random_file.split('/')[-1]}"
    print(f"Selected file: {random_file}")
    utils.send_pushover_notification(md.content, title=title)

