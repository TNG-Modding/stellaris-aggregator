from lark import Lark, Transformer, v_args
import os
from pathlib import Path
from pprint import pprint

def getValueArgs(args):
    values = []
    i = 2
    while i < len(args):
        values.append(args[i])
        i = i + 1      
    return values

def turnIntoDictionary(value):
    if isinstance(value, tuple):
        definition = {}
        definition[value[0]] = value[1]
        return definition
    return value
    
class EventTransformer(Transformer):
    
    def define(self, args):
        values = getValueArgs(args)
        if len(values) == 1:
            return args[0], turnIntoDictionary(values[0])
        else:
            definition = {}
            for value in values:
                definition[value[0]] = turnIntoDictionary(value[1])
            return args[0], definition

    def VAR_STR(self, args):
        return str(args).strip('\"')
    def MAGIC_VALUES(self, args):
        return str(args).strip('\"')
    def DOT_STR(self, args):
        return str(args).strip('\"')
    def STRING(self, args):
        return str(args).strip('\"')
    def set_planet_flag(self, args):
        return str(args).strip('\"')
    def start (self, args):
        definition = {}
        for arg in args:
            definition[arg[0]] = arg[1]
        return definition
    def POSS_SYMB(self, args):
        return args[0]

def ParseEventFile(eventFilepath):
    eventLarkFilepath = os.path.join(Path(os.path.realpath(__file__)).parent, "events.lark")
    with open(eventLarkFilepath, "r") as eventRules:
        eventParser = Lark(eventRules)
        with open (eventFilepath, "r") as events:
            tree = eventParser.parse(events.read())
            parsedTree = EventTransformer().transform(tree)
            print(parsedTree)
            return parsedTree
            

