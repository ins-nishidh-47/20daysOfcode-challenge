import pickle
#  the process of converting a Python object structure into a byte stream, which can then be stored in a file or transmitted over a network, and "unpickling" is the reverse process of reconstructing the object from the byte stream. 

# binary file

# Methods of Opening file
file = open("bin_files/challenge.dat","ab") #1
print(pickle.load(file))
file.close()
# => In first you have to close the file after opening
with open("bin_files/challenge.dat","ab") as file:
    print(pickle.load(file))
# => whereas with open automatically close the file

# Modes of Opening File
# -> (ab, wb, rb, ab+, rb+, wb+)
# ab -> (creates file if file isn't created and to write)
with open("bin_files/file_ab.dat", "ab") as f:
    pickle.dump(["This is appended text."],f)

# wb -> (creates and overwrites the file if it exists)
with open("bin_files/file_wb.dat", "wb") as f:
    pickle.dump(["This is appended text."],f)

# rb -> (opens the file in read mode, not related to destruct and struct of file)
with open("bin_files/file_r.dat", "rb") as f:
    print(f)

# ab+ -> (pointer is positioned in the end of the file, create file if not exist)
with open("bin_files/file_ab+.dat", "ab+") as f:
    pickle.dump(["Appended text."],f)
    f.seek(0)   # Move pointer to the beginning for reading
    print(pickle.load(f))  
    
# rb+ -> (pointer is positioned in the start of the file, doesn't create file if not exist)
with open("bin_files/file_rb+.dat", "rb+") as f:
    print(pickle.load(f))  # Display current content
    f.seek(0)        # Move pointer to the start
    pickle.dump(["Modified"],f)  # Overwrites from the start

# wb+ -> (truncates the file if exists and other functionality is same like write and read mode)
with open("bin_files/file_wb+.dat", "wb+") as f:
    f.write(["Fresh content."])
    f.seek(0)        # Move pointer to the start
    print(pickle.load(f))  # Display new content


#Methods for binary file handling
# open()	Opens a file (use mode like 'rb', 'wb', 'ab', etc.)
# read(size)	Reads the specified number of bytes from the file.
# readline()	Reads one line from the file (less common in binary files).
# readlines()	Reads all lines into a list.
# write(data)	Writes binary data to the file.
# writelines(lines)	Writes a list of lines to the file.
# seek(offset, whence)	Moves the pointer to a specific position.
# tell()	Returns the current file pointer position.
# flush()	Flushes the internal buffer to ensure data is written immediately.
# close()	Closes the file.

# #pickling methods
# pickle.dump(obj, file)	Serializes and writes obj to a binary file.
# pickle.load(file)	Deserializes data from the file back into Python objects.
# pickle.dumps(obj)	Serializes obj into a byte stream (string format).
# pickle.loads(byte_data)	Deserializes byte_data back into a Python object.


# Writing Data to a .dat File

# Sample data (e.g., dictionary)
data = {'name': 'Nishidh', 'age': 18, 'city': 'Lucknow'}

# Writing data to a binary file
with open('data.dat', 'wb') as file:
    pickle.dump(data, file)

print("Data written successfully!")

#reading data from binary file

# Reading data from binary file
with open('data.dat', 'rb') as file:
    loaded_data = pickle.load(file)

print("Loaded Data:", loaded_data)
