def convert(str):
    """The variable 'string' we created was an unnecessary step. Code works but
    we could've reduced the number of lines as such:

    def convert(string):
    try:
        return float(string)
    except ValueError:
        print("Could not convert the string to a float.")

c = convert("55.0")
print(c) """
    try:
        string = float(str)
        return string
    except (NameError,ValueError):
        print("Input must be a valid number")
