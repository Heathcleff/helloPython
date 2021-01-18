from sys import argv

script,filename=argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C.")
print("If you want that, hit RETURN")

input("...")

print("Opening the file...")
target=open(filename,'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I will ask you for three lines.")

line1=input("line1:")+"\n"
line2=input("line2:")+"\n"
line3=input("line3:")+"\n"

print("I'm going to write these to the file.")
print("If you don't want that, hit CTRL-C.")
print("If you want that, hit RETURN")

input("...")

target.write(line1+line2+line3)

print("And finally, we'll close it.")
target.close()

