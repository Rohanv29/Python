#wap to create a tuple(name, department,salary)
# employee1= ("John Doe", "Engineering", 75000)
# employee2= ("Jane Smith", "Marketing", 65000)
# employee3= ("Alice Johnson", "Finance", 80000)

# #highest salary
# highest_salary = max(employee1[2], employee2[2], employee3[2])
# if highest_salary == employee1[2]:
#     print(f"The employee with the highest salary is {employee1[0]} from {employee1[1]} department with a salary of ${employee1[2]}.")
# elif highest_salary == employee2[2]:
#     print(f"The employee with the highest salary is {employee2[0]} from {employee2[1]} department with a salary of ${employee2[2]}.")
# else:
#     print(f"The employee with the highest salary is {employee3[0]} from {employee3[1]} department with a salary of ${employee3[2]}.")


# #AVAERAGE SALARY
# average_salary = (employee1[2] + employee2[2] + employee3[2]) / 3
# print(f"The average salary of the employees is ${average_salary:.2f}.")

# #top2 highest salaries
# salaries=[employee1[2],employee2[2],employee3[2]]
# salaries.sort(reverse=True)
# print(f"The top 2 highest salaries are ${salaries[0]} and ${salaries[1]}")

employees = (
    ("Rohan", 101, "Developer", 50000),
    ("Rahul", 102, "Designer", 45000),
    ("Priya", 103, "Manager", 70000),
    ("Aman", 104, "Tester", 40000),
    ("Neha", 105, "HR", 55000)
)

# highest_salary=max(i[3] for i in employees )
# print(highest_salary)
average=0
for i in employees:

    average += i[3]
print(average//5)