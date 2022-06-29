new = open("test_file.txt", "a")    # 'a' - append. The line or data specified will be appended to the file
new.write("\nOrange")               # we can use the write method to add 'orange' to the file in a new line
new.close()

new2 = open("test_file.txt", "r")           # we then open the file in default mode and print it
print(new2.read())
new2.close()
