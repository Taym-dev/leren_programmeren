from test_lib import test, report
from math import pi
 
month_discount_brands = ["visco","kimco","yana"]
 
MONTH_DISCOUNT_PERC = 10
def calc_discount(price: float, brand: str, month_discount_brands: list) -> float:
    if brand  in month_discount_brands:
        discount_price = price * (1 - MONTH_DISCOUNT_PERC / 100)
        return round(discount_price ,2)
    return price
   
brand = "kimco"
price = 60.00
expect_content = 54.00
calculated_content = calc_discount(price, brand,month_discount_brands)
name = f'test price: {price} brand: {brand}'
test(name, expect_content, calculated_content)
 
brand = "yana"
price = 50.00
expect_content = 45.00
calculated_content = calc_discount(price, brand,month_discount_brands)
name = f'test price: {price} brand: {brand}'
test(name, expect_content, calculated_content)
 
report()