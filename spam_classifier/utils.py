from typing import Set, NamedTuple
import re

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

class Message(NamedTuple):
    text: str
    is_spam: bool

