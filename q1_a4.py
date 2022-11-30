number_input = input()
number = number_input.split()
output_number = int(number[0]) - int(number[1])
if output_number < 0:
    output_number = output_number*-1
i = 0
while i < len(number)-1:
    number1 = int(number[i])
    number2 = int(number[i+1])
    output_number1 = number1 - number2
    if output_number1 < 0:
        output_number1 = output_number1*-1
    if output_number1 < output_number:
        output_number = output_number1
    i = i + 1
print(output_number)
