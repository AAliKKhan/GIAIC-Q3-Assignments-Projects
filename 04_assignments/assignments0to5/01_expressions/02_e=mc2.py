C: int = 299792458  

def main():
    mass_in_kg: float = float(input("Enter kilos of mass: "))

    
    energy_in_joules: float = mass_in_kg * (C ** 2)

    print(f"m = {mass_in_kg} kg")
    print(f"C = {C} m/s")
    print(f"{energy_in_joules:.2e} joules of energy!")  # Formats in scientific notation

    
    print(str(energy_in_joules) + " joules of energy!")




if __name__ == '__main__':
    main()