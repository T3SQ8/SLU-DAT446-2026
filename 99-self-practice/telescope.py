class Telescope:
    def __init__(self):
        self.alpha = 0
        self.delta = 0
        self.observations = list()

        self.prev_rotation_alpha = 0
        self.prev_rotation_delta = 0
        self.last_valid_action = "UNDO"

    # Interval [0, 359]
    def rotate_alpha(self, relative_alpha):
        self.alpha += relative_alpha
        self.alpha = self.alpha % 360

        # LOGGING FOR UNDO
        self.prev_rotation_alpha = relative_alpha
        self.last_valid_action = "ROTATE_ALPHA"

    def rotate_delta (self, relative_delta):
      new_delta = self.delta + relative_delta
      
      if 0 <= new_delta <= 90:
        self.delta = new_delta

        self.prev_rotation_delta = relative_delta
        self.last_valid_action = "ROTATE_DELTA"
        
        return
      
      print("Invalid position")

    def observe(self, star_name):
      new_observation = Observation(self.alpha, self.delta, star_name)
      self.observations.append(new_observation)

      # LOGGING FOR UNDO
      self.last_valid_action = "OBSERVE"

    def print_observations(self):
        for observation in self.observations:
          print(observation)

    def undo(self):
      if self.last_valid_action == "ROTATE_ALPHA":
        self.alpha -= self.prev_rotation_alpha
      elif self.last_valid_action == "ROTATE_DELTA":
        self.delta -= self.prev_rotation_delta
      elif self.last_valid_action == "OBSERVE":
        self.observations.pop()
      else: 
        print("Invalid undo")

      self.last_valid_action = "UNDO"

class Observation:
    def __init__(self, alpha, delta, star_name):
        self.alpha = alpha
        self.delta = delta
        self.star_name = star_name

    def __repr__(self):
      return f"{self.alpha} {self.delta} {self.star_name}"
    