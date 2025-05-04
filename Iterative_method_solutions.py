import math

def gauss_jacobi(a1, b1, c1, d1,
                 a2, b2, c2, d2,
                 a3, b3, c3, d3, precision):
    x, y, z = 0, 0, 0
    iteration = 1

    print("-" * 48)
    print(f"|{'Iteration':^13}|{'x':^10}|{'y':^10}|{'z':^10}|")
    print("-" * 48)
    print(f"|{0:^13}|{0:^10}|{0:^10}|{0:^10}|")

    while(iteration <= 20):
        x1 = (d1 - (b1 * y) - (c1 * z)) / a1
        y1 = (d2 - (a2 * x) - (c2 * z)) / b2
        z1 = (d3 - (a3 * x) - (b3 * y)) / c3

        print(f"|{iteration:^13}|{x1:^10.{precision}f}|{y1:^10.{precision}f}|{z1:^10.{precision}f}|")

        if(round(x,precision) == round(x1,precision)
           and round(y,precision) == round(y1,precision)
           and round(z,precision) == round(z1, precision)):
            break

        x, y, z = x1, y1, z1
        iteration += 1

    else:
        return None, None, None
    
    print("-" * 48)
    return x, y, z

def gauss_seidal(a1, b1, c1, d1,
                 a2, b2, c2, d2,
                 a3, b3, c3, d3, precision):
    x, y, z = 0, 0, 0
    iteration = 1

    print("-" * 48)
    print(f"|{'Iteration':^13}|{'x':^10}|{'y':^10}|{'z':^10}|")
    print("-" * 48)
    print(f"|{0:^13}|{0:^10}|{0:^10}|{0:^10}|")

    while(iteration <= 20):
        x1 = (d1 - (b1 * y) - (c1 * z)) / a1
        y1 = (d2 - (a2 * x1) - (c2 * z)) / b2
        z1 = (d3 - (a3 * x1) - (b3 * y1)) / c3

        print(f"|{iteration:^13}|{x1:^10.{precision}f}|{y1:^10.{precision}f}|{z1:^10.{precision}f}|")

        if(round(x,precision) == round(x1,precision)
           and round(y,precision) == round(y1,precision)
           and round(z,precision) == round(z1, precision)):
            break

        x, y, z = x1, y1, z1
        iteration += 1

    else:
        return None, None, None
    
    print("-" * 48)
    return x, y, z

def sor(a1, b1, c1, d1,
        a2, b2, c2, d2,
        a3, b3, c3, d3,
        omega, precision):
    
    x, y, z = 0, 0, 0
    iteration = 1

    print("-" * 48)
    print(f"|{'Iteration':^13}|{'x':^10}|{'y':^10}|{'z':^10}|")
    print("-" * 48)
    print(f"|{0:^13}|{0:^10}|{0:^10}|{0:^10}|")

    while(iteration <= 20):
        x1 = (1 - omega) * x + (omega / a1) * (d1 - (b1 * y) - (c1 * z))
        y1 = (1 - omega) * y + (omega / b2) * (d2 - (a2 * x1) - (c2 * z))
        z1 = (1 - omega) * z + (omega / c3) * (d3 - (a3 * x1) - (b3 * y1))
        print(f"|{iteration:^13}|{x1:^10.{precision}f}|{y1:^10.{precision}f}|{z1:^10.{precision}f}|")
        if(round(x,precision) == round(x1,precision)
           and round(y,precision) == round(y1,precision)
           and round(z,precision) == round(z1, precision)):
            break
        x, y, z = x1, y1, z1
        iteration += 1

    else:
        return None, None, None
    
    print("-" * 48)
    return x, y, z

arr = []

for eq_num in range(1, 4):
    a = []
    for var in "xyz":
        a.append(int(input(f"Enter the co-efficient of {var} in equation {eq_num} : ")))
    a.append(int(input(f"Enter the constant term of equation {eq_num} : ")))
    print()
    arr.append(a)

print("The equations are")
for i in range(3):
    print(f"({arr[i][0]})x + ({arr[i][1]})y + ({arr[i][2]})z = {arr[i][3]}")

a1, b1, c1, d1 = arr[0]
a2, b2, c2, d2 = arr[1]
a3, b3, c3, d3 = arr[2]
precision = int(input("Enter precision value : "))

if (a1 != 0 and b2 != 0 and c3 != 0 and
    abs(a1) >= (abs(b1) + abs(c1)) and
    abs(b2) >= (abs(a2) + abs(c2)) and
    abs(c3) >= (abs(a3) + abs(b3))):
    choice = input('''Enter method name("GJ" for Gauss-Jacobi / "GS" for Gauss-Seidel /
                    "SOR" for Successive Over Relaxation (SOR)) : ''')
    if(choice == 'GJ'):
        print("\t\tGauss Jacobi method")
        x, y, z = gauss_jacobi(a1, b1, c1, d1,
                               a2, b2, c2, d2,
                               a3, b3, c3, d3, precision)
        
        if(x != None and y != None and z != None):
            print("The values are:")
            print(f"x = {x:.{precision}f}\ty = {y:.{precision}f}\tz = {z:.{precision}f}")
        else:
            print("Maximum iteration reached")

    elif(choice == 'GS'):
        print("\t\tGauss Seidal method")
        x, y, z = gauss_seidal(a1, b1, c1, d1,
                               a2, b2, c2, d2,
                               a3, b3, c3, d3, precision)
        
        if(x != None and y != None and z != None):
            print("The values are:")
            print(f"x = {x:.{precision}f}\ty = {y:.{precision}f}\tz = {z:.{precision}f}")
        else:
            print("Maximum iteration reached")

    elif(choice == 'SOR'):
        omega = float(input("Enter omega value : "))

        if(1 <= omega <= 2):
            print("\t\tSuccessive Over Relaxation (SOR) method")
            x, y, z = sor(a1, b1, c1, d1,
                          a2, b2, c2, d2,
                          a3, b3, c3, d3,
                          omega, precision)
            if(x != None and y != None and z != None):
                print("The values are:")
                print(f"x = {x:.{precision}f}\ty = {y:.{precision}f}\tz = {z:.{precision}f}")
            else:
                print("Maximum iteration reached")

        else:
            print("Invalid omega value")

    else:
        print("Invalid choice!")

else:
    print("Iterative Methods are not possible")
