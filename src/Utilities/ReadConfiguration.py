import sys , traceback
from configparser import ConfigParser

class ReadConfiguration:


    def read_config(file_name, section_name,key_name):
        try:
            config_parser = ConfigParser()
            config_parser.read(file_name)
            return config_parser.get(section_name,key_name)
        except Exception as e:
            print('FATAL ERROR in ReadConfiguration.py(read_config)')
            print(e)
            print(sys.exc_info())
            print(traceback.format_exc())
            raise Exception(e)


