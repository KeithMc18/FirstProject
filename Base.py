print("Hello World")

answer = 42
name = "Python"

print(f"I have been developing in {name} for {answer} days")

number = 5
if number == 5:
    print("Number is 5")
else:
    print("Number is not 5")


my_list = ["John", "Luke", "Mary", "Joseph"]

len(my_list)
del my_list[0]

for i in my_list:
    print("The students is {0}".format(i))

x = 0
while x <= 10:
    print("Count is {0}".format(x))
    x += 1

student = {
    "name": "Mark",
    "student_id": 123210,
    "feedback": None
}

try:
    number_plus_name = name + answer
except KeyError:
    print("Error finding last_name")
except Exception as error:   #Exception is too broad on its own
    print("Unknown Error: ")
    print(error)


