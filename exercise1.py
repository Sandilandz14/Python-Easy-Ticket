with open('sample.txt','w+') as readfile:
    readfile.write("We are love working")
    readfile.close()


with open('sample.txt','r') as readfile:
    print(readfile.read())



