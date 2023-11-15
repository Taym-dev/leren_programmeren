from test_lib import test, report
from math import pi
 
 
 
def calculate_cilinder_content(diameter: float, hoogte:  float) -> float:
    Inhoud = (diameter/ 2) * (diameter/ 2) * pi * hoogte
    afgerond_inhoud = round(Inhoud,1)
    return afgerond_inhoud
 
 
diameter = 8.0
height = 5.0
expect_content = 251.3
calculated_content = calculate_cilinder_content(diameter,height)
name = f'test diameter: {diameter} height: {height}'
test(name, expect_content, calculated_content )
 
report()