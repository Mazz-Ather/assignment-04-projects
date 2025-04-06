def main():
    # Dictionary of planetary gravity factors
    planet_gravity = {
        "mercury": 0.376,
        "venus": 0.889,
        "mars": 0.378,
        "jupiter": 2.36,
        "saturn": 1.081,
        "uranus": 0.815,
        "neptune": 1.14
    }

    while True:
        # Get user input for weight
        try:
            earth_weight = float(input("Enter your weight on Earth (or type 0 to exit): "))
            if earth_weight == 0:
                print("Goodbye!")
                break  # Exit the loop
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue  # Restart the loop

        while True:
            # Get user input for planet
            planet = input("Enter a planet to calculate your weight on (or type 'quit' to exit): ")

            if planet.lower() == "quit":  # Allow case-insensitive exit
                print("Goodbye!")
                return  # Exit the function

            if planet in planet_gravity:
                gravity = planet_gravity[planet]
                weight = round(earth_weight * gravity, 2)
                print(f"Your weight on {planet} is {weight:.2f} N\n")
                break  # Exit inner loop and ask for a new weight
            else:
                print("Invalid planet. Please enter a valid planet name.")

if __name__ == "__main__":
    main()
