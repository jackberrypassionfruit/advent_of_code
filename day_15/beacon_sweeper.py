import sys

class Beacon():
  def __init__(self, my_own_coords, manhattan_distance):
    self.my_own_coords = my_own_coords
    self.manhattan_distance = manhattan_distance
    

class BeaconExclusion():
  def get_manhattan_distance(self, coords_0, coords_1):
    # TODO
    raise NotImplementedError
  
  def __init__(self):
    with open(sys.argv[1], 'r') as infile:
      sensors_and_beacons = infile.readlines()
      
    self.sensors = set()
    self.beacons = set()
    
    #TODO
    # for sensor in sensors_sensors_and_beacons:
      # init a sensor obj and add it to set, with its Manhattan Distance
      # - we will use this later to take the empty board (all '.'s), and draw the "beacon exclusion zones" on top of it
    