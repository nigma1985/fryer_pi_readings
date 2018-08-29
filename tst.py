#!/usr/bin/python3

## from module import *
## import module.netTools as ntt
## from module.read.pi import *
import module.config as ini ## https://wiki.python.org/moin/ConfigParserExamples
from module.freyr import findConfig
## from module import cleanUnicode

## y = "u'Icb bin der \\u2103. Mein Name ist \\u2103 ich weiß von nix.'"
configFile = "freyr_config.ini"
config = ini.getConfig(configFile)

x = findConfig(sysKey = "cpu_temp_measure_sign", confSection = 'tmp_celsius', confOption = 'measure_sign', confFile = config)

print(x)

# print(y, cleanUnicode(y))
