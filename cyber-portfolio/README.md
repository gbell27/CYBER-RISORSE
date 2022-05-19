# PORTFOLIO
Alcuni programmi applicativi su argomenti studiati.

## Network subnetting tool in Python `iptobin.py`
> `python iptobin.py 192.168.35.15 255.255.224.0`  
   192.168.32.0
   
> `python iptobin.py 192.168.35.15 255.255.224.0 cidr`  
   CIDR NOTATION: 192.168.32.0/19  
   nil


> A: `11000000.10101000.00100011.00001111`   
B: `11111111.11111111.11100000.00000000`  
&: `11000000.10101000.00100011.00001111` 


## DNS lookup CLI in nodeJS

Basato su questo [video](https://www.youtube.com/watch?v=-wMU8vmfaYo) che parla di DNS, in particolare di quando Facebook è andato in down per 5 ore.

#### Risolvere il nome facebook.com nel terminale
`dig @198.41.0.4 www.facebook.com` asking _a.root-servers.net_ Verisign dns.  
`dig @192.12.94.30 www.facebook.com` asking _e.gtld-servers.net_ TLD server
`dig @129.134.30.12 www.facebook.com` asking _a.ns.facebook.com_ Facebook nameserver  
`QUERY: 1, ANSWER: 1  
;; ANSWER SECTION:  
facebook.com.		300	IN	A	157.240.231.35` 

#### NodeJS cli

file `rootservers.txt` contiene [Server Root](https://www.iana.org/domains/root/servers) copiati da https://www.iana.org/domains/root/servers.

> Dependencies:  
node@14.17.6  
npm@8.8.0  
inquirer@8.2.4     
chalk@5.0.1  
commander@9.2.0  
inquirer-press-to-continue@1.1.2  
inquirer-tree-prompt@1.1.2  
node-dig-dns@0.3.2  
node-netstat@1.8.0  

<!-- ![](GIF demo) -->
