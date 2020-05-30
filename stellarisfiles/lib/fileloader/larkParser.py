from lark import Lark, Transformer, v_args
import os
from pathlib import Path
from pprint import pprint

class EventTransformer(Transformer):
    def define(self, args):
        definition = {}
        items = []

        i = 2
        while i < len(args):
            items.append(args[i])
            i = i + 1            
        
        if args[1] != "=":
            definition["%s%s" % (args[0], args[1])] = items
        else:
            definition[args[0]] = items
        return definition
    def VAR_STR(self, args):
        return str(args)
    def MAGIC_VALUES(self, args):
        return str(args)
    def DOT_STR(self, args):
        return str(args)
    def STRING(self, args):
        return str(args)
    def set_planet_flag(self, args):
        return str(args)
    def start (self, args):
        definition = []
        for arg in args:
            definition.append(arg)
        return definition
    def POSS_SYMB(self, args):
        return args[0]

def ParseEventFile(eventFilepath):
    eventLarkFilepath = os.path.join(Path(os.path.realpath(__file__)).parent, "events.lark")
    with open(eventLarkFilepath, "r") as eventRules:
        eventParser = Lark(eventRules)
        with open (eventFilepath, "r") as events:
            tree = eventParser.parse(events.read())
            # pprint(tree)
            transformedTree = EventTransformer().transform(tree)
            pprint(transformedTree)

