input_line = int(input())

for i in range(1, input_line + 1):
    pascal_line_input = int(input())
    
    print("#{}".format(i))
    for line_a in range(1, pascal_line_input + 1):
        for line_b in range(1, line_a + 1):     
            if(line_b == line_a):
                line_b = 1
                print(line_b, end=" ")
            else:
                print(line_b, end=" ")
                            
        print()