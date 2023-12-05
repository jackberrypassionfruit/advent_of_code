from ast import literal_eval
import sys

class Distress():
  def __init__(self):
    with open(sys.argv[1]) as infile:
      input_text = infile.read()
      
    # print(input_text.split('\n\n'), end='\n\n')
      
    self.pairs = [pair.split('\n') for pair in input_text.split('\n\n')]
    # print(self.pairs)
    # for pair in self.pairs:
    #   print(pair)
  
  def __repr__(self):
    result = ''
    for pair in self.pairs:
      result += f'{pair[0]} <-> {pair[1]}\n'
    return result
  
  def water_level(self, packet_0, packet_1):
    cont, cont_1, cont_2 = True, True, True
    while cont and (cont_1 or cont_2):
      if type(packet_0) == list and cont_1:
        # print('packet_0: ', packet_0)
        packet_0 = packet_0[0]
        if packet_0 == []:
          cont = False
      else:
        cont_1 = False
        
      if type(packet_1) == list and cont_2:
        # print('packet_1: ', packet_1)
        packet_1 = packet_1[0]
        if packet_1 == []:
          cont = False
      else:
        cont_2 = False
    
    return packet_0, packet_1
    
  
  def recursive_order_check(self, packet_0, packet_1):
    try:
      packet_0_first = packet_0.pop()
    except:
      packet_0_first = None
    
    try:
      packet_1_first = packet_1.pop()
    except:
      packet_1_first = None
      
    # TODO
    # after leveling the 2 input packets, compare their first values
    # if one is None, or they are different, return comparison result
    # else, call the recursive func passing the remainder of both of the packets 
    
    
    
    
    # if   packet_0_first == None:
    #   return 1
    # elif packet_1_first == None:
    #   return -1
    # elif type(packet_0_first) != list and packet_0_first < packet_1_first:
    #   return 1
    # elif type(packet_1_first) != list and packet_0_first > packet_1_first:
    #   return 1
    # else:
    #   return 
    
        
  
  def order_check(self, pair):
    # return self.recursive_order_check(reversed(pair[0]), reversed(pair[1])) # this might not be necessary, since water level work well and I don't have to pop()
    return self.recursive_order_check(pair[0], pair[1])
