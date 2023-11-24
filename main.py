""" Main Module to run the application """
from arithmetic_arranger import arithmetic_arranger

process = arithmetic_arranger()

def main():
    """ start process """
    process.arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
    
if __name__ == "__main__":
    main()
