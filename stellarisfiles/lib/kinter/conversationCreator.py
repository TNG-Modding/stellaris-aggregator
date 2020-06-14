import uuid

def createConversationForOption(optionLocation, optionId, optionNameLocalization):
    return {
        "optionLocations": [optionLocation],
        "varname": "%s_%s" % (optionId,uuid.uuid1()),
        "name": optionNameLocalization,
        "desc": "TODO: Write description.",
        "ethic": "egalitarian",
        "durationYears": 25
    }

def createConversationLocation (fileName, eventId, optionId):
    return {
        "filename": fileName,
        "eventId": eventId,
        "optionId": optionId
    }