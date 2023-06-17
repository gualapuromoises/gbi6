def largo(seq):
    """
    largo es una función que calcula el número de carcateres de una secuencia
    input: seq es una secuencia de caracteres
    output: len_seq es un valor numérico de la cantidad de caracteres
    """
    len_seq = len(seq)
    return(len_seq)

def gc(seq):
    """
    gc es una función que calcula el procentaje de nucleótidos g y c
    input: seq secuencia de nucleótidos
    vars: 
        c cantidad de citosinas, 
        g cantidad de guaninas, 
        n longitud de la secuencia 
    output: gcp porcentaje de g y c
    """
    c = seq.count("C")
    g = seq.count("G")
    n = len(seq)
    gc = round(100*(c+g)/n, 3)
    return gc

def restriccion(seq, enzima):
    """
    restriccion es una función de digestión de secuencias utilizando enzimas
    input: 
        seq es una secuencia de nucléotidos
        enzima es un fragmento de nucleótidos que indica donde se corta la secuencia
    var: 

    output: 
        fragmentos: cada uno de los fragmentos digeridos/cortados
        longitud: largo de cada fragmento
    """
    frags = []
    while seq.find(enzima) != -1:
        ni = seq.find(enzima)
        frag1 = seq[:ni+len(enzima)]
        seq = seq[ni+len(enzima):]
        frags.append([frag1, len(frag1)])
    frags.append([seq, len(seq)])       
    return (frags)