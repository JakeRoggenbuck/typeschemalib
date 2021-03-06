class StmlWriter:
    """Write schema syntax in ether file, lines or dictionary

    self.schema is the dictionary of the key -> type pair
    self.lines is the syntax split into lines
    self.save_to_file() will swrite self.lines to a file specified"""
    def __init__(self, data, strict=False):
        self.data = data
        self.strict = strict
        self.schema = self.construct_key_type_pair()
        self.lines = self.construct_lines_with_schemma_dict()

    def check_type(self, value):
        """Check type of value and return string of name

        Return the string of the name of the data type"""
        if isinstance(value, str):
            return "Str"
        elif isinstance(value, bool):
            return "Bool"
        elif isinstance(value, float):
            return "Float"
        elif isinstance(value, int):
            return "Int"
        elif not self.strict:
            return "Undef"
        else:
            raise ValueError("Not writable value")

    def construct_key_type_pair(self):
        """Construct the key -> type pair dictionary

        Check the key for each value of data, then write a new entry in the
        dictionary with the key being the original key and the value being the
        type returned by the check_type()"""
        schema = {}
        for key, value in self.data.items():
            _type = self.check_type(value)
            schema[key] = _type
        return schema

    def construct_lines_with_schemma_dict(self):
        """Generate list if lines with the stml schema

        Get the new schema dictionary generated by the construct_key_type_pair
        and make a line with the key and value"""
        lines = []
        for key, value in self.schema.items():
            lines.append(f"{key}: {value}")
        return lines

    def save_to_file(self, filename: str):
        """Save all the lines to the file"""
        with open(filename, 'w') as file:
            for line in self.lines:
                file.write(f"{line}\n")


class StmlReader:
    def __init__(self, schema_file):
        """Get schema_file as name and save file and save file as stml_file"""
        self.schema_file = schema_file
        self.lines = self._final_lines()

    def _get_file(self):
        """Open schema_file and return as file"""
        file = open(self.schema_file, 'r')
        return file

    def _get_lines(self):
        """Get lines of file"""
        file = self._get_file()
        lines = file.readlines()
        return lines

    def _clean_line(self, line):
        """Clean new lines from file"""
        line = line.rstrip('\n')
        return line

    def _final_lines(self):
        """Return final lines"""
        lines = self._get_lines()
        lines = [line.rstrip('\n') for line in lines]
        return lines


class StmlParser:
    def __init__(self, schema_lines):
        self.schema_lines = schema_lines
        self.schema_dict = self.parse()

    def split_key_type(self, line, num):
        """Split key: type from line"""
        if ":" in line:
            line = line.split(":")
            return line
        else:
            raise ValueError(f"Line {num} has no ':' to separate key and type")

    def parse_line(self, line, num):
        """Clean and split line, get key and type and return as
        dict with key and type"""
        # Get key and type from line split by ':'
        line = self.split_key_type(line, num)
        # Set both values of line_key and line_type
        line_key, line_type = line
        line_type = line_type.lstrip()
        return {"key": line_key, "type": line_type}

    def parse(self):
        """Run parse_line for each line and get all lines"""
        all_lines = {}
        for num, line in enumerate(self.schema_lines):
            new_line = self.parse_line(line, num+1)
            all_lines[new_line["key"]] = new_line["type"]
        return all_lines


class DataChecker:
    def __init__(self, schema: dict, data: dict):
        """Run StmlParser on file name 'schema'"""
        self.schema = schema
        self.data = data

    def check_type(self):
        """Check type from schema for each key in the dictionary

        Return True if all data types are correct according to schema, return
        error if the schema does not match"""
        line_num = 1
        for key, value in self.data.items():
            # Get type listed in schema
            stml_value = self.schema.get(key)
            # Check type and key are listed in schema
            if stml_value is None:
                return f"{key} not in schema"
            # Check if type is listed as int and can be an int
            if stml_value == "Int":
                if not int(value) == value:
                    return f"{value} not {stml_value} on line {line_num}"
            # Check if type is listed as str and if it should be
            elif stml_value == "Str":
                if not str(value) == value:
                    return f"{value} not {stml_value} on line {line_num}"
            # Check if type is a float in schema and if it should be
            elif stml_value == "Float":
                if not float(value) == value:
                    return f"{value} not {stml_value} on line {line_num}"
            elif stml_value == "Bool":
                if not bool(value) == value:
                    return f"{value} not {stml_value} on line {line_num}"
            elif stml_value == "Undef":
                pass
            else:
                # Check if type exists in schema
                if stml_value == "" or stml_value == " ":
                    return f"{value} has no specified type on line {line_num}"
                else:
                    # Warn the type is incorrect
                    return f"{value} has incorrect or non existent type on line {line_num}"
            line_num += 1
        return True


def schema_check(schema, data):
    """Check type and parse accordingly

    Check if the entered schema is a filename: str, a dict or a list, use
    different built in parsing tools to check type"""
    if isinstance(schema, str):
        # If schema is filename
        lines = StmlReader(schema).lines
        schema_dict = StmlParser(lines).schema_dict
        dataChecker = DataChecker(schema_dict, data)
    if isinstance(schema, list):
        # If schema is a list of stml
        schema_dict = StmlParser(schema).schema_dict
        dataChecker = DataChecker(schema_dict, data)
    if isinstance(schema, dict):
        # If schema is a dict of stml
        dataChecker = DataChecker(schema, data)

    valid = dataChecker.check_type()
    return valid
