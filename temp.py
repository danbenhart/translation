from deep_translator import GoogleTranslator
import configparser
import progressbar

widgets = [' [',
           progressbar.Timer(format= 'elapsed time: %(elapsed)s'),
           '] ', progressbar.Bar('*'), ' (', progressbar.ETA(), ') ', ]

# text = 'Eingabe zur Versatzdatenerfassung Zimmer und Kreim'

# translated = GoogleTranslator(source='de', target='en').translate(text)  # output -> Weiter so, du bist großartig
#
# print(translated)

filename = r'C:\MCOSMOS_V51\LAYOUT\CAD_GEO_EDM.udl'

config = configparser.ConfigParser()
config.read(filename)
num_sections = len(config.sections())
i = 1

bar = progressbar.ProgressBar(max_value=num_sections,
                              widgets=widgets).start()

for section in config.sections():
    bar.update(i)
    if 'Name' in config[section]:
        name = config[section]['Name']
        if '---' in name:
            pass
        else:
            translated = GoogleTranslator(source='de', target='en').translate(name)
            config[section]['Name'] = translated
    i += 1

with open('example.ini', 'w') as configfile:
    config.write(configfile)
