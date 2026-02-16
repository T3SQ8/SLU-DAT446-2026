import math

# Constants
M = 1.991e30  # Mass of the sun in kg
G = 6.67e-11  # Gravitational constant in SI units

# Planet radii in meters
radii = {
  "mercury": 57.9e9,
  "venus": 108.2e9,
  "earth": 149.6e9,
  "mars": 228e9,
  "jupiter": 779.3e9,
  "saturn": 1427e9,
  "uranus": 2871e9,
  "neptune": 4497e9,
  "pluto": 5913e9
}

def planet_period(name):
  if name not in radii.keys():
    print("Unknown planet name") 
    return

  radius = radii[name]

  period_sq = (4 * (math.pi**2) / (G*M)) *  (radius** 3) 
  period = math.sqrt(period_sq)

  print(period)
  
  
  
