#!/usr/bin/python

#GraphML-Topo-to-Mininet-Network-Generator
#
# This file parses Network Topologies in GraphML format from the Internet Topology Zoo.
# A python file for creating Mininet Topologies will be created as Output.
# Files have to be in the same directory.
#
# Arguments:
#   TODO : make extensions optional
#   TODO find out what the line above did mean
#   -f          [filename to of GraphML input file]
#   --file      [filename to of GraphML input file]
#   -o          [filename to of GraphML output file]
#   --output    [filename to of GraphML output file]
#   -b          [number as integer for bandwidth in mbit]
#   --bandwidth [number as integer for bandwidth in mbit]
#
# Without specified input, program will terminate.
# Without specified output, outputfile will have the same name as the input file.
#
#
# Created by Stephan Schuberth in 01/2013



import xml.etree.ElementTree as ET
import sys
import math
from sys import argv

input_file_name = ''
output_file_name = ''
bandwidth_argument = ''

# TODO use 'argparse', the built-in argument parser of python
# TODO argparse may seem overhead, but it actually eases helpdoc's
# first check commandline arguments
for i in range(len(argv)):
    if argv[i] == '-f':
        input_file_name = argv[i+1]
    if argv[i] == '--file':
        input_file_name = argv[i+1]
    if argv[i] == '-o':
        output_file_name = argv[i+1]
    if argv[i] == '--output':
        output_file_name = argv[i+1]
    if argv[i] == '-b':
        bandwidth_argument = argv[i+1]
    if argv[i] == '--bandwidth':
        bandwidth_argument = argv[i+1]

# terminate when inputfile is missing
if input_file_name == '':
    sys.exit('\n\tno input file was specified as argument')

# define string fragments for output later on
outputstring_1 = '''#!/usr/bin/python

"""
Custom topology for Mininet, generated by GraphML-Topo-to-Mininet-Network-Generator.
"""

from mininet.topo import Topo

class GeneratedTopo( Topo ):
    "Internet Topology Zoo Specimen."

    def __init__( self, **opts ):
        "Create a topology."

        # Initialize Topology
        Topo.__init__( self, **opts )
'''

outputstring_2='''
        # add nodes
        # switches first
'''

# TODO remove the host adding and
# add a message to remind to not forget the
# hosts after using the generator
outputstring_3='''
        # hosts (put here if needed)
        # dont forget to add edges afterwards!

        #FIXME host and links section needs adjusting to your topology needs!!!
        # this are just exemplarical entries,
        # fitting my topology and needs.
        # I left this here as an sample entry.
        # tailor to your own needs!

        node1 = self.addHost( 'h1' )
        node2 = self.addHost( 'h2' )

        self.addLink( HAM , node1 )
        self.addLink( GAR , node2 )

        # add edges
'''

outputstring_4='''

topos = { 'generated': ( lambda: GeneratedTopo() ) }

# uncomment the following lines to run a basic performance test with your topology.
# fix the next FIXME entries, in case you do not have a remote controller on 10.0.2.2 runnin!

#FIXME uncomment all the following in case you need an executable script for performance testing

#def perfTest():
    #"Create network and run simple performance test"
    #topo = GeneratedTopo()
    ##FIXME chose another controller
    #net = Mininet(topo=topo, controller=RemoteController, host=CPULimitedHost, link=TCLink)
    ##FIXME fix controller ip if needed
    #c1 = net.addController( 'c1', ip='10.0.2.2', port=6633 )
    #net.start()
    #print "Dumping host connections"
    #dumpNodeConnections(net.hosts)
    #print "Testing network connectivity"
    #net.pingAll()
    #print "Testing bandwidth between h1 and h2"
    #h1, h2 = net.getNodeByName('h1', 'h2')
    #net.iperf((h1, h2))
    #net.stop()

#if __name__ == '__main__':
    #setLogLevel('info')
    #perfTest()
'''

# where to put results
outputstring_to_be_exported = ''
outputstring_to_be_exported += outputstring_1

# read file and do the actual parsing
tree = ET.parse(input_file_name)
namespace = "{http://graphml.graphdrawing.org/xmlns}"
ns = namespace # just doing shortcutting, namespaces are needed often.

root = tree.getroot()
graph = root.find(ns + 'graph')

#get all entries
nodes = graph.findall(ns + 'node')
edges = graph.findall(ns + 'edge')

# now first generate the id's
node_root_attrib = ''
node_name = ''
longitude = ''
latitude = ''
id_node_dict = {} # to hold all 'id: name' pairs
id_longitude_dict = {}
id_latitude_dict = {}

#get id data
#get longitude datk
#get latitude data
for n in nodes:
    node_root_attrib = n.attrib['id']
    data = n.findall(ns + 'data')
    for d in data:
        if d.attrib['key'] == 'd34':
            node_name = d.text
        if d.attrib['key'] == 'd33':
            longitude = d.text
        if d.attrib['key'] == 'd30':
            latitude = d.text
        #save data couple
        id_node_dict[node_root_attrib] = node_name
        id_longitude_dict[node_root_attrib] = longitude
        id_latitude_dict[node_root_attrib] = latitude
#create strings
tempstring = ''
# first create the nodes sections
tempstring = ''
for i in range(0, len(id_node_dict)):
    temp =  '        '
    temp += id_node_dict[str(i)]
    temp += " = self.addSwitch( 's"
    temp += str(i)
    temp += "' )\n"
    tempstring += temp

outputstring_to_be_exported += outputstring_2
outputstring_to_be_exported += tempstring
outputstring_to_be_exported += outputstring_3

# second calculate distances, set bandwidth and create the edges
tempstring = ''
distance = 0.0
latency = 0.0
for e in edges:
    # get ids for easier handling
    src_id = e.attrib['source']
    dst_id = e.attrib['target']
    # calculate
    #formula: (for distance)
    #dist(SP,EP) = arccos{ sin(La[EP]) * sin(La[SP]) + cos(La[EP]) * cos(La[SP]) * cos(Lo[EP] - Lo[SP])} * r
    #r = 6378.137 km
    #formula: (speed of light)
    # v = 2.3 * 10**8 m/s
    #formula: (latency being calculated from distance and light speed)
    #t = distance / speed of light
    #t (in ms) = ( distance in km * 1000 (for meters) ) / ( speed of light / 1000 (for ms))
    firstproduct = math.sin(float(id_latitude_dict[dst_id])) * math.sin(float(id_latitude_dict[src_id]))
    secondproductfirstpart = math.cos(float(id_latitude_dict[dst_id])) * math.cos(float(id_latitude_dict[src_id]))
    secondproductsecondpart = math.cos((float(id_longitude_dict[dst_id])) - (float(id_longitude_dict[src_id])))
    distance = math.radians(math.acos(firstproduct + (secondproductfirstpart * secondproductsecondpart))) * 6378.137

    #t (in ms) = ( distance in km * 1000 (for meters) ) / ( speed of light / 1000 (for ms))
    latency = ( distance * 1000 ) / ( 230000 )

    # bandwidth
    #set bw to 10mbit if nothing was specified otherwise on startup
    if bandwidth_argument == '':
        bandwidth_argument = '10';

    # create
    temp =  '        self.addLink( '
    temp += id_node_dict[src_id]
    temp += ' , '
    temp += id_node_dict[dst_id]
    temp += ", bw="
    temp += bandwidth_argument
    temp += ", delay='"
    temp += str(latency)
    temp += "ms')"
    #temp += "ms', loss=0, max_queue_size=1000, use_htb=True)"
    temp += '\n'
    tempstring += temp

outputstring_to_be_exported += tempstring
outputstring_to_be_exported += outputstring_4

# generation finished, write string to file
outputfile = ''
if output_file_name == '':
    output_file_name = input_file_name + '-generated-Mininet-Topo.py'
outputfile = open(output_file_name, 'w')
outputfile.write(outputstring_to_be_exported)
outputfile.close()
print "Generation SUCCESSFUL!"
