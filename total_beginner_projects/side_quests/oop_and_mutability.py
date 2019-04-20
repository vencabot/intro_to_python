# The point of type-hinting for parameters is just to help your fellow
# programmers understand how your functions work.

def print_age(person_name: str, person_age: str) -> None:
    print(person_name + " is " + person_age + " years old.")

print_age("Vencabot", "32")
