## tochange
to change ExecStart in ipmail.service   
to change emailsender in ipmail.py   
add this to /etc/crontab to post ip info  at intervals    
0  */12  * * *   root    python3 /home/ray/ipmail/ipmail.py -m="`ip addr`"
