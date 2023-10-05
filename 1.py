def unic(doc):
    txt = open(doc+'.txt', 'r').readlines();
    pool = set();
        
    for i in txt:
        for j in i.split(" "):
            pool.add(j.rstrip())

    return pool;

print(unic('1txt'))
print(unic('2txt'))