from typing import Iterable, List
from collections import namedtuple
from app.base import Instance, entropy

class Rule(list):
    def __init__(self, l):
        super().__init__(l)
        self.prediction = None

    def can_predict(self, x: Instance):
        for idx, value in enumerate(self):
            if value != x[idx] and value is not None:
                return False
        return True

    def predict(self, x: Instance):
        return self.prediction if self.can_predict(x) else None
    
    def __hash__(self):
        return tuple(self).__hash__()

Predicate = namedtuple("Predicate", "name num_arguments")

class Literal(object):
    def __init__(self, predicate: Predicate, variables:List[str]):
        super().__init__()
        self.predicate = predicate
        self.variables = variables


def get_performance(rule: Rule, instances: Iterable[Instance]):
    match_examples = [i for i in instances if rule.can_predict(i)]
    return -entropy(match_examples, lambda e: e[Instance.target_attribute_idx])
