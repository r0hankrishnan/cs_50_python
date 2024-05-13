#Prompt for mass
mass = int(input("Please enter a mass (in kgs): "))

#Define energy function
def energy_func(m):
     E = m * (300000000**2)
     print(E,"joules")

#Call energy function
energy_func(mass)