


def ip_data(myfile):
    dic = {}
    for line in myfile:
        line = line.strip()
        if line.startswith("PATA"):
            dic["publication_number"] = line[7:-2]
        if line.startswith("TITL"):
            dic["title"] = line[5:]
        if line.startswith("ABST"):
            dic["abstract"] = line[5:]
    print(dic)


with open("maps 225719.txt", "r", encoding="utf8")as myfile:
    ip_data(myfile)