def compter_voyelles(phrase):
    voyelles = "aeiouyAEIOUY"
    compteur = 0  
    for caractere in phrase:
        if caractere in voyelles:
            compteur += 1   
    return compteur
def trouver_mot_plus_long(liste_mots):
    mot_max = ""  
    for mot in liste_mots:
        if len(mot) > len(mot_max):
            mot_max = mot
    return mot_max
def construire_nouvelle_phrase(liste_mots):
    nouveaux_mots = []
    for mot in liste_mots:
        if len(mot) % 2 == 0: 
            nouveaux_mots.append(mot.upper())
        else:  
            nouveaux_mots.append(mot)
    return " ".join(nouveaux_mots)
def main():
    print("=" * 60)
    print("\tAnalyse et transformation de texte")
    print("=" * 60)   
    phrase = input("\nEntrez une phrase : ")
    phrase_minuscule = phrase.lower()
    print(f"\nVotre phrase en minuscule est : {phrase_minuscule}")
    liste_mots = phrase_minuscule.split()
    print("\n" + "-" * 60)
    print("\tRÉSULTATS DE L'ANALYSE")
    print("-" * 60)
    nombre_mots = len(liste_mots)
    print(f"\n1. Nombre total de mots : {nombre_mots}")
    print(f"\n2. Phrase convertie en minuscule :")
    print(f"   => {phrase_minuscule}")
    if nombre_mots > 0:
        mot_long = trouver_mot_plus_long(liste_mots)
        print(f"3. Mot le plus long : '{mot_long}' ({len(mot_long)} caractères)")
    else:
        print("3. Aucun mot trouvé")
    nb_voyelles = compter_voyelles(phrase)
    print(f"4. Nombre total de voyelles : {nb_voyelles}")  
    if nombre_mots > 0:
        nouvelle_phrase = construire_nouvelle_phrase(liste_mots)
        print(f"\n5. Nouvelle phrase transformée :")
        print(f"   (mots de longueur paire en MAJUSCULES)")
        print(f"   => {nouvelle_phrase}")
    
    print("\n" + "=" * 60)
    print("\t dECOUPAGE EN MOTS :")
    print("=" * 60) 
    for i, mot in enumerate(liste_mots, 1):
        longueur = len(mot)
        type_longueur = "paire" if longueur % 2 == 0 else "impaire"
        transformation = mot.upper() if longueur % 2 == 0 else mot
        print(f"{i}. '{mot}' => longueur {longueur} ({type_longueur}) => '{transformation}'")
    
    print("=" * 60)
    print("\tFIN DU PROGRAMME")
    print("=" * 60)
if __name__ == "__main__":
    main()