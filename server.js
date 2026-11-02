const express = require('express');
const multer = require('multer');
const path = require('path');
const fs = require('fs');

const app = express();
const port = process.env.PORT || 3000;

// Set up EJS view engine
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// Serve static files
app.use('/static', express.static(path.join(__dirname, 'public')));

// Configure multer for file uploads
const upload = multer({ dest: path.join(__dirname, 'uploads/') });

// Home page – upload form
app.get('/', (req, res) => {
  res.render('upload');
});

// Handle uploads – accept up to three files
app.post('/upload', upload.fields([
  { name: 'slotData', maxCount: 1 },
  { name: 'schedule', maxCount: 1 },
  { name: 'courses', maxCount: 1 }
]), (req, res) => {
  // Files are saved in ./uploads with random filenames
  const files = req.files;
  // For demo, we just list the uploaded file names
  res.render('schedule', { files });
});

// Simple route to view a specific uploaded file (text based)
app.get('/view/:filename', (req, res) => {
  const filePath = path.join(__dirname, 'uploads', req.params.filename);
  if (fs.existsSync(filePath)) {
    const content = fs.readFileSync(filePath, 'utf8');
    res.type('text').send(content);
  } else {
    res.status(404).send('File not found');
  }
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});

