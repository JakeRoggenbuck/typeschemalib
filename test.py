from typeschemalib import typeschemalib


if __name__ == "__main__":
    data = {"point": 45, "my_string": "Hey", "grade": 4.5}

    schema = "test.stml"
    valid = typeschemalib.schema_check(schema, data)
    print(valid)

    schema = ["point: Int", "my_string: Str", "grade: Float"]
    valid = typeschemalib.schema_check(schema, data)
    print(valid)

    schema = {"point": "Int", "my_string": "Str", "grade": "Float"}
    valid = typeschemalib.schema_check(schema, data)
    print(valid)
