from typeschemalib.typeschemalib import DataChecker
from termcolor import colored


if __name__ == "__main__":
    schema_file = "test.stml"
    data = {"point": 45, "my_string": "Hey", "grade": 4.5}

    dataChecker = DataChecker(schema_file, data)
    valid = dataChecker.check_type()
    if valid is True:
        print(colored(valid, 'green'))
    else:
        print(colored(valid, 'red'))
