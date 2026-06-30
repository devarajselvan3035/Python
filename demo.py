class Error(Exception):
    pass


try:
    value = int(input("Enter the value : "))
except ValueError:
    raise Error("Given value is not integer!")

print("hello world")
