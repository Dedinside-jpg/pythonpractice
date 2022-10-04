file = open("text.txt", "w+")

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        file.write("HelloWorld\n")
    elif i % 3 == 0:
        file.write("Hello\n")
    elif i % 5 == 0:
        file.write("World\n")
    else:
        file.write(str(i)+"\n")
file.close()


