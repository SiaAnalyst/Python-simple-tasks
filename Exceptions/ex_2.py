result = None
operand = None
operator = None
wait_for_number = True
operators = ['+', '-', '*', '/', '=']
list_of_inputs = []

def get_result(list_of_i):
    global result
    result = 0
    #print(list_of_i)
    for i in range(len(list_of_i)):
        if i == 0:
            result += list_of_i[0]
            #print(result)
        else:
            if list_of_i[i] == '+':
                result += list_of_i[i+1]
            elif list_of_i[i] == '-':
                result -= list_of_i[i+1]
            elif list_of_i[i] == '*':
                result *= list_of_i[i+1]
            elif list_of_i[i] == '/':
                result /= list_of_i[i+1]
    print(result)
    return result


get_result(["10", "+", "5", "6", "/", "3", "-", "a", "2", "*", "6", "= "]) # result 18.0
get_result(["2", "3", "-", "1", "+", "10", "*", "2", "="]) # result 22.0


while True:
    input_symb = input()
    if wait_for_number:
        try:
            input_symb = int(input_symb)
            wait_for_number = False
            list_of_inputs.append(input_symb)
            operand = input_symb
        except ValueError:
            print(f"'{input_symb}' is not a number. Try again")
    else:
        operator = input_symb
        if operator in operators:
            if operator == '=':
                get_result(list_of_inputs)
                break
            else:
                wait_for_number = True
                list_of_inputs.append(operator)
        else:
            print(f"{operator} is not '+' or '-' or '/' or '*'. Try again")