# dechiffrement_cesar
Déchiffrement d'un chiffrement additif (chiffrement de César) par analyse fréquentielle 

Ce programme applique l'analyse frequentielle pour casser un chiffrement additif

**L'analyse fréquentielle** est basée sur le fait que, dans chaque langue, certaines lettres ou combinaisons de lettres apparaissent avec une certaine fréquence. Par exemple, en français, le e est la lettre la plus utilisée, suivie du a et du s. Inversement, le w est peu utilisé.
Une deuxième condition nécessaire pour appliquer cette technique est la longueur du cryptogramme. En effet, un texte trop court ne reflète pas obligatoirement la répartition générale des fréquences des lettres. De plus, si la clé est de la même longueur que le message, il ne pourra y avoir de répétition de lettre et l'analyse fréquentielle deviendra impossible.

Decryption of an additive cipher (Caesar cipher) by frequency analysis

This program applies frequency analysis to break additive encryption

**Frequency analysis** is based on the fact that in each language certain letters or combinations of letters appear with a certain frequency. For example, in French, the e is the most used letter, followed by a and s. Conversely, the w is little used.
A second condition necessary for applying this technique is the length of the cryptogram. In fact, a text that is too short does not necessarily reflect the general distribution of letter frequencies. In addition, if the key is the same length as the message, there will be no letter repetition and frequency analysis will become impossible.

# Tools
- Environment : Python 3.6 and higher
# Run 
````python3 dechiffrement_cesar.py "Salut je suis un texte a dechiffrer je suis etudiant" 5```` 
