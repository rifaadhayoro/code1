class Etudiant:
    def __init__(self, nom, numero_identification):
        self.nom = nom
        self.numero_identification = numero_identification
        self.notes = []

    def ajouter_note (self, note):
        if isinstance(note, (int, float)) and 0 <= note <= 20:
            self.notes.append(note)
        else:
            raise ValueError("La note doit être un nombre entre 0 et 20")

    def calculer_moyenne(self):
        if self.notes:
            return sum(self.notes) / len(self.notes)
        return 0.0

    def afficher_moyenne(self):
        moyenne = self.calculer_moyenne()
        print(f"La moyenne des notes de {self.nom} (ID: {self.numero_identification}) est : {moyenne:.2f}")

def ajouter_nouvel_etudiant():
    nom = input("Entrez le nom de l'étudiant : ")
    numero_identification = input("Entrez le numéro d'identification de l'étudiant : ")
    if isinstance(nom, str) and isinstance(numero_identification, str):
        return Etudiant(nom, numero_identification)
    else:
        raise ValueError("Le nom et le numéro d'identification doivent être des chaînes de caractères")

def saisir_notes(etudiant):
    while True:
        note = input("Entrez une note (ou 'q' pour quitter) : ")
        if note.lower() == 'q':
            break
        try:
            note = float(note)
            etudiant.ajouter_note(note)
        except ValueError:
            print("Veuillez entrer un nombre valide entre 0 et 20.")

# Affichage
try:
    etudiant = ajouter_nouvel_etudiant()
    saisir_notes(etudiant)
    etudiant.afficher_moyenne()
except ValueError as e:
    print(e)
