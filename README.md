# AI File Organizer

A simple Python application to automatically organize files in any folder by categorizing them into subdirectories based on their file types (Images, Videos, Documents, Code, etc.).

## What It Does

The AI File Organizer scans a selected folder and automatically moves files into category-specific subdirectories:
- **Images**: `.png`, `.jpg`, `.jpeg`, `.gif`
- **Videos**: `.mp4`, `.mkv`, `.mov`
- **Documents**: `.pdf`, `.docx`, `.txt`
- **Code**: `.py`, `.js`, `.html`, `.css`
- **Others**: Any file with an unrecognized extension

## Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)
fushiguro
### Step 1: Install Dependencies

Open PowerShell or Command Prompt in the project folder and run:

```bash
pip install -r requirements.txt
```

This will install all required packages:
- `watchdog` (for file monitoring)
- `tkinter` (GUI framework - usually comes with Python)

### Step 2: Verify Installation

Test that everything is working:

```bash
python main.py
```

The GUI window should open without errors.

## How to Use

### Step-by-Step Guide

1. **Launch the Application**
   ```bash
   python main.py
   ```
   A window titled "AI File Organizer" will appear with three main elements:
   - A "🗂️ Pick Folder" button
   - A folder path display area
   - A "🚀 Organize Files" button

2. **Select a Folder**
   - Click the **"🗂️ Pick Folder"** button
   - A system folder browser will open
   - Navigate to the folder you want to organize (e.g., Downloads, Desktop, etc.)
   - Click "Select Folder" to confirm
   - The selected folder path will display below the button

3. **Organize Files**
   - Click the **"🚀 Organize Files"** button
   - The application will scan the folder and move files into category subdirectories
   - A success message will appear once complete
   - Check the console output to see which files were moved and where

4. **Check Results**
   - Open your file explorer and navigate to the selected folder
   - You'll see new subdirectories created for each category (Images, Videos, Documents, Code, Others)
   - Files are now organized by type inside these folders

## Example

**Before:**
```
Downloads/
  ├── photo.jpg
  ├── document.pdf
  ├── video.mp4
  └── script.py
```

**After running the organizer:**
```
Downloads/
  ├── Images/
  │   └── photo.jpg
  ├── Documents/
  │   └── document.pdf
  ├── Videos/
  │   └── video.mp4
  └── Code/
      └── script.py
```

## Configuration

Edit `config.py` to customize file extensions and folder names:

```python
# File extensions for each category
IMAGE_EXT = [".png", ".jpg", ".jpeg", ".gif"]
VIDEO_EXT = [".mp4", ".mkv", ".mov"]
DOC_EXT = [".pdf", ".docx", ".txt"]
CODE_EXT = [".py", ".js", ".html", ".css"]

# Folder names where files will be organized
FOLDERS = {
    "images": "Images",
    "documents": "Documents",
    "videos": "Videos",
    "code": "Code",
    "others": "Others"
}

# Default watch folder (used by the watcher module)
WATCH_FOLDER = "C:/Users/YourName/Downloads"
```

## Troubleshooting

### GUI doesn't open
- Ensure Python is installed correctly: `python --version`
- Verify tkinter is installed: `python -m tkinter`
- On Linux, you may need to install tkinter separately: `sudo apt-get install python3-tk`

### Files not moving
- Check that you have read/write permissions for the selected folder
- Ensure the folder contains files with recognized extensions
- Check the console output for specific error messages

### ImportError when running
- Make sure all dependencies are installed: `pip install -r requirements.txt`
- Verify you're in the correct project directory

## File Structure

```
ai-file-organizer/
├── main.py           # Entry point
├── config.py         # Configuration file
├── organizer.py      # File organization logic
├── requirements.txt  # Dependencies
├── gui/
│   └── app.py        # GUI application
└── organizer/
    ├── classifier.py # File classification
    ├── mover.py      # File movement logic
    └── watcher.py    # File watching (for advanced use)
```

## Advanced Usage (File Watcher)

The application includes a file watcher module that can automatically organize files as they're added to a folder. This requires configuration and is used internally.

## Tips

- **Backup first**: Consider backing up your folder before running the organizer for the first time
- **Test with small folders**: Test with a folder containing a few files to ensure it works as expected
- **Custom extensions**: Modify `config.py` to add or change file extensions for each category
- **Create multiple passes**: You can organize the same folder multiple times with different configurations

## Support

If you encounter issues or have questions about how to use the organizer, check:
1. The console output for error messages
2. The troubleshooting section above
3. Verify file permissions on your system

## License

This project is free to use and modify for personal or commercial purposes.

---

**Created**: February 2026
