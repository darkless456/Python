# book_pricing.py

def book_cost (quantity): # 价格函数
    discount_factor = 0.6 # 设定折扣系数
    discounted_price = 24.95 * discount_factor
    total_price = discounted_price * quantity
    return total_price

def shipping_cost (quantity): # 货运费用函数
    shipping_first = 3 # 起步价
    shipping_rest = 0.75 # 第二本后价格
    total_shipping = shipping_first + ((quantity-1) * shipping_rest)
    return total_shipping

num_books = int (input ('How many books do you want?'))
total_cost = book_cost (num_books) + shipping_cost (num_books)
print ("Shipping", num_books, "books costs", total_cost)
