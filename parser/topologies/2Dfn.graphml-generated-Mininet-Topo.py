#!/usr/bin/python

"""
Custom topology for Mininet, generated by GraphML-Topo-to-Mininet-Network-Generator.
"""
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.node import Node
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel

class GeneratedTopo( Topo ):
    "Internet Topology Zoo Specimen."

    def __init__( self, **opts ):
        "Create a topology."

        # Initialize Topology
        Topo.__init__( self, **opts )

        # add nodes, switches first...
        CHE = self.addSwitch( 's0' )
        LEI = self.addSwitch( 's1' )
        ADH = self.addSwitch( 's2' )
        DRE = self.addSwitch( 's3' )
        GSI = self.addSwitch( 's4' )
        HEI = self.addSwitch( 's5' )
        JEN = self.addSwitch( 's6' )
        ILM = self.addSwitch( 's7' )
        DeCix1 = self.addSwitch( 's8' )
        Geant = self.addSwitch( 's9' )
        FZK = self.addSwitch( 's10' )
        STU = self.addSwitch( 's11' )
        DeCix2 = self.addSwitch( 's12' )
        Telia = self.addSwitch( 's13' )
        BIE = self.addSwitch( 's14' )
        Telekom1 = self.addSwitch( 's15' )
        GOE = self.addSwitch( 's16' )
        BRE = self.addSwitch( 's17' )
        WUP = self.addSwitch( 's18' )
        BIR = self.addSwitch( 's19' )
        BON = self.addSwitch( 's20' )
        MAR = self.addSwitch( 's21' )
        GIE = self.addSwitch( 's22' )
        KAS = self.addSwitch( 's23' )
        PAD = self.addSwitch( 's24' )
        EWE = self.addSwitch( 's25' )
        Telekom2 = self.addSwitch( 's26' )
        MUE = self.addSwitch( 's27' )
        SAA = self.addSwitch( 's28' )
        GC = self.addSwitch( 's29' )
        DES = self.addSwitch( 's30' )
        HAM = self.addSwitch( 's31' )
        KIE = self.addSwitch( 's32' )
        ROS = self.addSwitch( 's33' )
        MAG = self.addSwitch( 's34' )
        BRA = self.addSwitch( 's35' )
        KAI = self.addSwitch( 's36' )
        GRE = self.addSwitch( 's37' )
        DOR = self.addSwitch( 's38' )
        BOC = self.addSwitch( 's39' )
        FHM = self.addSwitch( 's40' )
        REG = self.addSwitch( 's41' )
        AUG = self.addSwitch( 's42' )
        GAR = self.addSwitch( 's43' )
        DUI = self.addSwitch( 's44' )
        FZJ = self.addSwitch( 's45' )
        AAC = self.addSwitch( 's46' )
        WUE = self.addSwitch( 's47' )
        TUB = self.addSwitch( 's48' )
        HUB = self.addSwitch( 's49' )
        HAN = self.addSwitch( 's50' )
        FRA = self.addSwitch( 's51' )
        POT = self.addSwitch( 's52' )
        ERL = self.addSwitch( 's53' )
        BAY = self.addSwitch( 's54' )
        FFO = self.addSwitch( 's55' )
        ZIB = self.addSwitch( 's56' )
        ZEU = self.addSwitch( 's57' )

        # ... and now hosts
        CHE_host = self.addHost( 'h0' )
        LEI_host = self.addHost( 'h1' )
        ADH_host = self.addHost( 'h2' )
        DRE_host = self.addHost( 'h3' )
        GSI_host = self.addHost( 'h4' )
        HEI_host = self.addHost( 'h5' )
        JEN_host = self.addHost( 'h6' )
        ILM_host = self.addHost( 'h7' )
        DeCix1_host = self.addHost( 'h8' )
        Geant_host = self.addHost( 'h9' )
        FZK_host = self.addHost( 'h10' )
        STU_host = self.addHost( 'h11' )
        DeCix2_host = self.addHost( 'h12' )
        Telia_host = self.addHost( 'h13' )
        BIE_host = self.addHost( 'h14' )
        Telekom1_host = self.addHost( 'h15' )
        GOE_host = self.addHost( 'h16' )
        BRE_host = self.addHost( 'h17' )
        WUP_host = self.addHost( 'h18' )
        BIR_host = self.addHost( 'h19' )
        BON_host = self.addHost( 'h20' )
        MAR_host = self.addHost( 'h21' )
        GIE_host = self.addHost( 'h22' )
        KAS_host = self.addHost( 'h23' )
        PAD_host = self.addHost( 'h24' )
        EWE_host = self.addHost( 'h25' )
        Telekom2_host = self.addHost( 'h26' )
        MUE_host = self.addHost( 'h27' )
        SAA_host = self.addHost( 'h28' )
        GC_host = self.addHost( 'h29' )
        DES_host = self.addHost( 'h30' )
        HAM_host = self.addHost( 'h31' )
        KIE_host = self.addHost( 'h32' )
        ROS_host = self.addHost( 'h33' )
        MAG_host = self.addHost( 'h34' )
        BRA_host = self.addHost( 'h35' )
        KAI_host = self.addHost( 'h36' )
        GRE_host = self.addHost( 'h37' )
        DOR_host = self.addHost( 'h38' )
        BOC_host = self.addHost( 'h39' )
        FHM_host = self.addHost( 'h40' )
        REG_host = self.addHost( 'h41' )
        AUG_host = self.addHost( 'h42' )
        GAR_host = self.addHost( 'h43' )
        DUI_host = self.addHost( 'h44' )
        FZJ_host = self.addHost( 'h45' )
        AAC_host = self.addHost( 'h46' )
        WUE_host = self.addHost( 'h47' )
        TUB_host = self.addHost( 'h48' )
        HUB_host = self.addHost( 'h49' )
        HAN_host = self.addHost( 'h50' )
        FRA_host = self.addHost( 'h51' )
        POT_host = self.addHost( 'h52' )
        ERL_host = self.addHost( 'h53' )
        BAY_host = self.addHost( 'h54' )
        FFO_host = self.addHost( 'h55' )
        ZIB_host = self.addHost( 'h56' )
        ZEU_host = self.addHost( 'h57' )

        # add edges between switch and corresponding host
        self.addLink( CHE , CHE_host )
        self.addLink( CHE , CHE_host )
        self.addLink( LEI , LEI_host )
        self.addLink( LEI , LEI_host )
        self.addLink( LEI , LEI_host )
        self.addLink( ADH , ADH_host )
        self.addLink( ADH , ADH_host )
        self.addLink( DRE , DRE_host )
        self.addLink( DRE , DRE_host )
        self.addLink( GSI , GSI_host )
        self.addLink( GSI , GSI_host )
        self.addLink( HEI , HEI_host )
        self.addLink( JEN , JEN_host )
        self.addLink( ILM , ILM_host )
        self.addLink( DeCix1 , DeCix1_host )
        self.addLink( Geant , Geant_host )
        self.addLink( FZK , FZK_host )
        self.addLink( FZK , FZK_host )
        self.addLink( FZK , FZK_host )
        self.addLink( STU , STU_host )
        self.addLink( DeCix2 , DeCix2_host )
        self.addLink( Telia , Telia_host )
        self.addLink( BIE , BIE_host )
        self.addLink( BIE , BIE_host )
        self.addLink( BIE , BIE_host )
        self.addLink( GOE , GOE_host )
        self.addLink( GOE , GOE_host )
        self.addLink( BRE , BRE_host )
        self.addLink( BRE , BRE_host )
        self.addLink( BRE , BRE_host )
        self.addLink( WUP , WUP_host )
        self.addLink( WUP , WUP_host )
        self.addLink( BIR , BIR_host )
        self.addLink( BIR , BIR_host )
        self.addLink( BON , BON_host )
        self.addLink( MAR , MAR_host )
        self.addLink( MAR , MAR_host )
        self.addLink( GIE , GIE_host )
        self.addLink( KAS , KAS_host )
        self.addLink( EWE , EWE_host )
        self.addLink( Telekom2 , Telekom2_host )
        self.addLink( MUE , MUE_host )
        self.addLink( SAA , SAA_host )
        self.addLink( SAA , SAA_host )
        self.addLink( GC , GC_host )
        self.addLink( DES , DES_host )
        self.addLink( DES , DES_host )
        self.addLink( KIE , KIE_host )
        self.addLink( KIE , KIE_host )
        self.addLink( ROS , ROS_host )
        self.addLink( ROS , ROS_host )
        self.addLink( MAG , MAG_host )
        self.addLink( MAG , MAG_host )
        self.addLink( BRA , BRA_host )
        self.addLink( KAI , KAI_host )
        self.addLink( GRE , GRE_host )
        self.addLink( DOR , DOR_host )
        self.addLink( BOC , BOC_host )
        self.addLink( FHM , FHM_host )
        self.addLink( FHM , FHM_host )
        self.addLink( REG , REG_host )
        self.addLink( AUG , AUG_host )
        self.addLink( AUG , AUG_host )
        self.addLink( GAR , GAR_host )
        self.addLink( DUI , DUI_host )
        self.addLink( DUI , DUI_host )
        self.addLink( FZJ , FZJ_host )
        self.addLink( AAC , AAC_host )
        self.addLink( WUE , WUE_host )
        self.addLink( WUE , WUE_host )
        self.addLink( TUB , TUB_host )
        self.addLink( TUB , TUB_host )
        self.addLink( TUB , TUB_host )
        self.addLink( TUB , TUB_host )
        self.addLink( HAN , HAN_host )
        self.addLink( HAN , HAN_host )
        self.addLink( HAN , HAN_host )
        self.addLink( HAN , HAN_host )
        self.addLink( FRA , FRA_host )
        self.addLink( FRA , FRA_host )
        self.addLink( POT , POT_host )
        self.addLink( POT , POT_host )
        self.addLink( POT , POT_host )
        self.addLink( POT , POT_host )
        self.addLink( ERL , ERL_host )
        self.addLink( FFO , FFO_host )
        self.addLink( ZIB , ZIB_host )

        # add edges between switches
        self.addLink( CHE , LEI, bw=100, delay='0.298077704142ms')
        self.addLink( CHE , DRE, bw=100, delay='0.322365195402ms')
        self.addLink( LEI , ERL, bw=100, delay='0.999726235212ms')
        self.addLink( LEI , JEN, bw=100, delay='0.304663741178ms')
        self.addLink( LEI , Telekom1, bw=100, delay='0.177188075451ms')
        self.addLink( ADH , ZIB, bw=100, delay='0.0ms')
        self.addLink( ADH , HUB, bw=100, delay='0.0ms')
        self.addLink( DRE , POT, bw=100, delay='0.611196404787ms')
        self.addLink( DRE , ERL, bw=100, delay='1.36511770402ms')
        self.addLink( GSI , FRA, bw=100, delay='0.120153551776ms')
        self.addLink( GSI , HEI, bw=100, delay='0.224591638201ms')
        self.addLink( HEI , FZK, bw=100, delay='0.206100579927ms')
        self.addLink( JEN , ILM, bw=100, delay='0.305112206139ms')
        self.addLink( ILM , ERL, bw=100, delay='0.531397405368ms')
        self.addLink( DeCix1 , FRA, bw=100, delay='1.07425900065ms')
        self.addLink( Geant , FRA, bw=100, delay='1.07425900065ms')
        self.addLink( FZK , STU, bw=100, delay='0.123846482309ms')
        self.addLink( FZK , FRA, bw=100, delay='0.545310550152ms')
        self.addLink( FZK , KAI, bw=100, delay='0.257654222135ms')
        self.addLink( STU , GAR, bw=100, delay='0.183710390854ms')
        self.addLink( DeCix2 , POT, bw=100, delay='1.21589909521ms')
        self.addLink( Telia , POT, bw=100, delay='1.21589909521ms')
        self.addLink( BIE , PAD, bw=100, delay='0.151235973103ms')
        self.addLink( BIE , HAN, bw=100, delay='0.239411525498ms')
        self.addLink( BIE , MUE, bw=100, delay='0.0749935777704ms')
        self.addLink( GOE , HAN, bw=100, delay='0.403219149905ms')
        self.addLink( GOE , KAS, bw=100, delay='0.132198343422ms')
        self.addLink( BRE , EWE, bw=100, delay='0.285174357757ms')
        self.addLink( BRE , HAN, bw=100, delay='0.466716654548ms')
        self.addLink( BRE , HAM, bw=100, delay='0.613075736052ms')
        self.addLink( WUP , BIR, bw=100, delay='0.177529497718ms')
        self.addLink( WUP , DOR, bw=100, delay='0.132208980425ms')
        self.addLink( BIR , FRA, bw=100, delay='0.866363974909ms')
        self.addLink( BIR , BON, bw=100, delay='0.114396168803ms')
        self.addLink( BON , AAC, bw=100, delay='0.43021086546ms')
        self.addLink( MAR , GIE, bw=100, delay='0.123927107746ms')
        self.addLink( MAR , KAS, bw=100, delay='0.335776873611ms')
        self.addLink( GIE , FRA, bw=100, delay='0.226423040499ms')
        self.addLink( KAS , PAD, bw=100, delay='0.212992035908ms')
        self.addLink( EWE , MUE, bw=100, delay='0.593000769253ms')
        self.addLink( Telekom2 , HAN, bw=100, delay='0.65116824746ms')
        self.addLink( MUE , DUI, bw=100, delay='0.239436899338ms')
        self.addLink( SAA , FRA, bw=100, delay='0.726207753593ms')
        self.addLink( SAA , KAI, bw=100, delay='0.237226880719ms')
        self.addLink( GC , FRA, bw=100, delay='0.726207753593ms')
        self.addLink( DES , TUB, bw=100, delay='1.1465338582ms')
        self.addLink( DES , HAM, bw=100, delay='0.0ms')
        self.addLink( KIE , ROS, bw=100, delay='0.613089850628ms')
        self.addLink( KIE , HAN, bw=100, delay='0.95715083448ms')
        self.addLink( ROS , HAN, bw=100, delay='1.23919188963ms')
        self.addLink( ROS , GRE, bw=100, delay='0.451874040959ms')
        self.addLink( MAG , BRA, bw=100, delay='0.198596354707ms')
        self.addLink( MAG , POT, bw=100, delay='0.286623903897ms')
        self.addLink( BRA , HAN, bw=100, delay='0.181955327902ms')
        self.addLink( KAI , FRA, bw=100, delay='0.500429501646ms')
        self.addLink( GRE , POT, bw=100, delay='0.833384976554ms')
        self.addLink( DOR , BOC, bw=100, delay='0.0404988498769ms')
        self.addLink( BOC , DUI, bw=100, delay='0.0384340170956ms')
        self.addLink( FHM , REG, bw=100, delay='0.410717758791ms')
        self.addLink( FHM , GAR, bw=100, delay='0.0571389176142ms')
        self.addLink( REG , ERL, bw=100, delay='0.380251182629ms')
        self.addLink( AUG , GAR, bw=100, delay='0.146679197743ms')
        self.addLink( AUG , ERL, bw=100, delay='0.591013866677ms')
        self.addLink( GAR , FRA, bw=100, delay='0.476790264006ms')
        self.addLink( DUI , HAN, bw=100, delay='0.114794696877ms')
        self.addLink( DUI , FZJ, bw=100, delay='0.303995280517ms')
        self.addLink( FZJ , AAC, bw=100, delay='0.136555592075ms')
        self.addLink( AAC , FRA, bw=100, delay='1.2185434171ms')
        self.addLink( WUE , FRA, bw=100, delay='0.590926981844ms')
        self.addLink( WUE , ERL, bw=100, delay='0.435614129907ms')
        self.addLink( TUB , ZIB, bw=100, delay='0.0ms')
        self.addLink( TUB , HUB, bw=100, delay='0.0ms')
        self.addLink( TUB , POT, bw=100, delay='0.114412479891ms')
        self.addLink( TUB , ZEU, bw=100, delay='0.0950223458116ms')
        self.addLink( HAN , FRA, bw=100, delay='0.947985832412ms')
        self.addLink( HAN , POT, bw=100, delay='0.528173527957ms')
        self.addLink( HAN , ERL, bw=100, delay='1.10642887727ms')
        self.addLink( HAN , FFO, bw=100, delay='0.329662720518ms')
        self.addLink( FRA , POT, bw=100, delay='0.738212609301ms')
        self.addLink( FRA , ERL, bw=100, delay='0.977051156896ms')
        self.addLink( POT , ERL, bw=100, delay='0.924510931658ms')
        self.addLink( POT , BAY, bw=100, delay='0.910912393939ms')
        self.addLink( POT , FFO, bw=100, delay='0.342242121493ms')
        self.addLink( POT , ZIB, bw=100, delay='0.114412479891ms')
        self.addLink( ERL , BAY, bw=100, delay='0.297042828821ms')
        self.addLink( FFO , ZIB, bw=100, delay='0.308640678658ms')
        self.addLink( ZIB , ZEU, bw=100, delay='0.0950223458116ms')


topos = { 'generated': ( lambda: GeneratedTopo() ) }

# HERE THE CODE DEFINITION OF THE TOPOLOGY ENDS

# the following code produces an executable script working with a remote controller
# and providing ssh access to the the mininet hosts from within the ubuntu vm


def setupNetwork():
    "Create network and run simple performance test"
    topo = GeneratedTopo()
    # check if remote controller's ip was set
    # else set it to vbox standard: 10.0.2.2
    if controller_ip == '':
        controller_ip = '10.0.2.2';
    net = Mininet(topo=topo, controller=lambda a: RemoteController( a, ip=controller_ip, port=6633 ), host=CPULimitedHost, link=TCLink)
    return net


def connectToRootNS( network, switch, ip, prefixLen, routes ):
    """Connect hosts to root namespace via switch. Starts network.
      network: Mininet() network object
      switch: switch to connect to root namespace
      ip: IP address for root namespace node
      prefixLen: IP address prefix length (e.g. 8, 16, 24)
      routes: host networks to route to"""
    # Create a node in root namespace and link to switch 0
    root = Node( 'root', inNamespace=False )
    intf = TCLink( root, switch ).intf1
    root.setIP( ip, prefixLen, intf )
    # Start network that now includes link to root namespace
    network.start()
    # Add routes from root ns to hosts
    for route in routes:
        root.cmd( 'route add -net ' + route + ' dev ' + str( intf ) )


def sshd( network, cmd='/usr/sbin/sshd', opts='-D' ):
    "Start a network, connect it to root ns, and run sshd on all hosts."
    switch = network.switches[ 0 ]  # switch to use
    ip = '10.123.123.1'  # our IP address on host network
    routes = [ '10.0.0.0/8' ]  # host networks to route to
    connectToRootNS( network, switch, ip, 8, routes )
    for host in network.hosts:
        host.cmd( cmd + ' ' + opts + '&' )
    print
    print "*** Hosts are running sshd at the following addresses:"
    print

    for host in network.hosts:
        print host.name, host.IP()

    print "(If the topo breaks down HERE, check the xxx.graphml file for duplicate labels!)"
    print
    print "*** Type 'exit' or control-D to shut down network"
    CLI( network )
    for host in network.hosts:
        host.cmd( 'kill %' + cmd )
    network.stop()

if __name__ == '__main__':
    setLogLevel('info')
    #setLogLevel('debug')
    sshd( setupNetwork() )
