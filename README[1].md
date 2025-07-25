#  Prédiction du Risque de Diabète par Machine Learning
       Réalisée par :SANNAKY Ibtissam
                     NAOUI Ikram

##  Contexte du projet
Ce projet a été développé dans le cadre d’un laboratoire biomédical pour prédire si un patient présente un **risque élevé de développer le diabète** à partir de données cliniques.  
Il combine des approches de **clustering non supervisé** et de **classification supervisée**, avec des techniques de **prétraitement avancé**, **réduction de dimension**, **validation croisée**, et **optimisation des modèles**.



##  Structure du projet

diabete_prediction_project/

app.py                                  # Application Streamlit

meilleur_modele.pkl                     # Modèle ML final enregistré

dataset-687cf473b3eba683446726.csv      # Jeu de données historique 

README[1].md                            # Documentation du projet 

source_file1.ipynb                      # Notebook principal 

Test1.ipynb                             # Test du modèle 




##  Données utilisées

Le dataset contient les caractéristiques suivantes :

| Colonne                  | Description                                        |
|--------------------------|----------------------------------------------------|
| Glucose                  | Niveau de glycémie                                 |
| BloodPressure            | Pression artérielle                                |
| SkinThickness            | Épaisseur du pli cutané                            |
| Insulin                  | Taux d'insuline                                    |
| BMI                      | Indice de masse corporelle                         |
| DiabetesPedigreeFunction| Risque héréditaire de diabète                       |
| Age                      | Âge du patient                                     |
| Outcome                  | 1 = Diabétique, 0 = Non diabétique                 |
---------------------------------------------------------------------------------

---

##  Étapes du projet

###  Exploration des données (EDA)
- Vérification des types de données
- Détection des valeurs manquantes et aberrantes
- Visualisation des distributions et des corrélations

###  Prétraitement
- Suppression ou imputation des valeurs manquantes
- Suppression des outliers avec IQR ou Z-score
- Normalisation avec `StandardScaler`

###  Clustering
- Utilisation de **K-Means**
- Méthode du coude pour déterminer **k optimal**
- Réduction dimensionnelle avec **PCA**
- Visualisation des clusters
- Étiquetage `risk_category` selon les seuils cliniques

###  Classification supervisée
- Modèles testés : `RandomForest`, `SVM`, `GradientBoosting`, `LogisticRegression`
- Gestion du déséquilibre avec `RandomOverSampler`
- Évaluation : **matrice de confusion**, **f1-score**, **recall**, **precision**
- Validation croisée et **GridSearchCV**

###  Sauvegarde et déploiement
- Sauvegarde du meilleur modèle avec `joblib`

### Test du modèles sur des nouvaux outputs
- Test du modèle sur 'Test1.ipynb'

### Affichage d'une application Streamlit locale qui gère dinamiquement l'application du modèle choisi
- Utiliser l'application Streamlit 'app.py' par la commande *streamlit run app.py*


