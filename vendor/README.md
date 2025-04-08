# Vendor Management Module

This module provides tools for managing vendor data according to the Treasury Board of Canada's Standard on Vendor Records.

## Files

- **vendor_id.py**: Defines the JSON schema for vendor records based on Treasury Board policy and generates sample vendor data files for different vendor types (Corporation, Individual, Sole Proprietor, Partnership, OGD, Employee).

- **validate_vendor.py**: Provides functionality to validate vendor data against the defined schema.

## Schema Files

The schema and sample files are saved in the `vendor_schema` directory:

- **vendor_schema.json**: The JSON schema defining the structure and validation rules for vendor records.
- **sample_vendor.json**: Example of a corporation vendor.
- **sample_individual.json**: Example of an individual vendor.
- **sample_sole_proprietor.json**: Example of a sole proprietor vendor.
- **sample_partnership.json**: Example of a partnership vendor.
- **sample_ogd.json**: Example of an Other Government Department vendor.
- **sample_employee.json**: Example of an employee vendor.

## Vendor Categories

The schema supports different vendor categories as defined in Appendix B of the Treasury Board policy:

1. **Individual**: Can use unique identifier, SIN, or business number (for sole proprietors).
2. **Corporation/Partnership**: Canadian entities require a Business Number.
3. **Employee**: For internal staff members.
4. **Other Government Department**: For inter-departmental transactions.
5. **Other Government**: For other government entities.

## Tax Recipient Types

- `1`: Individuals/sole proprietors
- `3`: Corporations
- `4`: Partnerships
- Empty string: Government entities and employees

## Usage

```python
from validate_vendor import validate_vendor

# Load your vendor data
vendor_data = {...}  # Your vendor data here

# Validate the vendor data
is_valid, message = validate_vendor(vendor_data)
print(f"Valid: {is_valid}, Message: {message}")
```