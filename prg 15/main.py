"""
Write programs for reading and writing binary files
"""
def write_binary_file(filename, data):
    with open(filename, 'wb') as file:
        file.write(data)

def read_binary_file(filename):
    with open(filename, 'rb') as file:
        return file.read()



data_to_write = b'This is some binary data.'
write_binary_file('example.bin', data_to_write)

read_data = read_binary_file('example.bin')
print("Read binary data:", read_data)

