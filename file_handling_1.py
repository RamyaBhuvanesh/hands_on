def reader():
    '''

    # read
    reading_object = open(file= "test1.txt",
                                 mode="r"
    #output_of_read = reading_object.read()
    #print(output_of_read)  '''

    '''
    
    # write 
    reading_object = open(file= "test1.txt",
                                 mode="w"
    #output_of_read = reading_object.read()
    #print(output_of_read)   '''

    # append

    reading_object = open(file="test1.txt",
                          mode='a')
    output_of_read = reading_object.write("\n hey you!")

    print(output_of_read)







reader()