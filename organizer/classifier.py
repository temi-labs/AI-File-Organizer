import os

def classify_file(file_name):
    ext = os.path.splitext(file_name)[1].lower()

    if ext in [".png", ".jpg", ".jpeg"]:
        return "images"
    elif ext in [".pdf", ".docx", ".txt"]:
        return "documents"
    elif ext in [".mp4", ".mkv"]:
        return "videos"
    elif ext in [".py", ".js", ".html", ".css"]:
        return "code"
    else:
        return "others"
