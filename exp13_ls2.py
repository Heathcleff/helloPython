from sys import argv

print("参数表：书名，作者，版本，是否读完")
script, book_name, author, edition, is_read = argv
print("书名：", book_name, "\n作者：", author, "\n版本：", edition, "\n是否读完:", is_read)
