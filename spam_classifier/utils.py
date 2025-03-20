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
    
    def split_data(self, data:List[TypeVar], prob:float) -> Tuple[List[TypeVar], List[TypeVar]]:
        data = data[:]
        random.shuffle(data)
        cut = int(len(data) * prob)
        return data[:cut], data[cut:]
    
    def accuracy(self, tp:int, fp:int, fn:int, tn:int) -> float:
        correct = tp + tn
        total = tp + fp + fn + tn
        return correct / total
    
    def precision(self, tp:int, fp:int) -> float:
        prec = tp / (tp + fp)
        return prec
    
    def recall(self, tp:int, fn:int) -> float:
        rec = tp / (tp + fn)
        return rec
    
    def f1_score(self, tp:int, fp:int, fn:int, tn:int) -> float:
        pre = self.precision(tp, fp)
        rec = self.recall(tp, fn)
        f1 = (2 * pre * rec) / (pre + rec)
        return f1

class Message(NamedTuple):
    text: str
    is_spam: bool

