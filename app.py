import streamlit as st
import cv2
from PIL import Image
from ultralytics import YOLO

model = YOLO('yolov8n.yaml')
model = YOLO('best.pt')

# Définir les classes
classes = ['Bacterial Spot (Tache bactérienne)', 'Early Blight (Alternariose)', 'Healthy (Sain)', 'Iron Deficiency (Carence en fer)', 'Late Blight (Mildiou)', 'Leaf Mold (Moisissure des feuilles)', 'Leaf Miner (Mineuse)', 'Mosaic Virus (Virus mosaïque)', 'Septoria (Septoriose)', 'Spider Mites (Tétranyques)', 'Yellow Leaf Curl Virus (Virus des feuilles jaunes en cuillère de la tomate)']

st.title("Détection de maladies des feuilles de tomates")
st.markdown("""
Ce projet est une application web pour la détection des maladies courantes des feuilles de tomates. Il utilise le modèle YOLO (You Only Look Once) pour la détection d'objets. Le modèle a été formé sur un ensemble de données spécifique comprenant différentes classes de maladies des feuilles de tomates. Les classes du modèle sont les suivantes :
""" + ', '.join(classes) )

uploaded_file = st.file_uploader("Choisissez une image de feuille de tomate", type=["jpg", "png"])

# Ajouter une section pour l'auteur
st.sidebar.markdown("## Auteur")
st.sidebar.markdown("Nom :  **Arix ALIMAGNIDOKPO**")
st.sidebar.markdown("GitHub : https://github.com/Arix-ALIMAGNIDOKPO")
st.sidebar.markdown("LinkedIn : www.linkedin.com/in/arix-alimagnidokpo-27865a276")
st.sidebar.markdown("## Pour plus d'informations consultez le lien du depot Github ci-dessous :")
st.sidebar.markdown("Repository : https://github.com/Arix-ALIMAGNIDOKPO/Tomato-Leaf-Disease-Dection-using-Yolov8")

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    # Prédire les classes
    results = model(image)
    # View results
    for r in results:
        im_array = r.plot()  # plot a BGR numpy array of predictions
        im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
        im.show()  # show image
        im.save('results.jpg')  # save image
    st.image('results.jpg', caption='Prédiction du model')
    