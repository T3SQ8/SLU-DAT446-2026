import math

# Constants
M = 1.991e30  # Mass of the sun in kg
G = 6.67e-11  # Gravitational constant in SI units

class Kepler:
  """
  A class to record planet observations and estimate the radius of their orbits.
  """
  
  def __init__(self):
    """
    Initialize the attributes of the Kepler class.
    """
    self.observations = {}
    
  def observe(self, planet_name, angle, time):
    """
    Record an observation of a given planet at a given time and angle in its orbit.
    
    Args:
      planet_name: The name of the planet being observed
      angle: The angle of the planet in its orbit (in radians)
      time: The time of observation
    """

    #if planet_name not in self.observations:
    #  self.observations[planet_name] = []
    
    self.observations.setdefault(planet_name, [])

    self.observations[planet_name].append( (angle, time) )
    
  def get_period(self, planet_name):
    """
    Return an estimation of the planet's period of revolution.
    
    The estimation is computed by averaging the estimated period of revolution
    for all consecutive observations of the given planet.
    
    Args:
      planet_name: The name of the planet
      
    Returns:
      The estimated period of the planet, or None if there are not enough observations
    """
    # Your code here

    planet_obs = self.observations.get(planet_name, [])

    if len(planet_obs) < 2:
      return None
    else:
      ts = []
      for i in range(len(planet_obs) - 1):
        (a1, t1) = planet_obs[i] 
        (a2, t2) = planet_obs[i+1]
        #a = a2 - a1
        ts.append(2 * math.pi * (t2-t1) / (a2 - a1))
      return sum(ts) / len(ts)
      
    
  def get_radius(self, planet_name):
    """
    Return an estimation of the planet's radius using Kepler's formula.
    
    Args:
      planet_name: The name of the planet
      
    Returns:
      The estimated radius of the planet, or None if there are not enough observations
    """
    # Your code here

    t = self.get_period(planet_name)
    R = None
    
    if t is not None:
      R = (t**2 * G * M /(4*math.pi **2)) ** (1/3)
      
    return R
    
    
  def print_planets(self):
    """
    Print a table with every planet's name, estimated period, and estimated radius.
    
    If there are not enough observations for any given planet, print None for period and radius.
    """
    
    for planet in self.observations:
      print(planet, self.get_period(planet), self.get_radius(planet))


      
