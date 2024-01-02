import os, sys

class BoilingBoulders():
  def __init__(self):
    with open(sys.argv[1], 'r', encoding='utf8') as infile:
      file_text = infile.read()
      
    self.coords = []
    for line in file_text:
      self.coords.append(line.split(','))
      
  
