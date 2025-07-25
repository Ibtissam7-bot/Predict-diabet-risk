import streamlit as st
import joblib
import numpy as np

# Charger le modèle
model=joblib.load('meilleur_modele.pkl')

# Titre
st.title("🧪 Prédiction du Risque de Diabète")
st.write("Entrez les données cliniques du patient pour prédire le risque de diabète.")

# Champs de saisie
glucose = st.number_input("Glycémie (Glucose)", min_value=0.0, max_value=300.0, step=1.0)
bmi = st.number_input("Indice de Masse Corporelle (BMI)", min_value=0.0, max_value=70.0, step=0.1)
age = st.number_input("Âge", min_value=1, max_value=120, step=1)
dpf = st.number_input("Fonction de prédisposition génétique (Diabetes Pedigree Function)", min_value=0.0, max_value=3.0, step=0.01)

# Bouton de prédiction
if st.button("Prédire"):
    # Créer un tableau avec les inputs
    input_data = np.array([[glucose, bmi, age, dpf]])
    
    # Faire la prédiction
    prediction = model.predict(input_data)[0]

    # Affichage du résultat
    if prediction == 0:
        st.error("⚠️ Risque ÉLEVÉ de diabète")
    else:
        st.success("✅ Faible risque de diabète")
