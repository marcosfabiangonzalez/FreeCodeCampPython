import re

def arithmetic_arranger(arr, show=False) -> str:
  str_op1 = ""
  str_op2 = ""
  str_sep = ""
  str_ans = ""

  if len(arr) > 5:
    return "Error: Too many problems."

  for item in arr:
    item = item.strip().replace(' ', '')
    if not validate_operators(item):
      return "Error: Operator must be '+' or '-'."

    if not validate_digits(item):
      return "Error: Numbers must only contain digits."

    operands = item.split("+") if '+' in item else item.split('-')
    oper1 = operands[0]
    oper2 = operands[1]

    if not validate_length_operands(oper1, oper2):
      return "Error: Numbers cannot be more than four digits."

    max_length = max(len(oper1), len(oper2))
    dashes = 6 if max_length > 3 else max_length + 2

    str_oper1 = " " * (dashes - len(oper1)) + oper1
    str_oper2 = " " * (dashes - len(oper2)) + oper2
    separator = "-" * dashes
    result = "0"

    if '+' in item:
      str_oper2 = str_oper2.replace(" ", "+", 1)
      result = str(int(oper1) + int(oper2))
    else:
      str_oper2 = str_oper2.replace(" ", "-", 1)
      result = str(int(oper1) - int(oper2))

    str_op1 += str_oper1 + " " * 4
    str_op2 += str_oper2 + " " * 4
    str_sep += separator + " " * 4
    answer = " " * (len(separator) - len(result)) + result
    str_ans += answer + " " * 4

  result = str_op1.rstrip() + "\n" + str_op2.rstrip() + "\n" + str_sep.rstrip()

  if show:
    result += "\n" + str_ans.rstrip()

  return result


def validate_digits(item: str) -> bool:
  operation = re.match('^-?[\\d]+[.+,-]-?[\\d]*$', item)
  return True if operation is not None else False


def validate_operators(item: str) -> bool:
  operation = re.findall('\\S+[+,-]\\S+', item)
  return True if not len(operation) == 0 else False


def validate_length_operands(oper1: str, oper2: str) -> bool:
  return False if len(oper1) > 4 or len(oper2) > 4 else True
