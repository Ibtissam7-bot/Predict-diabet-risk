#  Prédiction du Risque de Diabète par Machine Learning
       Réalisée par :Sannaky IBTISSAM
                     Naoui IKRAM

##  Contexte du projet
Ce projet a été développé dans le cadre d’un laboratoire biomédical pour prédire si un patient présente un **risque élevé de développer le diabète** à partir de données cliniques.  
Il combine des approches de **clustering non supervisé** et de **classification supervisée**, avec des techniques de **prétraitement avancé**, **réduction de dimension**, **validation croisée**, et **optimisation des modèles**.



##  Structure du projet

.
├── data/
│ └── diabetes.csv # Données sources
├── notebooks/
│ └── prediction_diabete.ipynb
├── models/
│ └── final_model.pkl # Meilleur modèle sauvegardé
├── src/
├── README.md 





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
- Possibilité de le déployer dans une API Flask/FastAPI



