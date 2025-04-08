# Vendor and Customer Record Management

## Overview
This project implements the Treasury Board of Canada's Standard on Vendor Records ([Policy Reference](https://www.tbs-sct.canada.ca/pol/doc-eng.aspx?id=25845)). It provides JSON schema validation and sample data for vendor records in compliance with government requirements.

## Purpose
The tools in this repository ensure that vendor records follow the standardized data structure defined in Appendix B of the Treasury Board policy. This standardization helps government departments maintain consistent and interoperable vendor information across systems.

## Features
- JSON schema validation for vendor records
- Support for all vendor categories defined in the government standard:
  - Individual (Citizens, individuals, and sole proprietors)
  - Corporation/Partnership
  - Employee
  - Other Government Department (OGD)
  - Other Government
- Flexible identification number requirements based on vendor category
- CRA Tax Recipient Type code validation
- Country-specific validation for address formats
- Sample vendor records for all vendor categories

## File Structure
- `vendor_id.py` - Main script to generate the schema and sample files
- `validate_vendor.py` - Utility to validate vendor records against the schema
- `vendor_schema/` - Directory containing the schema and sample files
  - `vendor_schema.json` - The JSON schema definition
  - `sample_vendor.json` - Example of a Corporation/Partnership vendor
  - `sample_individual.json` - Example of an Individual vendor
  - `sample_sole_proprietor.json` - Example of a Sole Proprietor (Individual with business number)
  - `sample_partnership.json` - Example of a Partnership vendor
  - `sample_ogd.json` - Example of an Other Government Department vendor
  - `sample_employee.json` - Example of an Employee vendor

## Usage
### Generating the Schema and Samples
```python
python vendor_id.py
```

### Validating a Vendor Record
```python
from validate_vendor import validate_vendor
import json

# Load a vendor record
with open('path/to/your/vendor.json', 'r') as file:
    vendor_data = json.load(file)

# Validate the record
is_valid, message = validate_vendor(vendor_data)
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
This implementation aims to comply with the Treasury Board of Canada's Standard on Vendor Records as of April 2025.
