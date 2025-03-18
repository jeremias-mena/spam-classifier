from pathlib import Path

class Config:
    data_dir_raw = Path(__file__).resolve().parent/'data/raw'
    dara_dir_processed = Path(__file__).resolve().parent/'data/processed'
    data_dir_cleaned = Path(__file__).resolve().parent/'data/cleaned'
