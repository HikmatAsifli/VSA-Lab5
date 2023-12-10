from scipy.optimize import fsolve
import numpy as np

# Tənliyin funksiyası
def equation(x):
    return x**6 - 3*x**2 + x - 1

# Başlangıca görə kökü tapmaq üçün təxmin edilmiş qiymə
initial_guess = 1.25

# Tənliyin kökünü tapmaq
root = fsolve(equation, initial_guess)[0]

print(f"Təxmin edilmiş kök: {initial_guess}")
print(f"Tənliyin kökü: {root}")
