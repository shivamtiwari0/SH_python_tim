import sys


def get_int(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except EOFError:
            sys.exit(1)
        # except ValueError:
        #     print("Enter an integer, Try again")
        except:  # Superclass exception should come after all the exception mentioned in code, to test try
            # it before EOFerror.
            print("Enter an integer, Try again")
        finally:
            print('Finally clause always executes.')


a = get_int("Enter the first no. = ")
b = get_int("Enter the second no. = ")

try:
    print(a/b)
except ZeroDivisionError:
    print("cant divide by zero")
    sys.exit(2)
else:
    print("Division performed successfully")