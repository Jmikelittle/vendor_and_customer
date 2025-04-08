import json
import os

# Define JSON Schema for vendor record structure based on Appendix B of Treasury Board policy
vendor_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Vendor Record Structure",
    "description": "Data elements based on Treasury Board of Canada's Standard on Vendor Record",
    "type": "object",
    "required": [
        "legalName",
        "countryCode",
        "vendorIdentificationNumbers",
        "organizationType"
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
                    "description": "Business Number (BN) assigned by CRA - 9 digits for base BN, 15 chars for program account (9 digits + 2 letters + 4 digits)",
                    "type": "string",
                    "pattern": "^[0-9]{9}([A-Z]{2}[0-9]{4})?$"
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
                    "type": "string",
                    "pattern": "^[0-9]{10}TQ[0-9]{4}$"
                },
                "sinNumber": {
                    "description": "Social Insurance Number (SIN) - One option for individuals",
                    "type": "string",
                    "pattern": "^[0-9]{9}$"
                },
                "uniqueIdentifier": {
                    "description": "Any unique numeric identifier for individuals",
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
            "description": "Vendor Category as defined in Appendix B",
            "type": "string",
            "enum": [
                "Individual", 
                "Corporation/Partnership", 
                "Employee", 
                "Other Government Department", 
                "Other Government"
            ]
        },
        "taxRecipientType": {
            "description": "CRA-assigned Tax Recipient Type code identifying if the recipient of a taxable form is a public or private entity, non-resident, individual or employee",
            "type": "string",
            "enum": ["1", "3", "4", ""],
            "default": ""
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
                    "type": "string",
                    "pattern": "^[0-9]{3}$"
                },
                "branchIdentifier": {
                    "type": "string",
                    "pattern": "^[0-9]{5}$"
                },
                "accountNumber": {
                    "type": "string",
                    "pattern": "^[0-9]{7,12}$"
                }
            },
            "required": [
                "accountHolderName",
                "bankIdentifier",
                "branchIdentifier",
                "accountNumber"
            ]
        },
        "commodityCodes": {
            "description": "UNSPSC commodity codes",
            "type": "array",
            "items": {
                "type": "string",
                "pattern": "^[0-9]{8}$"
            }
        }
    },
    "allOf": [
        {
            "if": {
                "properties": {
                    "organizationType": { "enum": ["Individual"] }
                }
            },
            "then": {
                "properties": {
                    "vendorIdentificationNumbers": {
                        "anyOf": [
                            { "required": ["uniqueIdentifier"] },
                            { "required": ["sinNumber"] },
                            { "required": ["businessNumber"] }
                        ]
                    },
                    "taxRecipientType": {
                        "enum": ["1", ""]
                    }
                }
            }
        },
        {
            "if": {
                "properties": {
                    "organizationType": { "enum": ["Corporation/Partnership"] }
                }
            },
            "then": {
                "properties": {
                    "taxRecipientType": {
                        "enum": ["3", "4", ""]
                    }
                }
            }
        },
        {
            "if": {
                "properties": {
                    "organizationType": { "enum": ["Corporation/Partnership"] },
                    "countryCode": { "enum": ["CA"] }
                }
            },
            "then": {
                "properties": {
                    "vendorIdentificationNumbers": {
                        "required": ["businessNumber"]
                    }
                }
            }
        },
        {
            "if": {
                "properties": {
                    "countryCode": { "enum": ["CA"] }
                }
            },
            "then": {
                "properties": {
                    "contactInformation": {
                        "properties": {
                            "address": {
                                "properties": {
                                    "postalCode": {
                                        "pattern": "^[A-Z][0-9][A-Z]\\s?[0-9][A-Z][0-9]$"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        {
            "if": {
                "properties": {
                    "countryCode": { "enum": ["US"] }
                }
            },
            "then": {
                "properties": {
                    "contactInformation": {
                        "properties": {
                            "address": {
                                "properties": {
                                    "postalCode": {
                                        "pattern": "^[0-9]{5}(-[0-9]{4})?$"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    ]
}

# Create example vendor records for different types
corporation_vendor = {
    "legalName": "ABC Company Inc.",
    "operatingName": "ABC Solutions",
    "countryCode": "CA",
    "organizationType": "Corporation/Partnership",
    "taxRecipientType": "3",  # Corporation
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
            "postalCode": "K1A0A9"
        },
        "telephone": "6135551234",
        "email": "contact@abccompany.com"
    },
    "size": "Medium",
    "aboriginalStatus": False,
    "minorityStatus": False,
    "womenOwnedStatus": True,
    "commodityCodes": ["43211500", "43232400"]
}

individual_vendor = {
    "legalName": "John Smith",
    "countryCode": "CA",
    "organizationType": "Individual",
    "taxRecipientType": "1",  # Individual
    "vendorIdentificationNumbers": {
        "uniqueIdentifier": "ID12345678",
        "supplierNumber": "IND-67890"
    },
    "contactInformation": {
        "address": {
            "streetAddress": "456 Oak Avenue",
            "city": "Toronto",
            "province": "Ontario",
            "postalCode": "M5V2N4"
        },
        "telephone": "4165559876",
        "email": "john.smith@example.com"
    },
    "aboriginalStatus": False,
    "minorityStatus": False,
    "womenOwnedStatus": False
}

sole_proprietor = {
    "legalName": "Jane's Consulting",
    "operatingName": "JC Consulting",
    "countryCode": "CA",
    "organizationType": "Individual",
    "taxRecipientType": "1",  # Individual sole proprietor
    "vendorIdentificationNumbers": {
        "businessNumber": "987654321",
        "supplierNumber": "SP-12345"
    },
    "contactInformation": {
        "address": {
            "streetAddress": "789 Birch Street",
            "city": "Montreal",
            "province": "Quebec",
            "postalCode": "H2X1Y6"
        },
        "telephone": "5145556789",
        "email": "jane@jcconsulting.ca"
    },
    "size": "Small",
    "aboriginalStatus": False,
    "minorityStatus": False,
    "womenOwnedStatus": True
}

partnership_vendor = {
    "legalName": "XYZ Partners LLP",
    "operatingName": "XYZ Advisory",
    "countryCode": "CA",
    "organizationType": "Corporation/Partnership",
    "taxRecipientType": "4",  # Partnership
    "vendorIdentificationNumbers": {
        "businessNumber": "456789123",
        "supplierNumber": "PART-6789"
    },
    "contactInformation": {
        "address": {
            "streetAddress": "555 Partner Avenue",
            "city": "Vancouver", 
            "province": "British Columbia",
            "postalCode": "V6B5K3"
        },
        "telephone": "6045557890",
        "email": "info@xyzpartners.ca"
    },
    "size": "Medium",
    "aboriginalStatus": False,
    "minorityStatus": False,
    "womenOwnedStatus": False
}

ogd_vendor = {
    "legalName": "Department of Innovation",
    "operatingName": "DOI",
    "countryCode": "CA",
    "organizationType": "Other Government Department",
    "taxRecipientType": "",  # Left blank as per guidance
    "vendorIdentificationNumbers": {
        "businessNumber": "987654321",
        "supplierNumber": "GOV-54321"
    },
    "contactInformation": {
        "address": {
            "streetAddress": "789 Government Road",
            "city": "Ottawa",
            "province": "Ontario",
            "postalCode": "K1P5M7"
        },
        "telephone": "6135557890",
        "email": "contact@doi.gc.ca"
    }
}

employee_vendor = {
    "legalName": "Alex Johnson",
    "countryCode": "CA",
    "organizationType": "Employee",
    "taxRecipientType": "",  # Left blank for employees
    "vendorIdentificationNumbers": {
        "uniqueIdentifier": "EMP123456",
        "supplierNumber": "EMP-54321"
    },
    "contactInformation": {
        "address": {
            "streetAddress": "123 Employee Drive",
            "city": "Ottawa",
            "province": "Ontario",
            "postalCode": "K2P1X3"
        },
        "telephone": "6139995555",
        "email": "alex.johnson@gc.ca"
    }
}

def save_json_files():
    # Create a directory for the schema files if it doesn't exist
    os.makedirs("vendor_schema", exist_ok=True)
    
    # Save the schema file
    with open("vendor_schema/vendor_schema.json", "w", encoding='utf-8') as schema_file:
        json.dump(vendor_schema, schema_file, indent=2)
    
    # Save the sample vendor files
    with open("vendor_schema/sample_vendor.json", "w", encoding='utf-8') as sample_file:
        json.dump(corporation_vendor, sample_file, indent=2)
    
    with open("vendor_schema/sample_individual.json", "w", encoding='utf-8') as individual_file:
        json.dump(individual_vendor, individual_file, indent=2)
    
    with open("vendor_schema/sample_sole_proprietor.json", "w", encoding='utf-8') as sp_file:
        json.dump(sole_proprietor, sp_file, indent=2)
    
    with open("vendor_schema/sample_partnership.json", "w", encoding='utf-8') as part_file:
        json.dump(partnership_vendor, part_file, indent=2)
    
    with open("vendor_schema/sample_ogd.json", "w", encoding='utf-8') as ogd_file:
        json.dump(ogd_vendor, ogd_file, indent=2)
    
    with open("vendor_schema/sample_employee.json", "w", encoding='utf-8') as emp_file:
        json.dump(employee_vendor, emp_file, indent=2)
    
    print("JSON schema and sample files have been created in the 'vendor_schema' directory.")
    
    # Instructions for using the schema
    print("\nTo validate vendor data against this schema, you can use libraries like:")
    print("- jsonschema (Python)")
    print("- Ajv (JavaScript/Node.js)")
    print("\nNote: Different vendor categories require different identification numbers:")
    print("- Individuals can use a unique identifier, SIN, or business number (for sole proprietors)")
    print("- Canadian Corporations/Partnerships require a Business Number")
    print("- Tax Recipient Type codes: '1' for individuals/sole proprietors, '3' for corporations, '4' for partnerships")
    print("- Government entities and employees typically leave Tax Recipient Type blank")

if __name__ == "__main__":
    save_json_files()