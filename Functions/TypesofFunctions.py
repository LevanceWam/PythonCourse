def greet(name):
    print(f"Hi {name}")

# 2 types of functions
# 1- Performs a task
# 2- Return a value


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Vance")
# This implementation can be used in other places
# all functions return none unless it is told to
