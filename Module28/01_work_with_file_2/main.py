class File:

    def __init__(self, name: str, mode: str, encoding=None):
        self.name = name
        self.mode = mode
        self.encoding = encoding
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.name, self.mode, encoding=self.encoding)
            return self.file
        except FileNotFoundError:
            print(FileNotFoundError)
            self.file = open(self.name, "w", encoding=self.encoding)
            return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        if exc_type:
            print(exc_type)
        else:
            print(f"Файл закрылся: {self.file.closed}")


# with File("text.txt", "r") as file:
#     data = file.write("Hello World")
#     print(data)

with File("text.txt", "a") as file:
    file.write("Hello World")

with File("text.txt", "r") as file:
    data = file.read()
    print(data)