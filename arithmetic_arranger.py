
from array import *

import re

class arithmetic_arranger:
    str_op1: str
    str_op2: str
    str_sep: str
    str_ans: str
    
    def arithmetic_arranger(self, arr, show = False) -> None:
        self.str_op1 = ""
        self.str_op2 = ""
        self.str_sep = ""
        self.str_ans = ""
        
        if len(arr) > 4:
            print("Error: Too many problems.")
            return
        
        for item in arr:
            item = item.strip().replace(' ','')
            if not self.validate_operators(item):
                print("Error: Operator must be '+' or '-'.")
                return
            
            if not self.validate_digits(item):
                print("Error: Numbers must only contain digits.")
                return
            
            if not self.set_operation(item, show):
                return
        
        print(self.str_op1)
        print(self.str_op2)
        print(self.str_sep)
        print(self.str_ans)
        print("Process Run.")
    
    def validate_digits(self, item: str) -> bool:
        operation = re.findall('\\d[+,-]\\d', item)
        return True if not len(operation) == 0 else False
       
    def validate_operators(self, item: str) -> bool:
        operation = re.findall('\\S+[+,-]\\S+', item)
        return True if not len(operation) == 0 else False
    
    def validate_length_operands(self, oper1: str, oper2: str) -> bool:
        return False if len(oper1) > 4 or len(oper2) > 4 else True
    
    def set_operation(self, item: str, show: bool) -> bool:
        operands = list()
        
        operands = item.split("+") if '+' in item else item.split('-')
        oper1 = operands[0]
        oper2 = operands[1]
        
        if not self.validate_length_operands(oper1, oper2):
            print("Error: Numbers cannot be more than four digits.")
            return False
        
        max_length = max(len(oper1), len(oper2))
        dashes = 6 if max_length > 3 else max_length + 2
            
        str_oper1 = " " * (dashes-len(oper1)) + oper1
        str_oper2 = " " * (dashes-len(oper2)) + oper2
        separator = "-" * dashes
        result = "0"
        
        if '+' in item:
            str_oper2 = str_oper2.replace(" ", "+", 1)
            result = str(int(oper1) + int(oper2))
        else:
            str_oper2 = str_oper2.replace(" ", "-", 1)
            result = str(int(oper1) - int(oper2))
            
        #operation = str_oper1 + "\n" + str_oper2 + "\n" + separator
        self.str_op1 += str_oper1 + " " * 4
        self.str_op2 += str_oper2 + " " * 4
        self.str_sep += separator + " " * 4
        
        if show:
            answer = " " * (len(separator)-len(result)) + result
            #operation += "\n" + answer + "\n"
            self.str_ans += answer + " " * 4
            
        #print(operation)
        
        return True