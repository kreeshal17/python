file=open("kree.text","w+")
file.write("hiii kree")
file.seek(0)
print(file.read())
file.close()

