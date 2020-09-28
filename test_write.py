from typeschemalib.typeschemalib import StmlWriter


data = {
    "name": "Jake",
    "age": 16,
    "percent": 23.4,
    "hey": type("hey"),
    "passed": True
}

writer = StmlWriter(data)
print(writer.schema)
print(writer.lines)
writer.save_to_file("testtwo.stml")
