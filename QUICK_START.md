# Quick Start Guide - CV Filler

## 🚀 Fastest Way to Get Started

### Option 1: Standalone Script (No API needed)
Perfect for one-off CV generation or testing:

```bash
# Install dependencies
pip install python-docx

# Run the script
python fill_cv_standalone.py
```

The script will automatically:
- Read the template from `empty_DOCX.docx`
- Read data from `JSON_input.json`
- Output filled CV to `filled_cv.docx`

### Option 2: FastAPI Server (For production/integration)
For web service integration or multiple requests:

```bash
# Install all dependencies
pip install -r requirements.txt

# Start the server
python cv_filler_api.py
```

Visit `http://localhost:8000/docs` for interactive API documentation.

### Option 3: Docker (Production deployment)
Containerized deployment:

```bash
# Build and run
docker-compose up -d

# API will be available at http://localhost:8000
```

## 📝 Usage Examples

### Using the Standalone Script
```python
from fill_cv_standalone import SimpleCVFiller
import json

# Load your data
with open('your_data.json', 'r') as f:
    cv_data = json.load(f)

# Fill the CV
filler = SimpleCVFiller('your_template.docx')
filler.fill_cv(cv_data)
filler.save('output.docx')
```

### Using the API (cURL)
```bash
curl -X POST "http://localhost:8000/fill-cv/" \
  -F "template=@empty_DOCX.docx" \
  -F "cv_data_json=@JSON_input.json" \
  -o filled_cv.docx
```

### Using the API (Python Client)
```python
from client_example import CVFillerClient

client = CVFillerClient()
client.fill_cv_from_files(
    template_path="empty_DOCX.docx",
    json_path="JSON_input.json",
    output_path="output.docx"
)
```

## 📂 Project Structure

```
cv-filler/
├── cv_filler_api.py          # FastAPI server (full-featured)
├── fill_cv_standalone.py     # Standalone script (no API)
├── client_example.py         # Python client example
├── requirements.txt          # Python dependencies
├── README.md                 # Detailed documentation
├── QUICK_START.md           # This file
├── Dockerfile               # Docker container
└── docker-compose.yml       # Docker orchestration
```

## 🎯 What Each File Does

| File | Purpose | When to Use |
|------|---------|-------------|
| `fill_cv_standalone.py` | Simple Python script | One-off CV generation, testing |
| `cv_filler_api.py` | Full FastAPI server | Production, web integration, multiple users |
| `client_example.py` | API client | Calling the API from Python code |

## 🔧 Customization

### Modify Skill Categories
Edit the `_categorize_skills()` method to change how skills are grouped.

### Change Formatting
Adjust font sizes and styling in the `_fill_*` methods:
- Font size: `run.font.size = Pt(10)`
- Bold text: `run.bold = True`
- Italic text: `run.italic = True`

### Add New Sections
Add new methods to fill additional CV sections and call them from `fill_cv()`.

## ❓ Troubleshooting

### "No module named 'docx'"
```bash
pip install python-docx
```

### "Template document does not contain any tables"
Verify your template DOCX contains at least one table.

### API returns 500 error
Check the server logs for detailed error messages.

## 📊 Performance

- Single CV generation: ~0.5-1 second
- API can handle 50+ concurrent requests
- Memory usage: ~50-100MB per process

## 🔒 Security Notes

For production deployments:
- Add authentication to API endpoints
- Validate and sanitize file uploads
- Implement rate limiting
- Use HTTPS
- Set file size limits

## 📞 Support

Check the detailed README.md for comprehensive documentation including:
- Complete API reference
- JSON data structure
- Advanced customization
- Production deployment guides
- Troubleshooting

---
**Pro Tip:** Start with the standalone script to test your data structure, then move to the API for production use.
