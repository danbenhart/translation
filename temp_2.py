from deep_translator import GoogleTranslator
import configparser
import progressbar

filename = r'C:\MCOSMOS_V51\temp\GEO_EDM.udl'
comment_prefixes = ('#', ';')
config = configparser.ConfigParser(allow_no_value=True)

config.read(filename)

print(config.items('GEOEDM_Main', raw=True))
