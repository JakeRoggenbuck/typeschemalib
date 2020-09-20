import file_reader


if __name__ == "__main__":
    schema_file = "test.stml"
    data = {"point": 45, "my_string": "Hey", "grade": 4.5}

    dataChecker = file_reader.DataChecker(schema_file, data)
    valid = dataChecker.check_type()
    print(valid)
