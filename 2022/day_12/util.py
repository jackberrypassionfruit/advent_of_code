class Node():
    def __init__(self, state, coord, parent, action):
        self.state = state
        self.coord = coord 
        self.parent = parent
        self.action = action
        
    def __repr__(self):
        return f'state: {self.state}, coord: {self.coord}, action: {self.action}'


class StackFrontier():
    def __init__(self):
        self.frontier = []
        
    def __repr__(self):
        print('Current frontier:')
        result = ''
        for node in self.frontier: 
            result += str(node)+'\n'
        return result

    def get_frontier_coords(self):
        coords = []
        for node in self.frontier:
            coords.append(node.coord)
        return coords

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node
