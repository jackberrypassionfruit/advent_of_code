import sys

class Sensor():
  def __init__(self, coords, exclusion_radius):
    self.coords = coords
    self.exclusion_radius = exclusion_radius
    

class BeaconExclusion():
  def __init__(self):
    with open(sys.argv[1], 'r') as infile:
      sensors_and_beacons = infile.readlines()
      
    self.sensors = set()
    self.beacons = set()
    self.max_x, self.max_y, self.min_x, self.min_y = 0, 0, 0, 0
    
    for line in sensors_and_beacons:
      # init a sensor obj and add it to set, with its Manhattan Distance
      # - we will use this later to take the empty board (all '.'s), and draw the "beacon exclusion zones" on top of it
      sensor_line, beacon_line = line.split(': ')
      sensor_line = sensor_line.lstrip('Sensor at x=')
      x_sensor, y_sensor = [int(num) for num in sensor_line.split(', y=')]
      beacon_line = beacon_line.lstrip('closest beacon is at x=')
      x_beacon, y_beacon = [int(num) for num in beacon_line.split(', y=')]
      
      self.beacons.add((x_beacon, y_beacon))
      
      sensor_exclusion_radius = abs(x_sensor - x_beacon) + abs(y_sensor - y_beacon)
      self.sensors.add(Sensor((x_sensor, y_sensor), sensor_exclusion_radius))
      
    self.sensor_coords = [sensor.coords for sensor in self.sensors]
  
  def model_tunnel(self):
    self.tunnel = []
    for j in range(self.min_y, self.max_y + 1):
      line = []
      for i in range(self.min_x, self.max_x + 1):
        if   (i, j) in self.beacons:
          line.append('B')
        elif (i, j) in self.sensor_coords:
          line.append('S')
        else:
          line.append('.')
      self.tunnel.append(line)
      
    
  def __repr__(self):
    render_tunnel = ''
    for line in self.tunnel:
      render_tunnel += ''.join(line) + '\n'
    return render_tunnel
    # return str(self.beacons)
    
  def calculate_tunnel_bounds(self):
    for sensor in self.sensors:
      coords, radius = sensor.coords, sensor.exclusion_radius
      x_coord, y_coord = [int(coord) for coord in coords]
      for delta_y in range(-1*radius, radius + 1):
        for delta_x in range(-1*(radius - abs(delta_y)) , (radius - abs(delta_y)+1)):
          current_x = x_coord + delta_x
          current_y = y_coord + delta_y
          self.max_x = max(self.max_x, current_x)
          self.min_x = min(self.min_x, current_x)
          self.max_y = max(self.max_y, current_y)
          self.min_y = min(self.min_y, current_y)

  def exclude_zones(self):    
    for sensor in list(self.sensors)[:]:
      coords, radius = sensor.coords, sensor.exclusion_radius
      x_coord, y_coord = [int(coord) for coord in coords]  
      for delta_y in range(-1*radius, radius + 1):
        for delta_x in range(-1*(radius - abs(delta_y)) , (radius - abs(delta_y)+1)):
          current_x = x_coord + delta_x
          current_y = y_coord + delta_y
          current_coords_value = self.tunnel[current_y - self.min_y][current_x - self.min_x]
          if current_coords_value == '.':
            self.tunnel[current_y - self.min_y][current_x - self.min_x] = '#'

if __name__ == '__main__':
  beacon_sweeper = BeaconExclusion()
  beacon_sweeper.calculate_tunnel_bounds()
  beacon_sweeper.model_tunnel()
  beacon_sweeper.exclude_zones()
  print(beacon_sweeper)
  