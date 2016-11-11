


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

    target_file = "maps 225719.txt"

    with open(target_file, "r", encoding="utf8") as myfile:
        parsed_data = parse_patent_data_file(myfile)