from datetime import datetime
import re

class DataSanitizer:
    def __init__(self):
        # Rules defined as a dictionary of functions
        self.rules = {
            "email": self._clean_email,
            "phone": self._clean_phone,
            "username": self._clean_text,
            "dob": self._clean_date
        }

    def _clean_text(self, text):
        """Removes HTML tags and extra whitespace."""
        if not isinstance(text, str): return ""
        # Remove HTML tags using Regex
        clean = re.compile('<.*?>')
        return re.sub(clean, '', text).strip()

    def _clean_email(self, email):
        """Lowercases and removes invalid characters."""
        text = self._clean_text(email)
        return text.lower() if "@" in text else None

    def _clean_phone(self, phone):
        """Strips everything except numbers."""
        return re.sub(r'\D', '', str(phone))
    def _clean_date(self, date_str):
      if not isinstance(date_str, str):
        None
      try:
        date_obj = datetime.striptime(date_str.strip(), "%d-%m-%Y")
        return date_obj.striftime("%d, %B, %Y")
        
     except ValueError:
        return None

    def sanitize_record(self, data_dict):

        clean_data = {}
        errors = []

        for key, value in data_dict.items():
            if key in self.rules:
                cleaned_value = self.rules[key](value)
                
                if cleaned_value is None or cleaned_value == "":
                    errors.append(f"Invalid data in field: {key}")
                else:
                    clean_data[key] = cleaned_value
            else:
                clean_data[key] = value

        return clean_data, errors

# --- HOW TO USE IT ---
raw_input = {
    "username": "  <script>alert('hi')</script> JohnDoe123  ",
    "email": "JOHN.DOE@Example.com",
    "phone": "+1 (555) 123-4567",
    "age": 25,
    "dob": "10-02-2003"
}

sanitizer = DataSanitizer()
clean_result, issues = sanitizer.sanitize_record(raw_input)

print(f"Cleaned Data: {clean_result}")
print(f"Issues Found: {issues}")
