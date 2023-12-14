def arithmetic_arranger(problems, show_answers = False):
    
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = ""
    first = ""
    second = ""
    lines = ""
    sumx = ""

    for problem in problems:
        first_number = problem.split(" ")[0]
        operator = problem.split(" ")[1]
        second_number = problem.split(" ")[2]
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if len(first_number) > 4 or len(second_number) > 4:
            return "Error: Numbers cannot be more than four digits."
        if not first_number.isdigit() or not second_number.isdigit():
            return "Error: Numbers must only contain digits."
          
        result = ""
        if operator == "+":
            result = str(int(first_number) + int(second_number))
        elif operator == "-":
            result = str(int(first_number) - int(second_number))
          
        length = max(len(first_number), len(second_number)) + 2
        top = str(first_number).rjust(length)
        bottom = operator + str(second_number).rjust(length - 1)
        line = "-" * length
        res = str(result).rjust(length)
        
        if problem != problems[-1]:
            first += top + '    '
            second += bottom + '    '
            lines += line + '    '
            sumx += res + '    '
        else:
            first += top
            second += bottom
            lines += line
            sumx += res
          
    if show_answers:
        arranged_problems = first + "\n" + second + "\n" + lines + "\n" + sumx
    else:
        arranged_problems = first + "\n" + second + "\n" + lines
      
    return arranged_problems
  