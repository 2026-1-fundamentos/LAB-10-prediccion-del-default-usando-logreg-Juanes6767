# flake8: noqa: E501
#
# En este dataset se desea pronosticar el default (pago) del cliente el próximo
# mes a partir de 23 variables explicativas.
#
#   LIMIT_BAL: Monto del credito otorgado. Incluye el credito individual y el
#              credito familiar (suplementario).
#         SEX: Genero (1=male; 2=female).
#   EDUCATION: Educacion (0=N/A; 1=graduate school; 2=university; 3=high school; 4=others).
#    MARRIAGE: Estado civil (0=N/A; 1=married; 2=single; 3=others).
#         AGE: Edad (years).
#       PAY_0: Historia de pagos pasados. Estado del pago en septiembre, 2005.
#       PAY_2: Historia de pagos pasados. Estado del pago en agosto, 2005.
#       PAY_3: Historia de pagos pasados. Estado del pago en julio, 2005.
#       PAY_4: Historia de pagos pasados. Estado del pago en junio, 2005.
#       PAY_5: Historia de pagos pasados. Estado del pago en mayo, 2005.
#       PAY_6: Historia de pagos pasados. Estado del pago en abril, 2005.
#   BILL_AMT1: Historia de pagos pasados. Monto a pagar en septiembre, 2005.
#   BILL_AMT2: Historia de pagos pasados. Monto a pagar en agosto, 2005.
#   BILL_AMT3: Historia de pagos pasados. Monto a pagar en julio, 2005.
#   BILL_AMT4: Historia de pagos pasados. Monto a pagar en junio, 2005.
#   BILL_AMT5: Historia de pagos pasados. Monto a pagar en mayo, 2005.
#   BILL_AMT6: Historia de pagos pasados. Monto a pagar en abril, 2005.
#    PAY_AMT1: Historia de pagos pasados. Monto pagado en septiembre, 2005.
#    PAY_AMT2: Historia de pagos pasados. Monto pagado en agosto, 2005.
#    PAY_AMT3: Historia de pagos pasados. Monto pagado en julio, 2005.
#    PAY_AMT4: Historia de pagos pasados. Monto pagado en junio, 2005.
#    PAY_AMT5: Historia de pagos pasados. Monto pagado en mayo, 2005.
#    PAY_AMT6: Historia de pagos pasados. Monto pagado en abril, 2005.
#
# La variable "default payment next month" corresponde a la variable objetivo.
#
# El dataset ya se encuentra dividido en conjuntos de entrenamiento y prueba
# en la carpeta "files/input/".
#
# Los pasos que debe seguir para la construcción de un modelo de
# clasificación están descritos a continuación.
#
#
# Paso 1.
# Realice la limpieza de los datasets:
# - Renombre la columna "default payment next month" a "default".
# - Remueva la columna "ID".
# - Elimine los registros con informacion no disponible.
# - Para la columna EDUCATION, valores > 4 indican niveles superiores
#   de educación, agrupe estos valores en la categoría "others".
#
# Renombre la columna "default payment next month" a "default"
# y remueva la columna "ID".
#
#
# Paso 2.
# Divida los datasets en x_train, y_train, x_test, y_test.
#
#
# Paso 3.
# Cree un pipeline para el modelo de clasificación. Este pipeline debe
# contener las siguientes capas:
# - Transforma las variables categoricas usando el método
#   one-hot-encoding.
# - Escala las demas variables al intervalo [0, 1].
# - Selecciona las K mejores caracteristicas.
# - Ajusta un modelo de regresion logistica.
#
#
# Paso 4.
# Optimice los hiperparametros del pipeline usando validación cruzada.
# Use 10 splits para la validación cruzada. Use la función de precision
# balanceada para medir la precisión del modelo.
#
#
# Paso 5.
# Guarde el modelo (comprimido con gzip) como "files/models/model.pkl.gz".
# Recuerde que es posible guardar el modelo comprimido usanzo la libreria gzip.
#
#
# Paso 6.
# Calcule las metricas de precision, precision balanceada, recall,
# y f1-score para los conjuntos de entrenamiento y prueba.
# Guardelas en el archivo files/output/metrics.json. Cada fila
# del archivo es un diccionario con las metricas de un modelo.
# Este diccionario tiene un campo para indicar si es el conjunto
# de entrenamiento o prueba. Por ejemplo:
#
# {'type': 'metrics', 'dataset': 'train', 'precision': 0.8, 'balanced_accuracy': 0.7, 'recall': 0.9, 'f1_score': 0.85}
# {'type': 'metrics', 'dataset': 'test', 'precision': 0.7, 'balanced_accuracy': 0.6, 'recall': 0.8, 'f1_score': 0.75}
#
#
# Paso 7.
# Calcule las matrices de confusion para los conjuntos de entrenamiento y
# prueba. Guardelas en el archivo files/output/metrics.json. Cada fila
# del archivo es un diccionario con las metricas de un modelo.
# de entrenamiento o prueba. Por ejemplo:
#
# {'type': 'cm_matrix', 'dataset': 'train', 'true_0': {"predicted_0": 15562, "predicte_1": 666}, 'true_1': {"predicted_0": 3333, "predicted_1": 1444}}
# {'type': 'cm_matrix', 'dataset': 'test', 'true_0': {"predicted_0": 15562, "predicte_1": 650}, 'true_1': {"predicted_0": 2490, "predicted_1": 1420}}
#
# flake8: noqa: E501
#
# En este dataset se desea pronosticar el default (pago) del cliente el próximo
# mes a partir de 23 variables explicativas.
#
#   LIMIT_BAL: Monto del credito otorgado. Incluye el credito individual y el
#              credito familiar (suplementario).
#         SEX: Genero (1=male; 2=female).
#   EDUCATION: Educacion (0=N/A; 1=graduate school; 2=university; 3=high school; 4=others).
#    MARRIAGE: Estado civil (0=N/A; 1=married; 2=single; 3=others).
#         AGE: Edad (years).
#       PAY_0: Historia de pagos pasados. Estado del pago en septiembre, 2005.
#       PAY_2: Historia de pagos pasados. Estado del pago en agosto, 2005.
#       PAY_3: Historia de pagos pasados. Estado del pago en julio, 2005.
#       PAY_4: Historia de pagos pasados. Estado del pago en junio, 2005.
#       PAY_5: Historia de pagos pasados. Estado del pago en mayo, 2005.
#       PAY_6: Historia de pagos pasados. Estado del pago en abril, 2005.
#   BILL_AMT1: Historia de pagos pasados. Monto a pagar en septiembre, 2005.
#   BILL_AMT2: Historia de pagos pasados. Monto a pagar en agosto, 2005.
#   BILL_AMT3: Historia de pagos pasados. Monto a pagar en julio, 2005.
#   BILL_AMT4: Historia de pagos pasados. Monto a pagar en junio, 2005.
#   BILL_AMT5: Historia de pagos pasados. Monto a pagar en mayo, 2005.
#   BILL_AMT6: Historia de pagos pasados. Monto a pagar en abril, 2005.
#    PAY_AMT1: Historia de pagos pasados. Monto pagado en septiembre, 2005.
#    PAY_AMT2: Historia de pagos pasados. Monto pagado en agosto, 2005.
#    PAY_AMT3: Historia de pagos pasados. Monto pagado en julio, 2005.
#    PAY_AMT4: Historia de pagos pasados. Monto pagado en junio, 2005.
#    PAY_AMT5: Historia de pagos pasados. Monto pagado en mayo, 2005.
#    PAY_AMT6: Historia de pagos pasados. Monto pagado en abril, 2005.
#
# La variable "default payment next month" corresponde a la variable objetivo.
#
# El dataset ya se encuentra dividido en conjuntos de entrenamiento y prueba
# en la carpeta "files/input/".
#
# Los pasos que debe seguir para la construcción de un modelo de
# clasificación están descritos a continuación.
#
#
# Paso 1.
# Realice la limpieza de los datasets:
# - Renombre la columna "default payment next month" a "default".
# - Remueva la columna "ID".
# - Elimine los registros con informacion no disponible.
# - Para la columna EDUCATION, valores > 4 indican niveles superiores
#   de educación, agrupe estos valores en la categoría "others".
# - Renombre la columna "default payment next month" a "default"
# - Remueva la columna "ID".
#
#
# Paso 2.
# Divida los datasets en x_train, y_train, x_test, y_test.
#
#
# Paso 3.
# Cree un pipeline para el modelo de clasificación. Este pipeline debe
# contener las siguientes capas:
# - Transforma las variables categoricas usando el método
#   one-hot-encoding.
# - Descompone la matriz de entrada usando componentes principales.
#   El pca usa todas las componentes.
# - Escala la matriz de entrada al intervalo [0, 1].
# - Selecciona las K columnas mas relevantes de la matrix de entrada.
# - Ajusta una red neuronal tipo MLP.
#
#
# Paso 4.
# Optimice los hiperparametros del pipeline usando validación cruzada.
# Use 10 splits para la validación cruzada. Use la función de precision
# balanceada para medir la precisión del modelo.
#
#
# Paso 5.
# Guarde el modelo (comprimido con gzip) como "files/models/model.pkl.gz".
# Recuerde que es posible guardar el modelo comprimido usanzo la libreria gzip.
#
#
# Paso 6.
# Calcule las metricas de precision, precision balanceada, recall,
# y f1-score para los conjuntos de entrenamiento y prueba.
# Guardelas en el archivo files/output/metrics.json. Cada fila
# del archivo es un diccionario con las metricas de un modelo.
# Este diccionario tiene un campo para indicar si es el conjunto
# de entrenamiento o prueba. Por ejemplo:
#
# {'dataset': 'train', 'precision': 0.8, 'balanced_accuracy': 0.7, 'recall': 0.9, 'f1_score': 0.85}
# {'dataset': 'test', 'precision': 0.7, 'balanced_accuracy': 0.6, 'recall': 0.8, 'f1_score': 0.75}
#
#
# Paso 7.
# Calcule las matrices de confusion para los conjuntos de entrenamiento y
# prueba. Guardelas en el archivo files/output/metrics.json. Cada fila
# del archivo es un diccionario con las metricas de un modelo.
# de entrenamiento o prueba. Por ejemplo:
#
# {'type': 'cm_matrix', 'dataset': 'train', 'true_0': {"predicted_0": 15562, "predicte_1": 666}, 'true_1': {"predicted_0": 3333, "predicted_1": 1444}}
# {'type': 'cm_matrix', 'dataset': 'test', 'true_0': {"predicted_0": 15562, "predicte_1": 650}, 'true_1': {"predicted_0": 2490, "predicted_1": 1420}}
#

# flake8: noqa: E501
import os
import gzip
import json
import pickle
import pandas as pd
import numpy as np

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder,MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import (
    precision_score,
    balanced_accuracy_score,
    recall_score,
    f1_score,
    confusion_matrix,
)

# ---------------------------------------------------------------------------
# Paso 1 – Limpieza
# ---------------------------------------------------------------------------
def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = df.rename(columns={"default payment next month": "default"})
    
    if "ID" in df.columns:
        df = df.drop(columns=["ID"])
    
    # EDUCATION: valores > 4 → 4 (others)
    df["EDUCATION"] = df["EDUCATION"].apply(lambda x: 4 if x > 4 else x)
    
    # Eliminar registros con información no disponible (0)
    df = df.loc[df["EDUCATION"] != 0]
    df = df.loc[df["MARRIAGE"] != 0]
    
    df = df.dropna()
    return df


# ---------------------------------------------------------------------------
# Cargar los conjuntos ya divididos
# ---------------------------------------------------------------------------
def load_data():
    train_path = "files/input/train_data.csv.zip"
    test_path  = "files/input/test_data.csv.zip"

    train = pd.read_csv(train_path, compression="zip")
    test  = pd.read_csv(test_path,  compression="zip")

    train = clean_dataset(train)
    test  = clean_dataset(test)

    x_train = train.drop(columns=["default"])
    y_train = train["default"]
    x_test  = test.drop(columns=["default"])
    y_test  = test["default"]

    return x_train, y_train, x_test, y_test


# ---------------------------------------------------------------------------
# Paso 3 – Pipeline
#   - Variables categóricas → One-Hot Encoding
#   - Variables NO categóricas → pasan sin cambios (remainder="passthrough")
# ---------------------------------------------------------------------------
def make_pipeline(train):
    # Únicas variables categóricas del dataset
    categorical_features = ["SEX", "EDUCATION", "MARRIAGE"]

    numerical_features= [col for col in train.columns if col not in categorical_features ]

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "categorical",
                OneHotEncoder(handle_unknown="ignore", sparse_output=False),
                categorical_features,
            ), 
            (
        "numerical_preproc",
        Pipeline([
            ("scaler", MinMaxScaler()),
        ]),
        numerical_features,
    )           
           
# - Selecciona las K columnas mas relevantes de la matrix de entrada.
        ],
        remainder="passthrough",   # ← todas las variables NO categóricas
    )

    pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("SelectKBest", SelectKBest(score_func=f_regression)),
            ("logistic",LogisticRegression(),),
        ]
    )
    return pipeline


# ---------------------------------------------------------------------------
# Paso 4 – Optimización de hiperparámetros (10-fold CV + balanced_accuracy)
# ---------------------------------------------------------------------------
def optimize_hyperparameters(pipeline, x_train, y_train):
    param_grid = {
    # Mantiene la selección de características de tu Pipeline
    "SelectKBest__k": range(1, 15), 
    
    # Hiperparámetros específicos para Regresión Logística
    "logistic__C": [0.01, 0.1, 1.0, 10.0],                  # Inverso de la fuerza de regularización
    "logistic__penalty": ["l1", "l2"],                       # Tipo de penalización (Lasso o Ridge)
    "logistic__solver": ["liblinear", "saga"]                # Solvers compatibles con l1 y l2
}

    grid_search = GridSearchCV(
        estimator=pipeline,
        param_grid=param_grid,
        cv=10,
        scoring="balanced_accuracy",
        n_jobs=-1,
        verbose=1,
        refit=True,
    )

    grid_search.fit(x_train, y_train)

    print("Mejor balanced accuracy (CV):", round(grid_search.best_score_, 4))
    print("Mejores hiperparámetros:", grid_search.best_params_)
    print("Score train:", round(grid_search.score(x_train, y_train), 4))
    print("Score test :", round(grid_search.score(x_test, y_test), 4))

    return grid_search


# ---------------------------------------------------------------------------
# Paso 5 – Guardar el modelo comprimido
# ---------------------------------------------------------------------------
def save_model(model, path="files/models/model.pkl.gz"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with gzip.open(path, "wb") as f:
        pickle.dump(model, f)
    print(f"Modelo guardado en {path}")


# ---------------------------------------------------------------------------
# Paso 6 y 7 – Métricas + matrices de confusión
# ---------------------------------------------------------------------------
def compute_and_save_metrics(model, x_train, y_train, x_test, y_test,
                             path="files/output/metrics.json"):
    os.makedirs(os.path.dirname(path), exist_ok=True)

    metrics = []

    # ---------- 1. Métricas de train y test ----------
    for dataset_name, X, y in [
        ("train", x_train, y_train),
        ("test",  x_test,  y_test),
    ]:
        y_pred = model.predict(X)

        metrics.append(
            {
                "type": "metrics",
                "dataset": dataset_name,
                "precision": float(precision_score(y, y_pred, zero_division=0)),
                "balanced_accuracy": float(balanced_accuracy_score(y, y_pred)),
                "recall": float(recall_score(y, y_pred, zero_division=0)),
                "f1_score": float(f1_score(y, y_pred, zero_division=0)),
            }
        )

    # ---------- 2. Matrices de confusión de train y test ----------
    for dataset_name, X, y in [
        ("train", x_train, y_train),
        ("test",  x_test,  y_test),
    ]:
        y_pred = model.predict(X)
        cm = confusion_matrix(y, y_pred)

        metrics.append(
            {
                "type": "cm_matrix",
                "dataset": dataset_name,
                "true_0": {
                    "predicted_0": int(cm[0, 0]),
                    "predicted_1": int(cm[0, 1]),
                },
                "true_1": {
                    "predicted_0": int(cm[1, 0]),
                    "predicted_1": int(cm[1, 1]),
                },
            }
        )

    # Guardar (una línea por diccionario)
    with open(path, "w", encoding="utf-8") as f:
        for m in metrics:
            f.write(json.dumps(m) + "\n")

    print(f"Métricas guardadas en {path}")
    return metrics


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    x_train, y_train, x_test, y_test = load_data()
              
    pipeline = make_pipeline(x_train)
    grid_search = optimize_hyperparameters(pipeline, x_train, y_train)

    # Guardar el GridSearchCV completo (no el best_estimator_)
    save_model(grid_search)

    # Las predicciones se hacen igual
    compute_and_save_metrics(grid_search, x_train, y_train, x_test, y_test)
