seq = ("AATTCTATCTTGATATATCGGCGCGCGATCGGA")
def largo(seq):
    """
    largo es una funcion que calcula el numero de caracteres de una secuencia
    input: seq es una secuencia de caracteres 
    output: len_seq es un valor numerico de la cantidad de caracteres
    """
    len_seq = len(seq)
    return(len_seq)

def gc(seq):
    """
    gc es una funcion que calcula el porcentaje de nucleotidos g y c 
    input: con secuencia de nucleotodos
    vars:
        c
        g
        n
    """
    c = seq.count("C")
    g = seq.count("G")
    n = len(seq)
    gc = round(100*(c+g)/n, 3)
    return gc
gc(seq)

def restriccion(seq, enzima):
    """
    Restriccion es una funcion de digestion de secuencias utilizando enzimas
    input: seq, secuencia de nucleotidos.
    enzima: es un fragmento de nucleotidos que indican donde se corta la secuencia.
    var:
    output: 
    Fragmentos: cada uno de los fragmentos digeridos/cortados
    longitud: largo de cada fragmento.
    """
    frags = []
    while seq.find(enzima) != -1:
        ni = seq.find(enzima)
        frag1 = seq[:ni+len(enzima)]
        seq = seq[ni+len(enzima):]
        frags.append([frag1, len(frag1)])
    frags.append([seq, len(seq)])
    return frags
    