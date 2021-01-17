# 将10赋值给types_of_people
types_of_people = 10
# 将f-string赋值给x（这里将type_of_people取代为10）
x = f"There are {types_of_people} kinds of people."

# 将"binary"赋值给binary
binary = "binary"
# 将"don't"赋值给do_not
do_not = "don't"
# 将f-string赋值给y（这里用"binary"和"don't"取代binary和do_not）
y = f"Those who know {binary} and those who {do_not}."

# 打印f-string x
print(x)
# 打印f-string y
print(y)

# 将x嵌套后的f-string输出
print(f"If I said : {x}")
# 将y嵌套后的f-string输出
print(f"I also said: '{y}'")

# 声明一个逻辑变量hilarious，并赋值为伪
hilarious = False
# 声明一个f-stringj，并赋值给joke_valuation
joke_evaluation = "Isn't that joke so funny?! {}"
# 将joke_evaluation输出（花括号内用format的内容补全）
print(joke_evaluation.format(hilarious))

# 将字符串赋值给w
w = "This is the left side of..."
# 将字符串赋值给e
e = "This is the left side of w&s"
# 将w和e两个字符串进行拼接，然后输出拼接结果
print(w + e)
