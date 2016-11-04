data = input("Enter your file name: ")

try:
    file = open(data + ".txt", "r", encoding="utf8") #name: maps 225719.txt
except:
    print("There is no such file", data)
def ip_data():
    dic = {}
    for line in file:
        line = line.strip()
        if line.startswith("PATA"):
            dic["publication_number"] = line[7:-2]
        if line.startswith("TITL"):
            dic["title"] = line[5:]
        if line.startswith("ABST"):
            dic["abstract"] = line[5:]
    print (dic)
ip_data()