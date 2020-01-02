import json

class ConfigParser:
    def __init__(self, config):
        self.file = open(config, 'r')
        self.data = json.load(self.file)
        # print(self.data)
        self.file.close()
    
    def getRules(self):
        if self.data is None:
            raise 'NO DATA IN CONFIG FILE'
        else:
            return self.data.get('RULES', {})
    
    def getColumns(self):
        if self.data is None:
            raise 'NO DATA IN CONFIG FILE'
        else:
            return self.data.get('COLUMNS', {})
    
    def getTP(self):
        if self.data is None:
            raise 'NO DATA IN CONFIG FILE'
        else:
            return self.data.get('TIMEPOINTS', {})