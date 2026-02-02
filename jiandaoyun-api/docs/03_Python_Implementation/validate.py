import os
import json
import sys

def validate_schemas(schema_dir):
    print(f"Validating schemas in {schema_dir}...")
    valid_count = 0
    error_count = 0
    
    if not os.path.exists(schema_dir):
        print(f"Schema directory {schema_dir} does not exist.")
        return False

    for filename in os.listdir(schema_dir):
        if filename.endswith(".json"):
            filepath = os.path.join(schema_dir, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    schema = json.load(f)
                    # Basic check for JSON Schema structure
                    if "type" not in schema and "$ref" not in schema:
                        print(f"Warning: {filename} might not be a valid schema (missing type or $ref)")
                    valid_count += 1
            except json.JSONDecodeError as e:
                print(f"Error decoding {filename}: {e}")
                error_count += 1
            except Exception as e:
                print(f"Error processing {filename}: {e}")
                error_count += 1
                
    print(f"Validation complete. Valid: {valid_count}, Errors: {error_count}")
    return error_count == 0

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    schema_dir = os.path.join(base_dir, "schemas")
    
    success = validate_schemas(schema_dir)
    sys.exit(0 if success else 1)
