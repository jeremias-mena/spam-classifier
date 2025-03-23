import pandas as pd
import pickle
from spam_classifier import Config, Message, NaiveBayesClf, Utils

df = pd.read_csv(Config.data_cleaned_path)

messages = [Message(text, is_spam) for text, is_spam in zip(df['Message'], df['is_spam'])]

train_msg, test_msg = Utils().split_data(messages, 0.70)

model = NaiveBayesClf(k=0.8)
model.train(train_msg)

with open(Config.train_model_path, "wb") as model_file:
    pickle.dump(model, model_file)