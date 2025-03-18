from typing import Set, Iterable, Tuple, Dict, List
from collections import defaultdict

class NaiveBayesClf:
    def __init__(self, k: float = 0.5):
        self.k = k
        self.spam_msgs = 0
        self.ham_msgs = 0
        
        self.tokens: Set[str] = set()
        self.token_spam_counts: Dict[str, int] = defaultdict(int)
        self.token_ham_counts: Dict[str, int] = defaultdict(int)
        