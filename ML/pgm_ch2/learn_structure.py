import pandas as pd
import numpy as np
from libpgm.nodedata import NodeData
from libpgm.graphskeleton import GraphSkeleton
from libpgm.discretebayesiannetwork import DiscreteBayesianNetwork
from libpgm.pgmlearner import PGMLearner

def createData():
   nd = NodeData()
   skel = GraphSkeleton()
   fpath = "job_interview.txt"
   nd.load(fpath)
   skel.load(fpath)
   skel.toporder()
   bn = DiscreteBayesianNetwork(skel, nd)

   learner = PGMLearner()
   data = bn.randomsample(1000)
   X, Y = 'Grades', 'Offer'
   c,p,w=learner.discrete_condind(data, X, Y, ['Interview'])
   print "independence between X and Y: ", c, " p-value ", p, " witness node: ", w
   result = learner.discrete_constraint_estimatestruct(data)
   print result.E


if __name__ == "__main__":
   createData()