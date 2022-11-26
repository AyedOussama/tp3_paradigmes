ch=input("saisir une phrase :")
def text_to_index(ch):
  liste=ch.split(" ")
  dic={}
  for i in range(len(liste)):
      if liste[i] not in dic :
        dic[liste[i]]=[i]
      else:
        dic[liste[i]].append(i)
        
  return dic

print(ch)
print(text_to_index(ch))

