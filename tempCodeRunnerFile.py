input_line = int(input())

for i in range(1, input_line):
    pascal_line_input = int(input())
    
    # print("#{0}".format(input_line))
    for line_a in range(pascal_line_input + 1):
        for line_b in range(line_a):     
            # print(line_b, end=" ")
            print(line_b, end=" ")
        
        if(line_a != 0):
            print()