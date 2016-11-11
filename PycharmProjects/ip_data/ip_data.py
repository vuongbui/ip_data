


def parse_patent_data_file(myfile):
    dic = {}
    for line in myfile:
        line = line.strip()
        if line.startswith("PATA"):
            dic["publication_number"] = line[7:-2]
        if line.startswith("TITL"):
            dic["title"] = line[5:]
        if line.startswith("ABST"):
            dic["abstract"] = line[5:]

    return dic


if __name__ == '__main__':
    #set the location of the target input
    target_file = "C:\PythonApps\VuongsWork\maps 225719.txt"

    #open the file
    myfile = open(target_file, "r", encoding="utf8")

    #run the function we defined above, save 'dic' to the variable parsed_data
    parsed_data = parse_patent_data_file(myfile)

    #close the file, not necessary for small programs but a good habit to get into.
    myfile.close()

    #prints results
    print(parsed_data)