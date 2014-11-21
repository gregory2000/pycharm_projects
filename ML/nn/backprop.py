import random

class Node:
   def __init__(self):
      self.lastOutput = None
      self.lastInput = None
      self.error = None
      self.outgoingEdges = []
      self.incomingEdges = []
 
class Edge:
   def __init__(self, source, target):
      self.weight = random.uniform(0,1)
      self.source = source
      self.target = target
 
      # attach the edges to its nodes
      source.outgoingEdges.append(self)
      target.incomingEdges.append(self)

class Network:
   def __init__(self):
      self.inputNodes = []
      self.outputNode = None

class InputNode(Node):
   def __init__(self, index):
      Node.__init__(self)
      self.index = index; # the index of the input vector corresponding to this node