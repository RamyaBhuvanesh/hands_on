"""
how to read a file
1. open a file in read mode 'r'
2. read it word by word
"""
def fun_to_read():
  file_to_read = "test2.txt"

  read_object = open(file=file_to_read, mode='r')

  print((type(read_object.readline())))
  # print(read_object.read())
  print((read_object.readline()))
  read_object.close()

  print(read_object.readline())

      for line in read_object.readline():

            print(line)




fun_to_read()