import os

# Detect if running in GitHub Actions
if os.getenv("GITHUB_ACTIONS") == "true":
    print("Running in GitHub Actions - skipping GUI")
else:
    from gui.app import app
    app.mainloop()

