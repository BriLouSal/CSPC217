def bmi_calc(height, weight):
    # BMI formula: weight / (height ^ 2)
    return weight / (height ** 2)


# Ask for input of the height and weight. I'll use float to consider decimal points


# Furthermore, let's add replace function on the input in order to catch the mistake
# of the user typing "m" in the input; causing it to fail.

height = float(input('What is your Height in metres(m): ').replace('m', ''))

weight = float(input("What is your Weight in kilograms(kg): ").replace('kg', ''))

# Round it towards to the nearest tenth

bmi = round(bmi_calc(height=height, weight=weight), 1)

print(bmi, "kg/m^2")
