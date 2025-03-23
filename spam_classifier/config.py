from pathlib import Path

class Config:
    data_dir_raw = Path(__file__).resolve().parent/'data/raw'
    data_dir_processed = Path(__file__).resolve().parent/'data/processed'
    data_dir_cleaned = Path(__file__).resolve().parent/'data/cleaned'
    dir_train_model = Path(__file__).resolve().parent/'model'

    data_raw_path = data_dir_raw/'spam_emails.csv'
    data_processed_path = data_dir_processed/'spam_emails_processed.csv'
    data_cleaned_path = data_dir_cleaned/'spam_emails_cleaned.csv'

    train_model_path = dir_train_model/'spam_classifier_NB.pkl'

