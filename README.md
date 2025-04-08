# Vendor and Customer Record Management

## Overview
This project implements two Treasury Board of Canada standards:
1. Standard on Vendor Records ([Policy Reference](https://www.tbs-sct.canada.ca/pol/doc-eng.aspx?id=25845))
2. Standard on Customer Records ([Policy Reference](https://www.tbs-sct.canada.ca/pol/doc-eng.aspx?id=25857))

It provides JSON schema validation and sample data for both vendor and customer records in compliance with government requirements.

## Documentation
- [Vendor Module Documentation](vendor/README.md) - Detailed information about vendor record management
- [Customer Module Documentation](customer/README.md) - Detailed information about customer record management

## Purpose
The tools in this repository ensure that vendor and customer records follow the standardized data structures defined in their respective Treasury Board policies. This standardization helps government departments maintain consistent and interoperable information across systems.

## Features
- JSON schema validation for vendor and customer records
- Support for all vendor categories defined in the government standard:
  - Individual (Citizens, individuals, and sole proprietors)
  - Corporation/Partnership
  - Employee
  - Other Government Department (OGD)
  - Other Government
- Flexible identification number requirements based on vendor category
- CRA Tax Recipient Type code validation
- Country-specific validation for address formats
- Sample records for all vendor and customer categories

## File Structure
- `/vendor` - Vendor record management
  - `/vendor_schema` - Directory containing the vendor schema and sample files
    - `vendor_schema.json` - The JSON schema definition
    - `sample_vendor.json` - Example of a Corporation/Partnership vendor
    - `sample_individual.json` - Example of an Individual vendor
    - `sample_sole_proprietor.json` - Example of a Sole Proprietor
    - `sample_partnership.json` - Example of a Partnership vendor
    - `sample_ogd.json` - Example of an Other Government Department vendor
    - `sample_employee.json` - Example of an Employee vendor
  - `vendor_id.py` - Script to generate vendor schema and sample files
  - `validate_vendor.py` - Utility to validate vendor records against the schema
- `/customer` - Customer record management
  - `/customer_schema` - Directory containing the customer schema and sample files
    - `customer_schema.json` - The JSON schema definition for customers
  - `customer_id.py` - Script to generate customer schema and sample files
  - `validate_customer.py` - Utility to validate customer records against the schema

## Usage
### Generating the Vendor Schema and Samples
```python
python vendor/vendor_id.py
```

### Validating a Vendor Record
```python
from vendor.validate_vendor import validate_vendor
import json

# Load a vendor record
with open('path/to/your/vendor.json', 'r') as file:
    vendor_data = json.load(file)

# Validate the record
is_valid, message = validate_vendor(vendor_data)
print(f"Valid: {is_valid}, Message: {message}")
```

### Generating the Customer Schema and Samples
```python
python customer/customer_id.py
```

### Validating a Customer Record
```python
from customer.validate_customer import validate_customer
import json

# Load a customer record
with open('path/to/your/customer.json', 'r') as file:
    customer_data = json.load(file)

# Validate the record
is_valid, message = validate_customer(customer_data)
print(f"Valid: {is_valid}, Message: {message}")
```

## Vendor Identification Requirements
Different vendor categories require different identification numbers as per Appendix B:

| Vendor Category | Required Identification |
|----------------|------------------------|
| Individual | Any unique identifier, SIN, or Business Number (for sole proprietors) |
| Corporation/Partnership | Business Number (for Canadian entities) |
| Employee | Unique identifier within the department |
| Other Government Department | Department identifier |
| Other Government | Appropriate government identifier |

## Tax Recipient Type
The CRA-assigned Tax Recipient Type code is used for tax purposes and forms. The schema includes validation for these codes:

| Code | Description | Applicable To |
|------|-------------|--------------|
| "1" | Individual sole proprietor | Individuals |
| "3" | Corporation | Corporations |
| "4" | Partnership, association, trust, estate or other | Partnerships, etc. |
| "" (blank) | For entities without an assigned type or for non-taxable vendor records | Government entities, employees, or vendors for grants/contributions |

## License
See the LICENSE file for details.

## Compliance
This implementation aims to comply with:
- Treasury Board of Canada's Standard on Vendor Records as of April 2025
- Treasury Board of Canada's Standard on Customer Records as of April 2025
