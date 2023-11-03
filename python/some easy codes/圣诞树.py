def print_christmas_tree(height):  
    for i in range(height):  
        print(' ' * (height - i - 1) + '*' * (2 * i + 1))  
    print(' ' * (height - 1) + '|')  
  
print_christmas_tree(10)