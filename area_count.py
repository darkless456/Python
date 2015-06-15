def area(width, height):
#计算平面四边形的面积
	return width * height
# w=3
# h=4
w = float(input("the Width is ")) # 输入浮点数
h = float(input("the Height is "))
print("width =", w, " height =", h, " area =", area(w, h))
# 错误写法：print("width = ", w ,"height = ", h "area = ", area(w, h))   少一个”,“符号
