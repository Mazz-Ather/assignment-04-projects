"""
program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy
"""
C: int = 299792458
def main():
    mass_in_kg : float = float(input('Enter kilos of Mass : '))
    energy_in_joules :float = mass_in_kg * (C ** 2)
    print('e = m * C^2.........')
    print('m = ' + str(mass_in_kg) + 'kg')
    print('C = ' + str(C) + 'm/s')
    print("-----------------------------------------")
    print(str(energy_in_joules) + ' energy in joules')
    print("-----------------------------------------")

if __name__ =='__main__':
    main()