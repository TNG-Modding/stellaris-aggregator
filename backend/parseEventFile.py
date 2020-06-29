# import sys
# from lark import Lark, Transformer, v_args
# import os
# from pathlib import Path

# def getValueArgs(args):
#     values = []
#     i = 2
#     while i < len(args):
#         values.append(args[i])
#         i = i + 1      
#     return values

# def turnIntoDictionary(value):
#     if isinstance(value, tuple):
#         definition = {}
#         definition[value[0]] = value[1]
#         return definition
#     return value

# class EventTransformer(Transformer):
#     def define(self, args):
#         values = getValueArgs(args)
#         if len(values) == 1:
#             return args[0], values[0]
#         else:
#             definitions = []
#             for value in values:
#                 definitions.append((value[0], value[1]))
#             return args[0], definitions

#     def VAR_STR(self, args):
#         return str(args).strip('\"')
#     def MAGIC_VALUES(self, args):
#         return str(args).strip('\"')
#     def DOT_STR(self, args):
#         return str(args).strip('\"')
#     def STRING(self, args):
#         return str(args).strip('\"')
#     def set_planet_flag(self, args):
#         return str(args).strip('\"')
#     def start (self, args):
#         eventFile = {}
#         eventFile["events"] = []
#         for arg in args:
#             if arg[0] == "namespace":
#                 continue
            
#             eventFile["events"].append(arg)
#         return eventFile
#     def POSS_SYMB(self, args):
#         return args[0]

# def ParseEventFile(eventFilepath):
#     eventLarkFilepath = os.path.join(Path(os.path.realpath(__file__)).parent, "events.lark")
#     with open(eventLarkFilepath, "r") as eventRules:
#         eventParser = Lark(eventRules)
#         with open (eventFilepath, "r") as events:
#             tree = eventParser.parse(events.read())
#             parsedTree = EventTransformer().transform(tree)
#             return parsedTree
            

filepath = sys.argv[1]
# eventJson = ParseEventFile(filepath)
print(sys.argv[1])
sys.stdout.flush()