import pickle
import sys
from spam_classifier import Config

with open(Config.train_model_path, "rb") as model_file:
    model = pickle.load(model_file)

def predict_email(message: str) -> str:
    probability = model.predict(message)
    if probability > 0.5:
        return "Spam"
    else:
        return "Ham"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python predict.py 'Tu mensaje aqui'")
        sys.exit(1)
    
    message = sys.argv[1]
    result = predict_email(message)
    print(f"Resultado de la predicción: {result}")
