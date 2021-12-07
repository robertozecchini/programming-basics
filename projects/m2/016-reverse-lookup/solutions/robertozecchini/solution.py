def reverseLookup(dic, val):
    keys = []
    for k in dic:
        if dic[k] == val:
            keys.append(k)
    return keys

def main():
    d = {}
    d["pippo"] = "cane"
    d["topolino"] = "topo"
    d["pluto"] = "cane"
    print("Personaggi che sono cani: ", reverseLookup(d, "cane"))
    print("Personaggi che sono topi: ", reverseLookup(d, "topo"))
    print("Personaggi che sono leoni: ", reverseLookup(d, "leone"))

if __name__ == "__main__":
    main()