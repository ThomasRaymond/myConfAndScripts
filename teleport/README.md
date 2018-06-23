## how to setup
1. /.install.sh
1. if node is  a server in common network,change the conf/teleport_outerMatser.yaml:   
    serverip   
    token1   
    token2   
    clustername   
 else if node is a server in private network,change the conf/teleport_innerMaster.yaml:   
    token1   
    serverip   
    clustername   
    if want to connect to the outer server,chang the conf/cluster.yaml:   
      toservername   
      token1   
      remoteip
  else if it is normal node: 
       nothing  
1. 