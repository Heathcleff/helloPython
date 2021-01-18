from sys import argv

script, file_dir = argv

txt = open(file_dir)

print(txt.read())
