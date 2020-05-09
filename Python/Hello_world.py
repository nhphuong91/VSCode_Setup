import sys
import os
import time
import datetime

def printOut():
    print(f"Formatted string literals: {datetime.datetime.now()} \n")
    time.sleep(1)
    print("String format() Method: {} \n".format(datetime.datetime.now().strftime("%H:%M:%S")))
    time.sleep(1)
    print("Old string formatting: %s \n" %datetime.datetime.now().strftime("%H:%M:%S"))
    return 0

def main():
    '''
    Does all the works!!!
    '''
    printOut()
    

# main entry point for program. we'll call main() to do what needs to be done.
if __name__ == "__main__":
    sys.exit(main())
