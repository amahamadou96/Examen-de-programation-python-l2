def calculer_moyennes(etudiants):
    if len(etudiants) == 0:
        return 0, 0, 0 
    somme = 0
    max_note = etudiants[0][1]
    min_note = etudiants[0][1] 
    for nom, note in etudiants:
        somme += note    
        if note > max_note:
            max_note = note
        if note < min_note:
            min_note = note  
    moyenne = somme / len(etudiants)
    return moyenne, max_note, min_note
def afficher_etudiants(etudiants, titre):
    print("\n" + titre)
    print("==================================")   
    for i, (nom, note) in enumerate(etudiants, 1):
        print(f"{i}. {nom} : {note}/20")
def main():
    etudiants = [
        ('ali', 12),
        ('Fatou', 17),
        ('Moussa', 9),
        ('Awa', 18),
        ('Ibrahima',7),
    ]
    
    print("==================================")
    print("\tGestion des notes d'une classe")
    print("==================================")
    afficher_etudiants(etudiants, "TOUS LES ETUDIANTS")
    moyenne, max_note, min_note = calculer_moyennes(etudiants)
    print("==================================")
    print("\tStatistique")
    print("==================================")
    print(f"Nombre d'etudiants : {len(etudiants)}")
    print(f"Moyenne:{moyenne:.2f}/20")
    print(f"Note max:{max_note}/20")
    print(f"Note min:{min_note}/20")
    admis = [e for e in etudiants if e[1] >= 10]
    ajournes = [e for e in etudiants if e[1] < 10]
    afficher_etudiants(admis, "ADMIS (Note >= 10)")
    afficher_etudiants(ajournes, "AJOURNES (Note < 10)")
    
    taux = (len(admis) / len(etudiants)) * 100
    print("==================================")
    print(f"Taux de reussite : {taux:.1f}%")
    print("==================================")
    print("========================================================") 
    print("\tFIN DU PROGRAMME Gestion des notes d'une classe")
    print("\t*Mahamadou Soumaila Abdoulahic*")
    print("=========================================================") 
if __name__ == "__main__":
    main()