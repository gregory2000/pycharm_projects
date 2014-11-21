from libpgm.graphskeleton import GraphSkeleton
from libpgm.nodedata import NodeData
from libpgm.discretebayesiannetwork import DiscreteBayesianNetwork
from libpgm.tablecpdfactorization import TableCPDFactorization

def getTableCPD():
   nd = NodeData()
   skel = GraphSkeleton()
   jsonpath = "job_interview.txt"
   nd.load(jsonpath)
   skel.load(jsonpath)

   #load bayesian network
   bn = DiscreteBayesianNetwork(skel, nd)
   tablecpd = TableCPDFactorization(bn)
   return tablecpd


if __name__ == "__main__":
   tcpd = getTableCPD()
   result = tcpd.specificquery(dict(Grades='1'), dict(Interview='1', Experience='1'))
   print(result)
