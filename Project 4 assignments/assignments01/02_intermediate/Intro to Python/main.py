# Dictionary of planets with gravity relative to Earth
planets = {
    "Mercury": 37.6,
    "Venus": 88.9,
    "Mars": 37.8,
    "Jupiter": 236.0,
    "Saturn": 108.1,
    "Uranus": 81.5,
    "Neptune": 114.0
}

# Step 1: Get weight on Earth
earth_weight = float(input("Enter your weight on Earth: "))

# Step 2: Display planet choices after weight input
print("\nChoose a planet:")
for planet in planets:
    print(f"- {planet}")

# Step 3: Get user choice
choice = input("\nEnter the name of the planet: ").strip()

# Step 4: Validate input and calculate weight on chosen planet
if choice in planets:
    planet_gravity = planets[choice]
    weight_on_planet = (earth_weight * planet_gravity) / 100  # Convert weight
    print(f"\nYour weight on {choice} would be: {weight_on_planet:.2f} kg")
else:
    print("Invalid choice. Please enter a valid planet name.")
