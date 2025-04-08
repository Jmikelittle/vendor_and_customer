import json
import os

def generate_customer_schema():
    """
    Generates the customer record schema based on the Treasury Board standard.
    """
    # The schema is already created in customer_schema/customer_schema.json
    print("Customer schema already exists.")
    
def generate_sample_customer():
    """
    Generates a sample customer record that complies with the schema.
    """
    sample_customer = {
        "customerID": "CUST12345",
        "customerType": "Individual",
        "contactInformation": {
            "address": {
                "streetAddress": "123 Main Street",
                "city": "Ottawa",
                "province": "Ontario",
                "postalCode": "K1A 0A9",
                "country": "CA"
            },
            "telephone": "6135551234",
            "email": "customer@example.com"
        }
    }
    
    sample_path = os.path.join(
        os.path.dirname(__file__), 
        "customer_schema", 
        "sample_customer.json"
    )
    
    with open(sample_path, 'w') as f:
        json.dump(sample_customer, f, indent=2)
    
    print(f"Sample customer record written to {sample_path}")

if __name__ == "__main__":
    generate_customer_schema()
    generate_sample_customer()
