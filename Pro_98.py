def swapFileData():
    File=input("Ente the File 1")
    File2=input("Enter the File 2")
    with open (File,"r") as a:
        data_a= a.read()
    with open(File2,"r") as b:
        data_b= b.read()
    with open (File,"w") as a:
        a.write(data_b)
    with open (File2,"w") as b:
        b.write(data_a)
    print("Text has been Swaped.")
swapFileData()