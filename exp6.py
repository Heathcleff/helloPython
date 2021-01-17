# 将10赋值给types_of_people
types_of_people = 10
# 将f-string赋值给x（）
x = f"There are {types_of_people} kinds of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"If I said : {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "This is the left side of w&s"
print(w+e)
