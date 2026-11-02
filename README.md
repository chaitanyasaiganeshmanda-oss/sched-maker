# Time Slot Customizer

A simple web application that lets you upload three data files – **Slot Data**, **Schedule**, and **Courses** – and view them.

## Features
- Upload CSV or JSON files for each category.
- Lists the uploaded files with links to view the raw content.
- Built with **Flask** (Python) and plain HTML/CSS, no database required.

## Project Structure
```
time-slot-customizer/
├─ app.py                # Flask server
├─ requirements.txt      # Python dependencies
├─ templates/
│   ├─ upload.html      # Upload form
│   └─ schedule.html    # List of uploaded files
├─ static/
│   └─ style.css        # Simple styling
└─ uploads/              # Runtime folder for uploaded files (created automatically)
```

## Setup & Run
1. Open a terminal and change to the project folder:
   ```
   cd "C:\Users\Chaitanya\.gemini\antigravity\scratch\time-slot-customizer"
   ```
2. Install the required Python packages:
   ```
   python -m pip install -r requirements.txt
   ```
3. Start the web server:
   ```
   python app.py
   ```
   The server will start on **http://127.0.0.1:5000**.

4. Open a browser and navigate to the URL. Use the form to upload your three files. After uploading, you’ll see a list of the files with links to view their contents.

## Customisation
- **Styling** – edit `static/style.css`.
- **Templates** – modify `templates/upload.html` and `templates/schedule.html`.
- **Logic** – the upload handling lives in `app.py`; you can extend it to parse CSV/JSON and render custom schedules.

---
Feel free to ask if you need additional features (e.g., CSV parsing, schedule visualisation, authentication, etc.).
