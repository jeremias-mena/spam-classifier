from typing import Set, NamedTuple, List, TypeVar, Tuple
import re
import random

class Utils:
    def __init__(self):
        pass

    def tokenize(self, text:str) -> Set[str]:
        text = text.lower()
        all_words = re.findall("[a-z0-9']+", text)
        return set(all_words)
    
    def label_spam_column(self, value:str) -> bool:
        if value.lower() == 'spam': 
            return True
        else:
            return False
    
    def split_data(self, data: List[TypeVar], prob:float) -> Tuple[List[TypeVar], List[TypeVar]]:
        data = data[:]
        random.shuffle(data)
        cut = int(len(data) * prob)
        return data[:cut], data[cut:]

class Message(NamedTuple):
    text: str
    is_spam: bool

