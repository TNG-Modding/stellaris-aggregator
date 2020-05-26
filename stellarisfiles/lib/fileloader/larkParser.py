from lark import Lark, Transformer, v_args
import os
from pathlib import Path
from pprint import pprint

class EventTransformer(Transformer):
    def list(self, items):
        return list(items)
    def pair(self, key_value):
        k, v = key_value
        return k, v
    def dict(self, items):
        return dict(items)

def ParseEventFile(eventFilepath):
    eventLarkFilepath = os.path.join(Path(os.path.realpath(__file__)).parent, "events.lark")
    with open(eventLarkFilepath, "r") as eventRules:
        eventParser = Lark(eventRules)
        with open (eventFilepath, "r") as events:
            tree = eventParser.parse(events.read())
            pprint(tree)
            # print("Made the tree")
            # transformedTree = EventTransformer().transform(tree)
            # print("Transformed the tree")
            # pprint(transformedTree)

