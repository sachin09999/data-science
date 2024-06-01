try:
    with open("a.txt",'x') as f:
        f.write("my name is sachin")
        f.close()
except Exception as e:
    print("file is not present in directory")

else:
    print("successfully appended the data in given file") 