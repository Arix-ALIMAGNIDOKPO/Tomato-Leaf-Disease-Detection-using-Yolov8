# 🍅 Tomato Plant Disease Prediction Web Platform

Ce projet est une application web pour la détection des maladies courantes des feuilles de tomates. Il utilise le modèle YOLO (You Only Look Once) pour la détection d'objets.

## 🎯 Objectif

L'objectif de ce projet est de fournir une plateforme qui peut prédire avec précision les maladies des plantes de tomates à partir d'images. Cela peut aider les agriculteurs et les jardiniers à diagnostiquer et à traiter leurs plantes de manière plus efficace.

## 📚 Dataset

Le modèle a été formé sur un ensemble de données spécifique comprenant différentes classes de maladies des feuilles de tomates. Vous pouvez trouver le dataset ici.

## 🏷️ Classes du Modèle

Les classes du modèle sont les suivantes :
- Bacterial Spot (Tache bactérienne)
- Early Blight (Alternariose)
- Healthy (Sain)
- Iron Deficiency (Carence en fer)
- Late Blight (Mildiou)
- Leaf Mold (Moisissure des feuilles)
- Leaf Miner (Mineuse)
- Mosaic Virus (Virus mosaïque)
- Septoria (Septoriose)
- Spider Mites (Tétranyques)
- Yellow Leaf Curl Virus (Virus des feuilles jaunes en cuillère de la tomate)

## 🚀 Déploiement

L'application web est déjà déployée et vous pouvez y accéder  via le lien https://tomato-leaf-disease-detection-app.streamlit.app/

Pour déployer l'application en local sur votre ordinateur, suivez les instructions ci-dessous :

1. Clonez le dépôt sur votre machine locale.
2. Installez les dépendances nécessaires en utilisant la commande suivante :
```pip install -r requirements.txt```
3. Lancez l'application en utilisant la commande suivante :
```streamlit run app.py```


