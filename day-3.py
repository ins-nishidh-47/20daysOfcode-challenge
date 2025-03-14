#Python file handling

#text file

# Methods of Opening file
file = open("challenge.txt") #1
print(file.read())
file.close()
# => In first you have to close the file after opening
with open("challenge.txt") as file:
    print(file.read())
# => whereas with open automatically close the file

# Modes of Opening File
# -> (a, w, r, a+, r+, w+)
# a -> (creates file if file isn't created and to write)
with open("txt_files/file_a.txt", "a") as f:
    f.write("This is appended text.\n")

# w -> (creates and overwrites the file if it exists)
with open("txt_files/file_w.txt", "w") as f:
    f.write("This is new content.\n")

# r -> (opens the file in read mode, not related to destruct and struct of file)
with open("txt_files/file_r.txt", "r") as f:
    print(f.read())  

# a+ -> (pointer is positioned in the end of the file, create file if not exist)
with open("txt_files/file_a+.txt", "a+") as f:
    f.write("Appended text.\n")
    f.seek(0)   # Move pointer to the beginning for reading
    print(f.read())  
    # f.readline() -> read a single line 
    # f.readlines() -> reads every line and return a list of string

# r+ -> (pointer is positioned in the start of the file, doesn't create file if not exist)
with open("txt_files/file_r+.txt", "r+") as f:
    print(f.read())  # Display current content
    f.seek(0)        # Move pointer to the start
    f.write("Modified")  # Overwrites from the start

# w+ -> (truncates the file if exists and other functionality is same like write and read mode)
with open("txt_files/file_w+.txt", "w+") as f:
    f.write("Fresh content.\n")
    f.seek(0)        # Move pointer to the start
    print(f.read())  # Display new content

# close()	Closes the file
# detach()	Returns the separated raw stream from the buffer
# fileno()	Returns a number that represents the stream, from the operating system's perspective
# flush()	Flushes the internal buffer
# isatty()	Returns whether the file stream is interactive or not
# read()	Returns the file content
# readable()	Returns whether the file stream can be read or not
# readline()	Returns one line from the file
# readlines()	Returns a list of lines from the file
# seek()	Change the file position
# seekable()	Returns whether the file allows us to change the file position
# tell()	Returns the current file position
# truncate()	Resizes the file to a specified size
# writable()	Returns whether the file can be written to or not
# write()	Writes the specified string to the file
# writelines()	Writes a list of strings to the file
