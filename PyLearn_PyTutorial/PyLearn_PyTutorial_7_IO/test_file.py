def testWriteFile1():
    print("ENTER testWriteFile1()...")

    fout = open('testfile.txt', 'w')

    numCharacters = 0
    numCharacters += fout.write("This is first line of text file\n")
    numCharacters += fout.write("This is second line of text file\n")
    print("Number of Characters written = " + str(numCharacters))

    fout.close()
    print(".EXIT testWriteFile1().")

def testWriteFile2():
    print("ENTER testWriteFile2()...")

    fout = open('testfile.txt', 'a')

    for i in range(5):
        for j in range(10):
            fout.write( str( (i+1)*(j+1) ) + ' ' )  
        fout.write('\n') # there is no such function called writeline()

    fout.close();
    print(".EXIT testWriteFile2().")

def testReadFile1():
    print("ENTER testReadFile1()...")

    fin = open('testfile.txt', 'r')

    str = fin.read()    # read() without argument, it will read the whole file

    print(str)

    fin.close();
    print(".EXIT testReadFile1().")

def testReadFile2():
    print("ENTER testReadFile2()...")

    # The advantage of using 'with' is that the file is properly closed
    # after its suite finishes, even if an exception is raised at some point. 
    with open('testfile.txt') as fin:
        print("reading...")
        read_data = fin.read()
        print("data read => \n" + read_data)

    print("File is closed? => " + str(fin.closed))    
    print(".EXIT testReadFile2().")

def testReadFile3():
    print("ENTER testReadFile3()...")

    with open('testfile.txt') as fin:
        while True:
            print("reading...")
            read_data = fin.read(25)
            if not read_data:
                break
            print("data read => \n" + read_data)

    print("File is closed? => " + str(fin.closed))    
    print(".EXIT testReadFile3().")

def testReadFile4():
    print("ENTER testReadFile4()...")

    with open('testfile.txt') as fin:
        while True:
            print("reading...")
            read_data = fin.readline()
            if not read_data:
                break
            print("data read => \n" + read_data)

    print("File is closed? => " + str(fin.closed))    
    print(".EXIT testReadFile4().")

def testReadFile5():
    print("ENTER testReadFile5()...")

    with open('testfile.txt') as fin:
        for read_data in fin:
            print("reading...")
            print("data read => \n" + read_data)

    print("File is closed? => " + str(fin.closed))    
    print(".EXIT testReadFile5().")

testReadFile5()

def testReadFile6():
    print("ENTER testReadFile6()...")

    read_data = []
    with open('testfile.txt') as fin:
        print("reading...")
        read_data = fin.readlines()
        print("data read => \n" + str(read_data))

    print("File is closed? => " + str(fin.closed))    
    print(".EXIT testReadFile6().")

def testReadFile7():
    print("ENTER testReadFile7()...")

    read_data = []
    with open('testfile.txt') as fin:
        print("reading...")
        read_data = list(fin)
        print("data read => \n" + str(read_data))

    print("File is closed? => " + str(fin.closed))    
    print(".EXIT testReadFile7().")

def testReadFile8():
    print("ENTER testReadFile8()...")

    with open('testfile.txt','r') as fin:   # TEXT mode

                       # initially, position is 0
        print("== File Object's position = " + str(fin.tell()) + " ==")
        read_data = fin.read(5) 
        print(read_data)

        fin.seek(40)    # seek to offset 40 from beginning of file
        print("== File Object's position = " + str(fin.tell()) + " ==")
        read_data = fin.read(5)
        print(read_data)

        fin.seek(8)     # seek to offset 8 from beginning of file
                        # JUMP BACKWARD IS OKAY       
        print("== File Object's position = " + str(fin.tell()) + " ==")
        read_data = fin.read(5)
        print(read_data)

        fin.seek(65, 0) # seek to offset 65 from beginning of file (whence equals 0)
                        # whence equals 0 is the default
        print("== File Object's position = " + str(fin.tell()) + " ==")
        read_data = fin.read(5)
        print(read_data)

        fin.seek(0,1)   # seek to offset 0 from current position (whence equals 1)
                        # i.e. NOT DOING ANYTHING
        print("== File Object's position = " + str(fin.tell()) + " ==")
        read_data = fin.read(5)
        print(read_data)

        fin.seek(0,2)  # seek to offset 0 before end of file (whence equals 2)
        print("== File Object's position = " + str(fin.tell()) + " ==")
        read_data = fin.read(5)
        print(read_data)

        print("File is closed? => " + str(fin.closed))    
    print(".EXIT testReadFile8().")

def testReadFile9():
    print("ENTER testReadFile9()...")

    with open('testfile.txt','rb') as fin:   # BINARY mode

        fin.seek(35)    # seek to offset 35 from beginning of file        
        print("== File Object's position = " + str(fin.tell()) + " ==")
        
        fin.seek(5,1)   # seek to offset 5 from current position (whence equals 1)
        print("== File Object's position = " + str(fin.tell()) + " ==")
        read_data = fin.read(5)
        print(read_data)

        fin.seek(-37,1)   # seek to offset -37 from current position (whence equals 1)
        print("== File Object's position = " + str(fin.tell()) + " ==")
        read_data = fin.read(5)
        print(read_data)

        fin.seek(-10,2)  # seek to offset -10 before end of file (whence equals 2)
        print("== File Object's position = " + str(fin.tell()) + " ==")
        read_data = fin.read(5)
        print(read_data)
        
        print("File is closed? => " + str(fin.closed))    
    print(".EXIT testReadFile9().")

testWriteFile1()
testWriteFile2()
testReadFile1()
testReadFile2()
testReadFile3()
testReadFile4()
testReadFile5()
testReadFile6()
testReadFile7()
testReadFile8()
testReadFile9()


