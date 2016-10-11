# Christian Miljkovic
# CSCI-UA.0002 section 03
# Assignment #2

#ask user to enter the file size in kilobytes
og_file= int(input("Enter a file size, in kilobytes (KB): "))
print()
print(og_file, "KB ...")


#convert the input into bits, bytes, megabytes, and gigabytes
file_bytes = og_file*1024.0

file_bits = file_bytes*8.0

file_megabyte= og_file/1024.0

file_gigabyte= file_megabyte/1024.0

#format then print out converted input

form_file_bits = format(file_bits,">29,.2f")

form_file_bytes = format(file_bytes,">28,.2f")

form_file_megabyte= format(file_megabyte,">24,.2f")

form_file_gigabyte= format(file_gigabyte,">24,.2f")

print()
print("... in bits", form_file_bits,"bits")
print("... in bytes", form_file_bytes,"bytes")
print("... in megabytes", form_file_megabyte,"MB")
print("... in gigabytes", form_file_gigabyte,"GB")


# how to crash the program
"""
1. a syntax error would look like-> form_file_bits = format(file_bits,">29,.2f) because I did not put the correct delimiters
2. a runtime error would look like -> form_file_gigabytes= format(file_gigabyte,">24,.2f") because I havent defined form_file_gigabytes previously
3. a logic error would look like -> file_bits = file_bytes*10.0 because that would give us the wrong conversion of bytes to bits
4. another runtime error would look like -> form_file_bits = format(file_bits,">20.2,f") because I did not follow the correct formatting sequence
5. another runtime error would look like -> file_bits == file_bytes/8.0 because the double equal signs compare values and you cannot compare a string to a number

"""
