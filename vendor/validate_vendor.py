# Additional code to validate vendor data:
from jsonschema import validate

def validate_vendor(vendor_data):
    try:
        validate(instance=vendor_data, schema=vendor_schema)
        return True, "Validation successful"
    except Exception as e:
        return False, str(e)

# Example usage
# is_valid, message = validate_vendor(some_vendor_data)
# print(f"Valid: {is_valid}, Message: {message}")
