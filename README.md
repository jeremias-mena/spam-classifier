# 📧 Spam Classifier

Este repositorio contiene un clasificador de spam basado en Naive Bayes, diseñado para detectar mensajes no deseados en textos de correos electrónicos.

## 📌 Características

* Preprocesamiento de datos con técnicas de NLP.

* Tokenización de texto personalizada.

* Implementación de un clasificador Naive Bayes desde cero.

* Entrenamiento y evaluación del modelo con métricas para un modelo de clasificación.

## 📂 Estructura del Proyecto

📁 spam-classifier
├── 📂 spam_classifier   
    ├── 📂 data              
    │   ├── 📂 raw
    │   ├── 📂 processed
    │   ├── 📂 cleaned
    ├── 📂 model
    ├── 📂 notebooks
    ├── 📂 src                         
        ├── train.py             
        ├── predict.py
    ├── __init__.py             
    ├── config.py
    ├── data_manipulation.py
    ├── model.py
    ├── utils.py            
├── requirements.txt
├── .gitignore      
├── README.md
├── setup.py            

## 🚀 Instalación

Clona el repositorio:

> git clone https://github.com/tu-usuario/spam-classifier.git
> cd spam-classifier

Instala las dependencias para poder utilizar este repositorio:

> pip install -r requirements.txt

## 🏃 Uso

Entrenar el modelo

> python train.py

Realizar predicciones

> python predict.py "Tu mensaje aquí"

## 📊 Evaluación del Modelo

El modelo se entrena con datos de correos electrónicos, separando el conjunto en entrenamiento y prueba. Se evalúa con métricas como precisión, recall y F1-score.


## 📫 Contacto

Si tienes preguntas o sugerencias, no dudes en abrir un issue o contactarme en menajeremias08@gmail.com.

