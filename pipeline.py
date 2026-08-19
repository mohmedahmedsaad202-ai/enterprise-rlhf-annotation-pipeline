import re
import json

class DataSanitizer:
    """Sanitizes raw AI datasets by detecting PII and structural errors."""

    @staticmethod
    def mask_pii(text: str) -> str:
        # Mask emails and basic phone numbers for data privacy
        email_pattern = r'[\w\.-]+@[\w\.-]+\.\w+'
        phone_pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
        
        sanitized = re.sub(email_pattern, "[REDACTED_EMAIL]", text)
        sanitized = re.sub(phone_pattern, "[REDACTED_PHONE]", sanitized)
        return sanitized

    @staticmethod
    def validate_schema(record: dict) -> bool:
        required_keys = ["prompt", "response_a", "response_b"]
        return all(key in record and isinstance(record[key], str) for key in required_keys)

if __name__ == "__main__":
    sample_raw = {
        "prompt": "Contact me at user@example.com for AI training.",
        "response_a": "Here is the response.",
        "response_b": "Alternative response."
    }
    
    if DataSanitizer.validate_schema(sample_raw):
        sample_raw["prompt"] = DataSanitizer.mask_pii(sample_raw["prompt"])
        print("Sanitizer Test Passed:", json.dumps(sample_raw, indent=2))
