import json

def SAVE(screen):
    data = {
        'screen' : screen,
        'state' : 'menu'
    }
    with open('system_files\\save\\config.txt','w') as d:
        json.dump(data,d)
        
def LOAD(data):
    with open('system_files\\save\\config.txt') as d:
        DATA_MANAGEMENT = json.load(d)
        for keys , values in DATA_MANAGEMENT.items():
            if keys == data:
                return values