
#ouvrir le document
with open("./document.txt") as doc:
    document = doc.readlines() #lire tous les lignes (les retournes '\n' sont inclus)
    document = [ligne.rsplit("\n")[0] for ligne in document] #supprimer les "\n" du liste


    
def etallonage(mots):
    print(f"le document d'etallonage: {mots}")
    somme=0
    for i in range(len(mots)):
        #filter tous les mots en laissant juste les nombres
        mots[i] = "".join(character for character in mots[i] if character.isdigit())

        #filter tous les nombres en laissant juste les premier et les derniers chiffres
        #rq: cette methode peut retourner plus de 2 chiffres (cas de duplication des chiffres)
        mots[i] = "".join(num for num in mots[i] if num == mots[i][0] or num == mots[i][-1])
        

        #en cas des chiffre dupliquèes on prend seuelement la 1ere et derniere chiffre
        if(len(mots[i])>2):
            mots[i] = mots[i][0]+mots[i][-1]

        #s il'ya seulement une chiffre on la duplique car elle est la premiere et la dernière
        elif (len(mots[i])==1):
            mots[i] *=2

        #s il'ya aucune chiffre on met un 0
        elif(len(mots[i])==0):
            mots[i] = "0"
        
        mots[i] = int(mots[i]) #convertir les strings en des entiers
        somme += mots[i]
    print(f"les valeurs d'etallonage sont: {mots}")
    print(f"la somme de toutes les valeurs d'etallonage est: {somme}")


etallonage(document)