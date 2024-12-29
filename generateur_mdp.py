import string
import random


def choix_utilisateur_O_N (texte) :
    
    # Définition pour les questions à choix oui ou non ('O' ou 'N')
    # avec retour erreur
    
    while True :
        try :
            choix = input(texte).upper()
            if choix not in ['O','N'] :
                raise ValueError("Vous devez répondre O ou N")
            return choix
        except ValueError as e :
            print(e)



def options_utilisateur() :
    
    #Initialisation des valeurs
    
    lmp = None
    maj = None
    chf = None
    car = None
    
    #Liste des réponses acceptées
    reponse =['O','N']
    
    # Question : Longueur du mot de passe
    while lmp is None :
        
        try :
            lmp = int(input('Longueur du mot de passe entre 6 et 30 caractères : '))
            if lmp < 6 or lmp > 30 :
                raise ValueError("La longueur doit-être comprise entre 6 et 30 caractères")
        except ValueError as e :
            print(e)
            lmp = None
    
    # Question : si l'utilisateur veut des majuscules (avec fonction)       
    maj = choix_utilisateur_O_N('Voulez vous des majuscules ? O/N : ')
    
    # Question : si l'utilisateur veut des chiffres       
    chf = choix_utilisateur_O_N('Voulez vous des chiffres ? O/N : ')
    
    # Question : si l'utilisateur veut des caractères spéciaux        
    car = choix_utilisateur_O_N('Voulez vous des caractères spéciaux ? O/N : ')
    
    # Retourne les valeurs validées        
    return [lmp, maj, chf, car]
 




def generer_mot_de_passe(options=None):

# Fonction pour générer un mot de passe    
    
    
    
    # Définition des caractères
    l_minuscules = string.ascii_lowercase
    l_majuscules = string.ascii_uppercase
    chiffres = string.digits
    carac_speciaux = string.punctuation
    
    
    # Récupération des options utilisateur
    
    if options is None :
        options = options_utilisateur()
    
    
    longueur = options[0]
    
    # Initialisation de la liste des mots de passe
    mot_pass=[]
    # Base minuscules
    caracteres = l_minuscules
    
    # Ajout de majuscules, minuscules, caractères spéciaux selon les choix (O/N) 
    if options[1] == 'O' :
        caracteres += l_majuscules
        mot_pass.append(random.choice(l_majuscules))
    if options[2] == 'O' :
        caracteres += chiffres
        mot_pass.append(random.choice(chiffres))
    if options[3] == 'O' :
        caracteres += carac_speciaux
        mot_pass.append(random.choice(carac_speciaux))
    
    # Mot de passe complété jusqu'à longueur demandée  
    mot_pass += random.choices(caracteres, k= longueur - len(mot_pass))
    
    # Mélange du mot de passe
    random.shuffle(mot_pass)
    
    # Retourne le mot de passe final
    return ''.join(mot_pass)




def generer_plusieurs_mdp():
    
    # Fonction (principal) permettant de demander
    # si l'utilisateur veut plusieurs mots de passe
    
    #initialisation de la liste mot de passe
    mots_de_passe =[]
    
    # Question sur le nombre de mots de passe souhaités
    n= None
    
    while n is None :
        try :
            n = int(input('Combien de mots de passe voulez vous générer ? : '))
            if n <= 0:
                raise ValueError("Le nombre doit-être supérieur à 0.")
            
            
        except ValueError as e:
            print(e)
            n=None
    
    # Condition si le nombre est 1 
    if n == 1 :
        mots_de_passe.append(generer_mot_de_passe())
    
    # Condition si le nombre est supérieur à 1
    if n > 1:
        
      # Question si l'utilisateur souhaite conserver les mêmes options pour tout les mots de passe  
        meme = choix_utilisateur_O_N('Voulez vous les mêmes caractéristiques (O/N) : ')
        if meme == 'O':
            options = options_utilisateur()
            for _ in range(n):
                mots_de_passe.append(generer_mot_de_passe(options))
        else:
            for _ in range(n):
                mots_de_passe.append(generer_mot_de_passe())
    
        
    # affichage des mots de passe générés avec enumerate commençant à ,1
    for i, mdp in enumerate(mots_de_passe,1):
        print(f"{i}. {mdp}")
    
    # Question si l'utilisateur veut enregistrer sur un fichier .txt
    enr = choix_utilisateur_O_N('\nVoulez-vous enregistrer ces mots de passe dans un fichier texte ? (O/N) : ')
            
    if enr == 'O' :
        with open('mots_de_passe.txt','w',encoding='utf-8') as F:
            for mdp in mots_de_passe :
                F.write(mdp + '\n')
        print(f"{len(mots_de_passe)} mots de passe ont été enregistrés avec succès.")
        
       
        
    
 

    
    
    
  
        
            
                
                
