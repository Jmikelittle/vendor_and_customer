import json
import os

# Define JSON Schema for vendor record structure based on Appendix B
vendor_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Vendor Record Structure",
    "description": "Data elements based on Treasury Board of Canada's Standard on Vendor Record",
    "type": "object",
    "required": [
        "legalName",
        "countryCode",
        "vendorIdentificationNumbers"
    ],
    "properties": {
        "legalName": {
            "description": "Legal name of the vendor",
            "type": "string",
            "maxLength": 120
        },
        "operatingName": {
            "description": "Operating name if different from legal name",
            "type": "string",
            "maxLength": 120
        },
        "countryCode": {
            "description": "Country code (ISO 3166-1 alpha-2)",
            "type": "string",
            "pattern": "^[A-Z]{2}$"
        },
        "vendorIdentificationNumbers": {
            "type": "object",
            "description": "Collection of identification numbers",
            "properties": {
                "businessNumber": {
                    "description": "Business Number (BN) assigned by CRA",
                    "type": "string",
                    "pattern": "^[0-9]{9}$"
                },
                "supplierNumber": {
                    "description": "Supplier identification number",
                    "type": "string"
                },
                "gstHstNumber": {
                    "description": "GST/HST Registration Number",
                    "type": "string",
                    "pattern": "^[0-9]{9}RT[0-9]{4}$"
                },
                "dunsNumber": {
                    "description": "D-U-N-S Number",
                    "type": "string",
                    "pattern": "^[0-9]{9}$"
                },
                "qstNumber": {
                    "description": "Quebec Sales Tax Number",
                    "type": "string"
                }
            }
        },
        "contactInformation": {
            "type": "object",
            "properties": {
                "address": {
                    "type": "object",
                    "properties": {
                        "streetAddress": {
                            "type": "string",
                            "maxLength": 100
                        },
                        "city": {
                            "type": "string",
                            "maxLength": 50
                        },
                        "province": {
                            "type": "string",
                            "maxLength": 50
                        },
                        "postalCode": {
                            "type": "string",
                            "maxLength": 10
                        }
                    },
                    "required": ["streetAddress", "city", "postalCode"]
                },
                "telephone": {
                    "type": "string",
                    "pattern": "^[0-9]{10,15}$"
                },
                "email": {
                    "type": "string",
                    "format": "email"
                }
            }
        },
        "organizationType": {
            "description": "Type of organization",
            "type": "string",
            "enum": ["Individual", "Business", "Government", "NGO", "Other"]
        },
        "size": {
            "description": "Size of the organization",
            "type": "string",
            "enum": ["Small", "Medium", "Large"]
        },
        "aboriginalStatus": {
            "description": "Aboriginal status indicator",
            "type": "boolean"
        },
        "minorityStatus": {
            "description": "Visible minority indicator",
            "type": "boolean"
        },
        "womenOwnedStatus": {
            "description": "Women-owned business indicator",
            "type": "boolean"
        },
        "bankingInformation": {
            "type": "object",
            "properties": {
                "accountHolderName": {
                    "type": "string"
                },
                "bankIdentifier": {
                    "type": "string"
                },
                "branchIdentifier": {
                    "type": "string"
                },
                "accountNumber": {
                    "type": "string"
                }
            }
        },
        "commodityCodes": {
            "description": "UNSPSC commodity codes",
            "type": "array",
            "items": {
                "type": "string"
            }
        }
    }
}

# Create a sample vendor record that would validate against the schema
sample_vendor = {
    "legalName": "ABC Company Inc.",
    "operatingName": "ABC Solutions",
    "countryCode": "CA",
    "vendorIdentificationNumbers": {
        "businessNumber": "123456789",
        "supplierNumber": "SUPP-12345",
        "gstHstNumber": "123456789RT0001"
    },
    "contactInformation": {
        "address": {
            "streetAddress": "123 Main Street",
            "city": "Ottawa",
            "province": "Ontario",
            "postalCode": "K1A 0A9"
        },
        "telephone": "6135551234",
        "email": "contact@abccompany.com"
    },
    "organizationType": "Business",
    "size": "Medium",
    "aboriginalStatus": False,
    "minorityStatus": False,
    "womenOwnedStatus": True,
    "commodityCodes": ["43211500", "43232400"]
}

def save_json_files():
    # Create a directory for the schema files if it doesn't exist
    os.makedirs("vendor_schema", exist_ok=True)
    
    # Save the schema file
    with open("vendor_schema/vendor_schema.json", "w") as schema_file:
        json.dump(vendor_schema, schema_file, indent=2)
    
    # Save the sample vendor file
    with open("vendor_schema/sample_vendor.json", "w") as sample_file:
        json.dump(sample_vendor, sample_file, indent=2)
    
    print("JSON schema and sample files have been created in the 'vendor_schema' directory.")
    
    # Instructions for using the schema
    print("\nTo validate vendor data against this schema, you can use libraries like:")
    print("- jsonschema (Python)")
    print("- Ajv (JavaScript/Node.js)")

if __name__ == "__main__":
    save_json_files()