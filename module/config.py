#!/usr/bin/python

# This script delivers functions to read and write ini-configurations

import configparser ## https://wiki.python.org/moin/ConfigParserExamples
import re, os, codecs
from module import cleanType, cleanUnicode

###############################################################################

## reading 'freyr_config.ini'
def getConfig(iniFile = "freyr_config.ini"):
    if os.path.isfile(iniFile):
        cnfg = configparser.SafeConfigParser()
        cnfg.read_file(codecs.open(iniFile, "r", "utf8"))
        #cnfg.read(iniFile)
        return cnfg
    else:
        return None

###############################################################################

def ConfigSectionMap(section = 'defaults', iniFile = 'freyr_config.ini', iniConfig = None):
    dict1 = {}

    if iniFile is None and iniConfig is None:
        return dict1
    elif iniConfig is None:
        if os.path.isfile(iniFile):
            # print os.path.isfile(iniFile)
            iniConfig = configparser.SafeConfigParser()
            # cnfg.read_file(codecs.open(iniFile, "r", "utf8")) #        read(iniFile)
            iniConfig.read(iniFile)
        else:
            return dict1

    options = iniConfig.options(section)

    for option in options:
        try:
            dict1[option] = iniConfig.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print(("exception on %s!" % option))
            dict1[option] = None

    return dict1

###############################################################################

def ConfigSectionMapAdv(section = 'defaults', option = None, iniFile = 'freyr_config.ini', iniConfig = None):
    # print section, option, iniFile, iniConfig
    dict1 = {}

    if iniFile is None and iniConfig is None:
        return dict1
    elif iniConfig is None:
        if os.path.isfile(iniFile):
            # print os.path.isfile(iniFile)
            iniConfig = configparser.SafeConfigParser()
            # cnfg.read_file(codecs.open(iniFile, "r", "utf8")) #        read(iniFile)
            iniConfig.read(iniFile)
        else:
            return dict1

    def _ConfigSectionMap(_section = 'defaults', _iniConfig = None):
        # print _section, _iniConfig
        dict2 = {}

        options = _iniConfig.options(_section)

        for option in options:
            # print option
            try:
                dict2[option] = _iniConfig.get(_section, option)
                if dict2[option] == -1:
                    DebugPrint("skip: %s" % option)
            except:
                print(("exception on %s!" % option))
                dict2[option] = None
        # print options
        return dict2

    try:
        try:
            dict1 = _ConfigSectionMap(_section = "custom", _iniConfig = iniConfig)[option]
        except:
            dict1 = _ConfigSectionMap(_section = section, _iniConfig = iniConfig)[option]
    except:
        dict1 = _ConfigSectionMap(_section = "defaults", _iniConfig = iniConfig)[option]

    ## try to convert to correct data type:
    dict1 = cleanType(dict1)

    ## try to find unicode and decode it:
    dict1 = cleanUnicode(dict1)

    return dict1

def writeConfig(section = "defaults", option = '', value = '', iniFile = None, iniConfig = None):
    if iniFile is None and iniConfig is None:
        raise("no file given!")
    elif iniFile is None:
        iniFile = 'freyr_config.ini'
    elif iniConfig is None:
        if os.path.isfile(iniFile):
            # print os.path.isfile(iniFile)
            iniConfig = configparser.SafeConfigParser()
            iniConfig.read(iniFile)
        else:
            raise("no file there!")
    change = iniConfig.set(section, option, str(value))
    with open(iniFile, 'w+') as change:
        # change = config.set(sec, opt, str(x))
        iniConfig.write(change)
