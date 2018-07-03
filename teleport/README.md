## Project Related
https://github.com/gravitational/teleport

## how to setup
first to do: /.install.sh   
if node is  a server in common network
````
    # change the conf/teleport_outerMatser.yaml in:  serverip,token1,token2,clustername   
    mv conf/teleport_outerMatser.yaml /etc/teleport/teleport.yaml   
    mv conf/teleport.service /usr/lib/systemd/system/   
    systemctl enable teleport
    systemctl start teleport   
    tctl users add $USER
 ````
 else if node is a server in private network
 ````
    # change the conf/teleport_innerMaster.yaml in:serverip,token1,clustername   
    mv conf/teleport_innerMaster.yaml /etc/teleport/teleport.yaml  
    mv conf/teleport.service /usr/lib/systemd/system/   
    systemctl enable teleport
    systemctl start teleport   
 ````
if node is a server in private network and it need be connected with remoteserver 
 ```` 
    # change the conf/cluster.yaml in:toservername,token2,remoteip   
    mv conf/cluster.yaml /etc/teleport/cluster.yaml  
    tctl create -c /etc/teleport/teleport.yaml /etc/teleport/cluster.yaml  
 ````
  else if it is normal node:   
 ````
    #change conf/teleport.service ExecStart=usr/bin/teleport start —roles=node,proxy —token=token1 —auth-server=remoteip:3025
    mv conf/teleport.service /usr/lib/systemd/system/  
    systemctl enable teleport
    systemctl start teleport    
 ````