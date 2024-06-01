#BMI CALCULATER
"""Tracking your BMI is a useful way of checking if you’re maintaining a healthy weight. It’s calculated using a person's weight and height, using this formula: weight / height²
The resulting number indicates one of the following categories:
 Underweight = less than 18.5
 Normal = more or equal to 18.5 and less than 25
 Overweight = more or equal to 25 and less than 30
 Obesity = 30 or more"""

print("Hi,please enter your weight & height for calculate your BMI :")
weight=int(input("weight:"))
height=int(input("height"))
BMI=weight/float(height*height)
if BMI < 18.5:
    print('Underweight')
elif BMI>=18.5 and BMI<25:
    print('Normal')
elif BMI>=25 and BMI<30:
    print('Overweight')
else :
    print('Obesity')            
