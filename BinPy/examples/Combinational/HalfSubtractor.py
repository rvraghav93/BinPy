from __future__ import print_function
from BinPy.Combinational.combinational import *
""" Examples for Half Subtractor class """
print ("\n---Initializing the HalfSubtractor class--- ")
print ("hs = HalfSubtractor(0, 1)")
hs = HalfSubtractor(0, 1)
print ("\n---Output of HalfSubtractor")
print ("hs.output()")
print (hs.output())
print("The output is of the form [DIFFERENCE, BORROW]")
print ("\n---Input changes---")
print ("hs.setInput(1, 0) #Input at index 1 is changed to 0")
hs.setInput(1, 0)
print ("\n---New Output of the HalfSubtractor---")
print (hs.output())
print ("\n---Changing the number of inputs---")
print ("No need to set the number, just change the inputs")
print ("Input length must be two")
print ("hs.setInputs(1, 1)")
hs.setInputs(1, 1)
print ("\n---To get the input states---")
print ("hs.getInputStates()")
print (hs.getInputStates())
print ("\n---New output of HalfSubtractor---")
print (hs.output())
print ("\n\n---Using Connectors as the input lines---")
print ("Take a Connector")
print ("conn = Connector()")
conn = Connector()
print ("\n---Set Output at index to Connector conn---")
print ("hs.setOutput(0, conn)")
hs.setOutput(0, conn)
print ("\n---Put this connector as the input to gate1---")
print ("gate1 = AND(conn, 0)")
gate1 = AND(conn, 0)
print ("\n---Output of the gate1---")
print ("gate1.output()")
print (gate1.output())
print ("Information about hs instance can be found by")
print ("hs")
print (hs)
