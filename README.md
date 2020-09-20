# lib_type_schema
A yaml like schema file that can assign types and or regex to keys.

## Schema file
#### schema example
```
point: Int
my_string: Str
grade: Float
```

#### data example
```json
{"point": 45, "my_string": "Hey", "grade": 4.5}
```

## Checking data for correct schema

```py
import file_reader

# Set schema file
schema_file = "test.stml"
# Set Data dictionary that corresponds to schema file
data = {"point": 45, "my_string": "Hey", "grade": 4.5}

# Check data for correct schema_file
dataChecker = file_reader.DataChecker(schema_file, data)

# Run type check to see if data corresponds
# valid will be True if schema is correct, it will throw errors otherwise
valid = dataChecker.check_type()
```

## Todo
- Should incorrect schema throw error or just return false?
- Should there be an option for both?
- Have types for id and for more complex types that can be stored in mongodb documents
