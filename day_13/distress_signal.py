from ast import literal_eval
import sys

class Distress():
  def __init__(self):
    with open(sys.argv[1]) as infile:
      input_text = infile.read()
            
    self.pairs = [pair.split('\n') for pair in input_text.split('\n\n')]
    # for pair in self.pairs:
    #   print(pair)
    self.correct_pairs = []
  
  def __repr__(self):
    result = ''
    for pair in self.pairs:
      result += f'{pair[0]} <-> {pair[1]}\n'
    return result
  
  def water_level(self, packet_0, packet_1):
    cont, cont_1, cont_2 = True, True, True
    while cont and (cont_1 or cont_2):
      if type(packet_0) == list and cont_1:
        packet_0 = packet_0[0]
        if packet_0 == []:
          cont = False
      else:
        cont_1 = False
        
      if type(packet_1) == list and cont_2:
        packet_1 = packet_1[0]
        if packet_1 == []:
          cont = False
      else:
        cont_2 = False
    
    print('water: ', packet_0, packet_1)
    return packet_0, packet_1
    
  
  def recursive_order_check(self, packet_0, packet_1):
    print('recur:', packet_0, ' / ', packet_1)
    try:
      if type(packet_0) == list:
        while len(packet_0) == len(packet_0[0]) == 1:
          packet_0 = packet_0[0]
    except:
      pass
    try:
      if type(packet_1) == list:
        while len(packet_1)== 1 and len(packet_1[0]) == 1:
          packet_1 = packet_1[0]
    except:
      pass
    # if type(packet_0) == int:
    #   packet_0 = [packet_0]
    # if type(packet_1) == int:
    #   packet_1 = [packet_1]
      
    try:
      packet_0_first = packet_0[0]
    except:
      packet_0_first = None
    
    try:
      packet_1_first = packet_1[0]
    except:
      packet_1_first = None
      
      
      
    # TODO
    # after leveling the 2 input packets, compare their first values
    # if one is None, or they are different, return comparison result
    # else, call the recursive func passing the remainder of both of the packets 
    
    if   not packet_0_first:
      return True
    elif not packet_1_first:
      return False
    
    # print('water args: ', packet_0_first, packet_1_first)
    compair_0, compair_1 = self.water_level(packet_0_first, packet_1_first)
    if compair_0 == []:
      return True
    if compair_1 == []:
      return False
    if compair_0 < compair_1:
      return True
    if compair_0 > compair_1:
      return False
    # at this point you know the water_levels are the same
    # before advancing, maybe check inside the [0]'s
    # if compair_0 == compair_1:
    #   return None
    print('firsts: ', packet_0_first, packet_1_first)
    if type(packet_0_first) == list and len(packet_0_first) > 0 and type(packet_1_first) == list and len(packet_1_first) > 0:
      print('got here')
      check_deeper = self.recursive_order_check(packet_0_first[1:], packet_1_first[1:])
      if check_deeper is not None:
        return check_deeper
        
     
    else:
      return self.recursive_order_check(packet_0[1:], packet_1[1:])
    
        
  
  def order_check(self, pair):
    # print('pair: ', pair)
    if self.recursive_order_check(literal_eval(pair[0]), literal_eval(pair[1])):
      print('Correct')
      return False
    else:
      print('Incorrect')
      return True
      
  def order_check_all(self):
    # filtering as I'm testing just the enumerated values that are erroring
    for pair_index, pair in [(pair_index, pair) for pair_index, pair in enumerate(self.pairs) if pair_index + 1 in [5, 8]]:
    # for pair_index, pair in enumerate(self.pairs):
      print(pair_index + 1) #, '-', pair)
      if not self.order_check(pair):
        self.correct_pairs.append(pair_index + 1)
      # print('\n\n\n')
    print('\n', sum(self.correct_pairs), self.correct_pairs)
    