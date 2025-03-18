from pathlib import Path

class Config:
    data_dir_raw = Path(__file__).resolve().parent/'data/raw'
    data_dir_processed = Path(__file__).resolve().parent/'data/processed'
    data_dir_cleaned = Path(__file__).resolve().parent/'data/cleaned'

    data_raw_path = data_dir_raw/'spam_emails.csv'
    data_processed_path = data_dir_processed/'spam_emails_processed.csv'
    data_cleaned_path = data_dir_cleaned/'spam_emails_cleaned.csv'
