name = input("Choisis ton prénom pour cette aventure: ")
print("Bienvenue", name, "dans cette aventure!")

answer = input(f"Ops, {name}, tu ne peux plus avancer tout droit. Mais ne t'inquiète pas, tu peux continuer à gacuhe ou à droite! Dans quelle direction veux-tu aller? ").lower()
    

if answer == "gauche":
    answer = input(f"Super! {name}, la rivière UNGABUNGA se trouve juste devant toi. Tu peux la contourner ou la traverser. Alors, quelle aventure tu va prendre? Contourner ou Traverser: ").lower()
    if answer == "contourner":
        print(f"Tu as marché pendant de nombreuses heures, tu n'as plus de nourriture et d'eau avec toi! Malheuresement, tu vas mourir de faim et déhydratation. :( RIP, {name}!")
        print("T'as perdu!")
    elif answer == "traverser":
        print(f"Tu as essayé de traverser la rivière, mais tu a été mangé par un crocodile! :(  RIP {name}!")
    else:
        print("Ops, tu n'as pas choisit l'une des deux options. T'as perdu!")
        print("T'as perdu!")
        
elif answer == "droite":
    answer = input(f"{name}, t'es arrivé devant un pont, qui n'a pas l'air stable. Est-ce que tu as le courage de traverser le pont ou retourner en arrière. Ecris traverser ou retourner pour choisir ton aventure: ").lower()
    if answer == "retourner":
        print("Opsi!")
        print("T'as perdu!")
    elif answer == "traverser":
        answer = input("Tu as traversé le pont et tu aS rencontré un parfait inconnu. Tu as le courage de parler avec cette personne? Oui/Non: ").lower()
        if answer == "oui":
            print("Tu as parlé avec l'inconnu et il t'a donné d'or! T'as gagné la partie!!! HOURRAAAA")
        elif answer == "non":
            print("Tu ignores l'inconnu! Il est en colère! ")
            print("T'as perdu!")  
        else:
            print("Ops, tu n'as pas choisit l'une des deux options. T'as perdu!")
            print("T'as perdu!")  
           
    else:
        print("Ops, tu n'as pas choisit l'une des deux options. T'as perdu!")
        print("T'as perdu!")
        
else: 
    print("Il faut choisir: gauche ou droite pour continuer! You lost!")
   

print("Merci d'avoir fait cette aventure", name)