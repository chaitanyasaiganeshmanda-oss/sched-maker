import os, zipfile, pathlib, sys
src = pathlib.Path(r'C:\Users\Chaitanya\.gemini\antigravity\scratch\time-slot-customizer')
zip_path = pathlib.Path(r'C:\Users\Chaitanya\.gemini\antigravity\brain\9da7ac95-0237-4018-9652-8f4bf1d10e2f\time-slot-customizer.zip')
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
    for root, _, files in os.walk(src):
        for f in files:
            file_path = pathlib.Path(root) / f
            arcname = file_path.relative_to(src)
            zf.write(file_path, arcname)
print('ZIP created at', zip_path)
