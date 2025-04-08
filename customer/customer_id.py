import json
import os

def generate_customer_schema():
    """
    Generates the customer record schema based on the Treasury Board standard.
    
    References Appendix B: Customer Record Structure from the 
    Standard on Customer Records (https://www.tbs-sct.canada.ca/pol/doc-eng.aspx?id=25857)
    """
    schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "title": "Customer Record Schema",
        "description": "Schema for customer records as per Treasury Board Standard on Customer Records",
        "type": "object",
        "required": ["customerID", "customerType", "contactInformation"],
        "properties": {
            "customerID": {
                "type": "string",
                "description": "Unique identifier for the customer"
            },
            "customerType": {
                "type": "string",
                "description": "Type of customer",
                "enum": ["Individual", "Business", "Government", "NGO", "Other"]
            },
            "legalName": {
                "type": "string",
                "description": "Full legal name of the customer (individual or organization)"
            },
            "operatingName": {
                "type": "string",
                "description": "Operating or doing business as name if different from legal name"
            },
            "contactInformation": {
                "type": "object",
                "description": "Contact information for the customer",
                "required": ["address"],
                "properties": {
                    "address": {
                        "type": "object",
                        "required": ["streetAddress", "city", "country"],
                        "properties": {
                            "streetAddress": {
                                "type": "string"
                            },
                            "city": {
                                "type": "string"
                            },
                            "province": {
                                "type": "string",
                                "description": "Province or territory (required for Canadian addresses)"
                            },
                            "postalCode": {
                                "type": "string",
                                "description": "Postal code or ZIP code"
                            },
                            "country": {
                                "type": "string",
                                "description": "Country code (ISO 3166-1 alpha-2)"
                            }
                        }
                    },
                    "telephone": {
                        "type": "string"
                    },
                    "email": {
                        "type": "string",
                        "format": "email"
                    },
                    "alternateContact": {
                        "type": "object",
                        "properties": {
                            "name": {
                                "type": "string"
                            },
                            "telephone": {
                                "type": "string"
                            },
                            "email": {
                                "type": "string",
                                "format": "email"
                            }
                        }
                    }
                }
            },
            "language": {
                "type": "string",
                "description": "Official language preference",
                "enum": ["English", "French"]
            },
            "identificationNumbers": {
                "type": "object",
                "description": "Various identification numbers that may be used depending on customer type",
                "properties": {
                    "businessNumber": {
                        "type": "string",
                        "description": "CRA Business Number for businesses"
                    },
                    "programIdentifier": {
                        "type": "string",
                        "description": "Program-specific identifier"
                    }
                }
            },
            "accountStatus": {
                "type": "string",
                "description": "Current status of the customer account",
                "enum": ["Active", "Inactive", "Suspended", "Closed"]
            },
            "accountDetails": {
                "type": "object",
                "description": "Additional account details",
                "properties": {
                    "creationDate": {
                        "type": "string",
                        "format": "date"
                    },
                    "lastModified": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "servicePreferences": {
                        "type": "object",
                        "properties": {
                            "communicationMethod": {
                                "type": "string",
                                "enum": ["Email", "Mail", "Phone"]
                            }
                        }
                    }
                }
            }
        }
    }
    
    schema_path = os.path.join(
        os.path.dirname(__file__), 
        "customer_schema", 
        "customer_schema.json"
    )
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(schema_path), exist_ok=True)
    
    with open(schema_path, 'w', encoding='utf-8') as f:
        json.dump(schema, f, indent=2)
    
    print(f"Customer schema written to {schema_path}")
    
def generate_sample_customer():
    """
    Generates sample customer records that comply with the schema.
    Creates samples for different customer types based on the Treasury Board standard.
    """
    # Individual customer example
    individual_customer = {
        "customerID": "CUST12345",
        "customerType": "Individual",
        "legalName": "Jane Smith",
        "contactInformation": {
            "address": {
                "streetAddress": "123 Main Street",
                "city": "Ottawa",
                "province": "Ontario",
                "postalCode": "K1A 0A9",
                "country": "CA"
            },
            "telephone": "6135551234",
            "email": "jane.smith@example.com"
        },
        "language": "English",
        "accountStatus": "Active",
        "accountDetails": {
            "creationDate": "2025-01-15",
            "lastModified": "2025-04-08T10:15:30",
            "servicePreferences": {
                "communicationMethod": "Email"
            }
        }
    }
    
    # Business customer example
    business_customer = {
        "customerID": "CUST67890",
        "customerType": "Business",
        "legalName": "Maple Innovations Inc.",
        "operatingName": "Maple Tech",
        "contactInformation": {
            "address": {
                "streetAddress": "456 Business Avenue, Suite 300",
                "city": "Toronto",
                "province": "Ontario",
                "postalCode": "M5V 2H1",
                "country": "CA"
            },
            "telephone": "4165557890",
            "email": "contact@mapletech.example.com",
            "alternateContact": {
                "name": "John Doe",
                "telephone": "4165559876",
                "email": "john.doe@mapletech.example.com"
            }
        },
        "language": "English",
        "identificationNumbers": {
            "businessNumber": "123456789",
            "programIdentifier": "PRG1234"
        },
        "accountStatus": "Active",
        "accountDetails": {
            "creationDate": "2024-11-05",
            "lastModified": "2025-04-01T09:30:15",
            "servicePreferences": {
                "communicationMethod": "Email"
            }
        }
    }
    
    # Government customer example
    government_customer = {
        "customerID": "CUST24680",
        "customerType": "Government",
        "legalName": "Department of Innovation",
        "contactInformation": {
            "address": {
                "streetAddress": "789 Government Road",
                "city": "Ottawa",
                "province": "Ontario",
                "postalCode": "K1A 1A1",
                "country": "CA"
            },
            "telephone": "6135552468",
            "email": "info@innovation.gc.ca"
        },
        "language": "English",
        "identificationNumbers": {
            "programIdentifier": "GC5678"
        },
        "accountStatus": "Active"
    }
    
    # Save the sample files
    schema_dir = os.path.join(os.path.dirname(__file__), "customer_schema")
    os.makedirs(schema_dir, exist_ok=True)
    
    # Save individual customer
    with open(os.path.join(schema_dir, "sample_customer.json"), 'w', encoding='utf-8') as f:
        json.dump(individual_customer, f, indent=2)
    
    # Save business customer
    with open(os.path.join(schema_dir, "sample_business_customer.json"), 'w', encoding='utf-8') as f:
        json.dump(business_customer, f, indent=2)
    
    # Save government customer
    with open(os.path.join(schema_dir, "sample_government_customer.json"), 'w', encoding='utf-8') as f:
        json.dump(government_customer, f, indent=2)
    
    print(f"Sample customer records written to {schema_dir}")

if __name__ == "__main__":
    generate_customer_schema()
    generate_sample_customer()
