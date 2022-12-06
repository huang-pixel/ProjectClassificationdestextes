-------------------------------------------
Auteurice : Megumi ADACHI & HUANG He
Date : 26 avril 2022

Ce rapport est une description et explication du projet rendu dans le cadre du cours de "Extraction d'informations" du M1 Plurital (INALCO).

--------------------------------------------
--- RANGEMENT DES DONNÉES ------------------

Le répertoire "./projet/" contient 2 dossiers, 1 fichier python, 3 fichiers jupyter notebook, un fichier resume.pdf et 1 fichier README.txt.
Dans le dossier "./data/", les fichiers de source sont rangés. Les résultats sont sauvegardés sous le même dossier. Dans le dossier "./library/", les articles et rapports sont rangés.
Le fichier "train.db" dans "./data/" sert d'échantillons de chaque langue. 

projet
├── ReadMe.txt
├── requirements.txt
├── resume.pef
├── prepare_annotation.py
├── ngram_identification.ipynb
├── data
│   ├── 1-1.txt <- texte source
│   ├── 1-2.txt
│   ├── ...
│   ├── annotation_corpus.csv <- classements de fichier par la langue
│   ├── test.bin <- liste des fichiers test
│   ├── train.bin <- liste des fichiers train
│   ├── train.db <- ngrammes et fréquences de chaque langue
│   ├── train2.db
│   ├── train3.db
└── library
    ├── 01_Language_Identification_from_Text_Using_N-gram_Cumulative Frequency Addition
    ├── 01_recap.pdf
    ├── 02_Language Identification of Short Text Segments with N-gram Models
    ├── 02_recap.pdf
    ├── 03_Automatic Language Identification in Texts: A Surveys.pdf

--------------------------------------------
--- LANCEMENT ET DESCRIPTION DES SCRIPTS ---

--LANCEMENT

Le script python présents dans le dossier "./projet/" devront être lancés via une commande sur le terminal :  "python [nom_du_script.py]".

Il est impératif de placer le terminal (cwd) dans le dossier "./projet/" pour que les programmes se lancent sans encombre.


--DESCRIPTION DU SCRIPT

-*-*-*-*-*-*-*-*
SCRIPT 1 : "prepare_annotation.py"

Annoter des classements de fichiers et créer des fichiers "annotation_corpus.tsv", "train.bin" et "test.bin".

- Exécution -
python prepare_annotation.py

- Résultats -
ex) "annotation_corpus.tsv"
No	language
2-1	ENG
2-10	ENG
2-11	ENG
2-12	ENG

ex) format dictionnaire pour "train.bin" et "test.bin"
{'ENG': ['2-5'...], 'TRK': ['3-1'...]} {'ENG': ['2-14'...], 'TRK': ['3-24'...]}

-> Les résultats sont sauvegardés sous :
./data/annotation_corpus.tsv
./data/train.bin
./data/test.bin

-*-*-*-*-*-*-*-*
SCRIPT 2 : "ngram_identification.ipynb"

1. Lire les textes de train et créer une base de données "train.db" contenant des ngrams et leur fréquences de chaque langue. Cette base de données sert d'échantillon de chaque langue.

-> Le résultat est sauvegardé sous :
./data/train.db

2. Créer un dictionnaire de donnée test et comparer avec le train.

- Résultats -
Precision ENG: 0.0
Precision TRK: 0.0
Precision FRA: 0.0
Recall ENG: 0.0
Recall TRK: 0.0
Recall FRA: 0.0

3. Afficher le heatmap de données.

-*-*-*-*-*-*-*-*
SCRIPT 3 : "filtered_ngram_identification.ipynb"

1. Lire les textes de train et créer une base de données "train.db" contenant des ngrams et leur fréquences de chaque langue après un nettoyage de texte. Cette base de données sert d'échantillon de chaque langue.

-> Le résultat est sauvegardé sous :
./data/train.db

2. Créer un dictionnaire de donnée test et comparer avec le train.

- Résultats -
Precision ENG: 1.0
Precision TRK: 0.0
Precision FRA: 0.25
Recall ENG: 0.2857142857142857
Recall TRK: 0.0
Recall FRA: 0.5714285714285714

3. Afficher le heatmap de données.
-*-*-*-*-*-*-*-*

SCRIPT 4 : "classification_sklearn.ipynb"

1. Récupérer le corpus déjà classifié par des étiquettes

2. Nettoyage chaque texte pour supprimer les symboles

3. Construire un jeu de données 
-> train et test

4. Vectorisation (Bag of words)

5. Prédiction avec classifier

6. Obtenir le résultat

Bayes
------------------------Rapport----------------------
              precision    recall  f1-score   support

         ENG       0.89      1.00      0.94         8
         FRA       1.00      1.00      1.00        10
         TRK       1.00      0.86      0.92         7

    accuracy                           0.96        25
   macro avg       0.96      0.95      0.95        25
weighted avg       0.96      0.96      0.96        25

KNeighbors
------------------------Rapport----------------------
 precision    recall  f1-score   support

         ENG       0.89      1.00      0.94         8
         FRA       1.00      0.90      0.95        10
         TRK       0.86      0.86      0.86         7

    accuracy                           0.92        25
   macro avg       0.92      0.92      0.92        25
weighted avg       0.92      0.92      0.92        25

Decision Tree
------------------------Rapport----------------------
precision    recall  f1-score   support

         ENG       0.89      1.00      0.94         8
         FRA       1.00      0.80      0.89        10
         TRK       0.88      1.00      0.93         7

    accuracy                           0.92        25
   macro avg       0.92      0.93      0.92        25
weighted avg       0.93      0.92      0.92        25