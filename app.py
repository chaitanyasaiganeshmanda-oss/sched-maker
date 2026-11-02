import sys, subprocess
# Ensure Flask is installed – if not, install it automatically
try:
    from flask import Flask, request, render_template, send_from_directory, abort
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
    from flask import Flask, request, render_template, send_from_directory, abort
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'uploads')
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Ensure all three files are provided – otherwise show an error page
    required_fields = ['slotData', 'schedule', 'courses']
    missing = []
    uploaded = {}
    for field in required_fields:
        file = request.files.get(field)
        if not file:
            missing.append(field)
        else:
            filename = secure_filename(file.filename)
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(save_path)
            uploaded[field] = filename
    if missing:
        # Render a simple error template listing missing fields
        return render_template('error.html', missing=missing), 400
    return render_template('schedule.html', files=uploaded)

@app.route('/view/<filename>')
def view_file(filename):
    safe_name = secure_filename(filename)
    path = os.path.join(app.config['UPLOAD_FOLDER'], safe_name)
    if os.path.isfile(path):
        return send_from_directory(app.config['UPLOAD_FOLDER'], safe_name, as_attachment=False)
    else:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

