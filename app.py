import sys
import os
from src import ConfigParser, linter

def main():
    if len(sys.argv) < 2:
        print('Usage: python3 app.py (configfile.xlsx)')
    
    if not os.path.exists(sys.argv[1]):
        raise 'Config File Error'
    
    config = ConfigParser(sys.argv[1])
    print(config.getRules())

main()