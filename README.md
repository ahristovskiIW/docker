# CV Filler API - FastAPI Solution

A FastAPI-based REST API for automatically filling DOCX CV templates with data from JSON files.

## Features

- ✅ Fill DOCX CV templates with structured JSON data
- ✅ Automatic skill categorization
- ✅ Professional experience sorting (reverse chronological)
- ✅ Industry knowledge extraction from projects
- ✅ Proper formatting and styling preservation
- ✅ Two API endpoints: file upload and JSON body

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the API

### Local Development
```bash
python cv_filler_api.py
```

Or using uvicorn directly:
```bash
uvicorn cv_filler_api:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

## API Endpoints

### 1. Fill CV from Uploaded Files
**Endpoint:** `POST /fill-cv/`

Upload both the template and JSON file:

```bash
curl -X POST "http://localhost:8000/fill-cv/" \
  -F "template=@empty_DOCX.docx" \
  -F "cv_data_json=@JSON_input.json" \
  -o filled_cv.docx
```

### 2. Fill CV from JSON Body
**Endpoint:** `POST /fill-cv-from-data/`

Upload template and send JSON in request body (requires multipart/form-data for template + JSON body).

### 3. Interactive Documentation
Access the auto-generated API docs at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## JSON Data Structure

The JSON input should follow this structure:

```json
{
  "personal_info": {
    "name": "John Doe",
    "email": "john@example.com",
    "phone": "+1234567890",
    "additional": {
      "position": "Full-Stack Developer"
    }
  },
  "education": [
    {
      "institution": "University Name",
      "degree": "Bachelor",
      "field_of_study": "Computer Science",
      "start_date": "2015",
      "end_date": "2019"
    }
  ],
  "programming_skills": [
    "Python", "Java", "JavaScript", "Docker", "AWS"
  ],
  "soft_skills": [
    "Team collaboration", "Problem solving", "Communication"
  ],
  "projects": [
    {
      "name": "Project Name",
      "description": "Project description",
      "technologies": ["Python", "FastAPI", "Docker"],
      "start_date": "January 2023",
      "end_date": "Current",
      "additional": {
        "industry": "Technology"
      }
    }
  ],
  "other_info": "Professional summary text here..."
}
```

## How It Works

### 1. Template Structure
The system expects a DOCX template with a single table containing:
- **Row 0, Cell 1**: Name and Position
- **Row 1, Cells 0-1**: Summary (merged cells)
- **Row 1, Cell 2**: Education and Industry Knowledge
- **Row 2, Cells 0-1**: Professional Experience (merged cells)
- **Row 2, Cell 2**: Skills

### 2. Data Processing
- **Skills**: Automatically categorized into groups (Programming Languages, Backend, Frontend, Cloud & DevOps, etc.)
- **Projects**: Sorted in reverse chronological order (most recent first)
- **Industries**: Extracted from project metadata
- **Formatting**: Preserves professional styling with appropriate font sizes and bold headers

### 3. Key Features

#### Automatic Skill Categorization
Skills are intelligently grouped into categories:
- Programming Language (C#, Java, JavaScript, etc.)
- Backend Development (.NET Core, Spring Boot, etc.)
- Frontend Development (Angular, React, etc.)
- Cloud & DevOps (AWS, Azure, Docker, Kubernetes)
- Database (PostgreSQL, MySQL, MongoDB)
- Web Services (REST, SOAP, GraphQL)
- CI/CD (Jenkins, Azure DevOps)
- Supporting tools (Git, Jira, Maven)

#### Industry Knowledge Extraction
Industries are automatically extracted from project metadata and displayed under Education section.

#### Date Parsing and Sorting
Projects are sorted by start date in reverse chronological order, with "Current" always appearing first.

## Python Usage (Without API)

You can also use the `CVFiller` class directly in your Python code:

```python
from cv_filler_api import CVFiller, CVData
import json

# Load JSON data
with open('JSON_input.json', 'r') as f:
    cv_data_dict = json.load(f)

cv_data = CVData(**cv_data_dict)

# Fill CV
filler = CVFiller('empty_DOCX.docx')
filler.fill_cv(cv_data)
filler.save('filled_cv.docx')
```

## Advanced Customization

### Custom Skill Categories
Modify the `_categorize_skills()` method to add custom categorization rules:

```python
def _categorize_skills(self, skills: List[str]) -> Dict[str, List[str]]:
    # Add your custom categorization logic
    pass
```

### Custom Formatting
Adjust font sizes, colors, and styling in the individual `_fill_*` methods.

## Error Handling

The API includes comprehensive error handling:
- Invalid JSON format → 400 Bad Request
- Missing template table → 500 Internal Server Error
- File processing errors → 500 Internal Server Error with detailed message

## Testing

### Using cURL
```bash
# Test the fill-cv endpoint
curl -X POST "http://localhost:8000/fill-cv/" \
  -F "template=@empty_DOCX.docx" \
  -F "cv_data_json=@JSON_input.json" \
  -o output_cv.docx

# Verify the output
file output_cv.docx
```

### Using Python requests
```python
import requests

url = "http://localhost:8000/fill-cv/"
files = {
    'template': open('empty_DOCX.docx', 'rb'),
    'cv_data_json': open('JSON_input.json', 'rb')
}

response = requests.post(url, files=files)

with open('filled_cv.docx', 'wb') as f:
    f.write(response.content)
```

## Production Deployment

### Using Docker
```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY cv_filler_api.py .

CMD ["uvicorn", "cv_filler_api:app", "--host", "0.0.0.0", "--port", "8000"]
```

Build and run:
```bash
docker build -t cv-filler-api .
docker run -p 8000:8000 cv-filler-api
```

### Using Gunicorn (for production)
```bash
pip install gunicorn
gunicorn cv_filler_api:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

## License

MIT License - feel free to use and modify as needed.

## Support

For issues or questions, please refer to the FastAPI and python-docx documentation:
- FastAPI: https://fastapi.tiangolo.com/
- python-docx: https://python-docx.readthedocs.io/
