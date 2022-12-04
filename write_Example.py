"""

this is write function

1. create a object to open a file in write mode -'w'
2. perform the write action
3. close the object

"""
def fun_to_write():
    filename_to_write = "test2.txt"
    write_object_example1 = open(file=filename_to_write, mode='w')

    list_1 = ["this is line 1",
              "this is line 2",
              "this is line 3",
              "this is line 4"]
    write_object_example1.write(list_1)

    write_object_example1.close()

fun_to_write()
