# Error Handling


# Possible errors: FileNotFoundError, KeyError, ValueError, IndexError


try:
    # Try this piece of code
    file = open("Days16-31:Intermediate/day30/file.txt")
    dictionary = {"key": "value"}
    print(dictionary["not_a_key"])
except FileNotFoundError:
    # If there is a FileNotFound error, do this
    file = open("file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    # If there is a KeyError do this and remember the error message 
    print(f"The key {error_message} does not exist.")
else:
    # If no exceptions are thrown from the try statement, do this.
    # what else do you want to do.
    content = file.read()
    print(content)
finally:
    # Do this regardless of code succeeding or failing
    file.close()
    
# Raise a false error.
impossible_value = 2
if impossible_value > 0:
	raise ValueError("Value too large.")
