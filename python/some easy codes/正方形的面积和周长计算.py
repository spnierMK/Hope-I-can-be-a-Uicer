import math  
  
def calculate_square(side_length):   
    area = side_length ** 2   
    perimeter = 4 * side_length   
    return area, perimeter  
  
side_length = float(input("请输入正方形的边长： "))  
  
area, perimeter = calculate_square(side_length)  
  
print("正方形的面积为： {:.2f}".format(area))  
print("正方形的周长为： {:.2f}".format(perimeter))
