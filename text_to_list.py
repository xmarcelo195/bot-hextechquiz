def importar(q, a):
    with open('qa_limpo.txt', 'r') as f:
        mylist = [line.strip() for line in f]

    for name in mylist:
        x = name.split(';')
        q.append(x[0])
        a.append(x[1].strip())

    return q,a
