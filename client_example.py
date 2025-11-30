"""
Example Python client for CV Filler API
"""
import requests
import json


class CVFillerClient:
    """Client for interacting with CV Filler API"""
    
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url
    
    def fill_cv_from_files(self, template_path: str, json_path: str, output_path: str):
        """
        Fill CV using file uploads
        
        Args:
            template_path: Path to empty DOCX template
            json_path: Path to JSON data file
            output_path: Where to save the filled CV
        """
        url = f"{self.base_url}/fill-cv/"
        
        with open(template_path, 'rb') as template_file, \
             open(json_path, 'rb') as json_file:
            
            files = {
                'template': ('template.docx', template_file, 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'),
                'cv_data_json': ('data.json', json_file, 'application/json')
            }
            
            response = requests.post(url, files=files)
            response.raise_for_status()
            
            # Save the filled CV
            with open(output_path, 'wb') as output_file:
                output_file.write(response.content)
            
            return output_path
    
    def health_check(self):
        """Check if API is running"""
        try:
            response = requests.get(f"{self.base_url}/")
            return response.status_code == 200
        except:
            return False


# Example usage
if __name__ == "__main__":
    client = CVFillerClient()
    
    # Check if API is running
    if not client.health_check():
        print("❌ API is not running. Please start the API first.")
        print("Run: python cv_filler_api.py")
        exit(1)
    
    print("✅ API is running")
    
    # Fill CV
    try:
        output = client.fill_cv_from_files(
            template_path="empty_DOCX.docx",
            json_path="JSON_input.json",
            output_path="filled_cv_output.docx"
        )
        print(f"✅ CV filled successfully!")
        print(f"Output saved to: {output}")
    except requests.exceptions.HTTPError as e:
        print(f"❌ Error: {e}")
        print(f"Response: {e.response.text}")
    except FileNotFoundError as e:
        print(f"❌ File not found: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
