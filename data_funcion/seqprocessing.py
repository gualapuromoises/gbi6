def traductor(secuencia, codones): 
  """
  Función traductor realiza la traducción de nucleótidos a aminoácidos
  input: secuencia de nucleótidos
  output: secuencia de nucleótidos codificantes y secuencia de amino ácidos
  """
  seqc = secuencia[secuencia.find("ATG"):]
  peptido = ""
  for i in range(len(seqc)):
      i *= 3
      codon = seqc[i:i+3]
      if len(codon) < 3: # no reconoce como codon si hay 0,1,2 Nucleotidos
          break
      AmAc = codones[codon] # cambiar por un código
      if AmAc =="_":
        break
      peptido += AmAc  #equivale al append
  return([seqc,peptido])


def gcp(secuencia): 
   """
   gcp realiza el cálculo del porcentaje de contenido de Gs y Cs
   input: secuencia de nucleótidos
   output: porcentaje de gc
   """
   pgc = round(100*(secuencia.count("C") + secuencia.count("G"))/len(secuencia), 2)
   return pgc