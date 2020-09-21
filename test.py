from typeschemalib import typeschemalib
from termcolor import colored


if __name__ == "__main__":
    """Test parse with stml file"""
    schema_file = "test.stml"
    data = {"point": 45, "my_string": "Hey", "grade": 4.5}

    lines = typeschemalib.StmlReader(schema_file).lines
    schema_dict = typeschemalib.StmlParser(lines).schema_dict

    dataChecker = typeschemalib.DataChecker(schema_dict, data)
    valid = dataChecker.check_type()
    if valid is True:
        print(colored(valid, 'green'))
    else:
        print(colored(valid, 'red'))

    """Test parse with schema dictionary"""
    data = {"point": 45, "my_string": "Hey", "grade": 4.5}
    schema = {"point": "Int", "my_string": "Str", "grade": "Float"}

    schema_dict = typeschemalib.StmlParser(lines).schema_dict
    dataChecker = typeschemalib.DataChecker(schema, data)

    valid = dataChecker.check_type()
    if valid is True:
        print(colored(valid, 'green'))
    else:
        print(colored(valid, 'red'))
