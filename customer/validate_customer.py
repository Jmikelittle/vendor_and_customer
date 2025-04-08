import json
import os

try:
    import jsonschema
except ImportError:
    print("Error: The jsonschema package is not installed.")
    print("Please install it using: pip install jsonschema")
    # You can either exit or provide fallback functionality
    jsonschema = None

def validate_customer(customer_data):
    """
    Validates a customer record against the Customer Records schema.
    
    Args:
        customer_data (dict): A dictionary containing customer data.
        
    Returns:
        tuple: (bool, str) - A boolean indicating if the record is valid, 
               and a message providing details on validation result.
    """
    # Check if jsonschema was successfully imported
    if jsonschema is None:
        return False, "Cannot validate: jsonschema package is not installed. Run 'pip install jsonschema' first."
    
    schema_path = os.path.join(
        os.path.dirname(__file__), 
        "customer_schema", 
        "customer_schema.json"
    )
    
    try:
        with open(schema_path, 'r') as f:
            schema = json.load(f)
    except FileNotFoundError:
        return False, f"Schema file not found at {schema_path}"
    except json.JSONDecodeError:
        return False, "Invalid JSON in schema file"
    
    try:
        jsonschema.validate(instance=customer_data, schema=schema)
        return True, "Customer record is valid."
    except jsonschema.exceptions.ValidationError as e:
        return False, f"Validation error: {e.message}"
    except Exception as e:
        return False, f"An error occurred during validation: {str(e)}"

if __name__ == "__main__":
    # Example usage
    print("This module is intended to be imported, not run directly.")
