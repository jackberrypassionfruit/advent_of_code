
class Item():
  def __init__(self, worry_lvl, monkey_index):
    self.worry_lvl = worry_lvl
    self.monkey_index = monkey_index
    
  def __repr__(self):
    return f'Item, worry_lvl: {self.worry_lvl}, monkey_index: {self.monkey_index}\n'
  
  def update(self, worry_lvl, op, test):
    self.worry_lvl = op(worry_lvl) % 9699690
    self.monkey_index = test(worry_lvl)

## this shit was all useless
class MonkeyBusinessFast():
  def __init__(self):
    self.items = \
      [Item(lvl, 0) for lvl in [57] ] + \
      [Item(lvl, 1) for lvl in [58, 93, 88, 81, 72, 73, 65] ] + \
      [Item(lvl, 2) for lvl in [65, 95] ] + \
      [Item(lvl, 3) for lvl in [58, 80, 81, 83] ] + \
      [Item(lvl, 4) for lvl in [58, 89, 90, 96, 55] ] + \
      [Item(lvl, 5) for lvl in [66, 73, 87, 58, 62, 67] ] + \
      [Item(lvl, 6) for lvl in [85, 55, 89] ] + \
      [Item(lvl, 7) for lvl in [73, 80, 54, 94, 90, 52, 69, 58 ] ]
        
    self.monkey_ops = [
      lambda old: old * 13,
      lambda old: old + 2,
      lambda old: old + 6,
      lambda old: old ** 2,
      lambda old: old + 3,
      lambda old: old * 7,
      lambda old: old + 4,
      lambda old: old + 7
    ]
    
    self.monkey_tests = [
      lambda x: 3 if x % 11 == 0 else 2,
      lambda x: 6 if x % 7  == 0 else 7,
      lambda x: 3 if x % 13 == 0 else 5,
      lambda x: 4 if x % 5  == 0 else 5,
      lambda x: 1 if x % 3  == 0 else 7,
      lambda x: 4 if x % 17 == 0 else 1,
      lambda x: 2 if x % 2  == 0 else 0,
      lambda x: 6 if x % 19 == 0 else 0
    ]
    
    self.monkey_num_inspects = [0] * 8
   
  
  def __repr__(self):
    result = ''
    for item_index, item in enumerate(self.items):
        result += f'item: {item_index} has worry_lvl: {item.worry_lvl}, monkey_index: {item.monkey_index}\n'
    return result
  
  def print_current_items(self):
    for item in self.items:
      print(item.worry_lvl)
      
  def print_current_monkey_inspects(self):
    for monkey_index, num_inpects in enumerate(self.monkey_num_inspects):
      print(f'monkey #{monkey_index}: {num_inpects}')
   
  def item_turn(self, item_index):
    current_monkey_index = self.items[item_index].monkey_index
    self.monkey_num_inspects[current_monkey_index] += 1
    current_worry_lvl = self.items[item_index].worry_lvl
    new_worry_lvl = self.monkey_ops[current_monkey_index](current_worry_lvl)
    # new_monkey_index = self.monkey_tests[current_monkey_index](new_worry_lvl)
    # print(f'item: {item_index}, monkey: {current_monkey_index}, new_monkey: {new_monkey_index}, current_worry_lvl: {current_worry_lvl}, new_worry_lvl: {new_worry_lvl}')
    self.items[item_index].update(current_worry_lvl, self.monkey_ops[current_monkey_index], self.monkey_tests[current_monkey_index])
    
    # current_monkey_index = self.items['item_index'].monkey_index
    # self.monkey_num_inspects[current_monkey_index] += 1
    # # change logic here for the monkey list to item list changeover
    # current_worry_lvl = self.items['item_index'].worry_lvl
    # current_worry_lvl = self.monkey_ops[item_index](current_worry_lvl)
    # next_monkey = self.monkey_tests[item_index](current_worry_lvl)
    # self.monkey_items[next_monkey].append(current_worry_lvl)
    # self.monkey_items[item_index] = []
      
  def item_round(self):
    for item_index in range(len(self.items)):
      self.item_turn(item_index)
    
  def calculate_monkey_business(self):
    hi, lo = sorted(self.monkey_num_inspects)[-2:]
    # print(f'hi: {hi}, lo: {lo}')
    return hi * lo
      
      
      
      
      
      
      
      
      
      
      
      
      
      
class MonkeyBusinessSlow():
  def __init__(self):
    self.monkey_items = [
      [57],
      [58, 93, 88, 81, 72, 73, 65] ,
      [65, 95],
      [58, 80, 81, 83],
      [58, 89, 90, 96, 55],
      [66, 73, 87, 58, 62, 67],
      [85, 55, 89],
      [73, 80, 54, 94, 90, 52, 69, 58]
    ]
        
    self.monkey_ops = [
      lambda old: old * 13,
      lambda old: old + 2,
      lambda old: old + 6,
      lambda old: old ** 2,
      lambda old: old + 3,
      lambda old: old * 7,
      lambda old: old + 4,
      lambda old: old + 7
    ]
    
    self.monkey_tests = [
      lambda x: 3 if x % 11 == 0 else 2,
      lambda x: 6 if x % 7  == 0 else 7,
      lambda x: 3 if x % 13 == 0 else 5,
      lambda x: 4 if x % 5  == 0 else 5,
      lambda x: 1 if x % 3  == 0 else 7,
      lambda x: 4 if x % 17 == 0 else 1,
      lambda x: 2 if x % 2  == 0 else 0,
      lambda x: 6 if x % 19 == 0 else 0
    ]
    
    self.monkey_num_inspects = [0] * 8
   
  
  def __repr__(self):
    result = ''
    for item_index, monkey_items in enumerate(self.monkey_items):
        result += f'monkey: {item_index} ({self.monkey_num_inspects[item_index]} inspects) has {monkey_items}\n'
    return result
   
  def item_turn(self, item_index: int):
    for item in self.monkey_items[item_index]:
      self.monkey_num_inspects[item_index] += 1
      item = self.monkey_ops[item_index](item)  % 9699690
      # item = item // 3
      next_monkey = self.monkey_tests[item_index](item)
      self.monkey_items[next_monkey].append(item)
      self.monkey_items[item_index] = []
      
  def monkey_round(self):
    for item_index in range(8):
      self.item_turn(item_index)
      
  def calculate_monkey_business(self):
    hi, lo = sorted(self.monkey_num_inspects)[-2:]
    # print(f'hi: {hi}, lo: {lo}')
    return hi * lo