replace = open("test_file.txt", "w")    # 'w' - write/replace. The specified data replaces the old data in the file.
replace.write("Now, all the data in the file is replaced by this line")
replace.close()

replace2 = open("test_file.txt", "r")
print(replace2.read())  # only the above specified line in write() method is present in the file so the same is printed
replace2.close()

