# Customer Management Module

This module provides tools for managing customer data according to the established customer record standards.

## Files

- **customer_id.py**: Contains functions to generate customer schema and sample customer data.

- **validate_customer.py**: Provides functionality to validate customer data against the defined schema.

## Schema Files

The schema and sample files are saved in the `customer_schema` directory:

- **customer_schema.json**: The JSON schema defining the structure and validation rules for customer records.
- **sample_customer.json**: Example of a customer record.

## Customer Types

The module supports different customer types as defined in the schema, including "Individual" and potentially other types.

## Usage

```python
from validate_customer import validate_customer

# Load your customer data
customer_data = {...}  # Your customer data here

# Validate the customer data
is_valid, message = validate_customer(customer_data)
print(f"Valid: {is_valid}, Message: {message}")
```

## Requirements

The validation functionality requires the `jsonschema` package:

```bash
pip install jsonschema
```