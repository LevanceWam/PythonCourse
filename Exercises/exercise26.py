# Create a function showEmployee() in a way that it should collect the employee name and salary
# display the salary and the name and if the salary argument is missing it should still
# display a value
# By Levance Wamley jr


def showEmployee(name, salary=9000):
    print(f'The employee name is {name}, The salary is {salary}')


showEmployee('jack', 3000)
