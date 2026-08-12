# open(file,mode)
# r = read, w = Write (overwrite), a = append, x = create_new_file, r+ = read + write, w+ = write + read, a+ = Apped + read


# Reading process
with open("student.txt") as f:
    print(f"File reading using .read()\n{f.read()}")
    f.seek(0)
    print(f"File reading using .read() and specific index\n{f.read(2)}") # Specific Character 2
    f.seek(0)
    print(f"File reading using .readline()\n{f.readline()}")
    f.seek(0)
    print(f"File reading using .readlines()\n{f.readlines()}") # it returns with array


# Writing process
with open("student.txt","a") as f: # w is overwrite # x is the create file
    print("Writing the content")
    f.write("\nPyae,25,Botony")
    print("Wrote")
