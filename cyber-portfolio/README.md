# PORTFOLIO
Alcuni programmi applicativi su argomenti studiati.

## Network subnetting tool in Python `iptobin.py`
ex. Creare 2 sottoreti da 1000 host ciascuna 
> `python iptobin.py -i 192.168.35.15 -o 1000 1000 -v -c`  
CIDR NOTATION: 192.168.32.0/22  
CREATING NETWORK OF 1000 hosts  
   NETWORK PREFIX: 192.168.32.0   
            FIRST: 192.168.32.1   
            LAST: 192.168.35.254  
            BROADCAST: 192.168.35.255 <br /><br />
CIDR NOTATION: 192.168.36.0/22  
CREATING NETWORK OF 1000 hosts  
   NETWORK PREFIX: 192.168.36.0  
            FIRST: 192.168.36.1  
            LAST: 192.168.39.254  
            BROADCAST: 192.168.39.255   



> `python iptobin.py --help`  
Flags:
- i  indirizzo ip di partenza
- o  numero di host, se ne possono mettere  
     quanti se ne vogliono, così da creare più sottoreti   
- v  verbose, mostra indirizzo di rete, primo indirizzo, ultimo e broadcast  
- c  cidr notation on oppure off.  
- h  help  

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
`node dnsnodecli.js facebook.com`  

![NodeCliDEMO](https://github.com/gbell27/CYBER-RISORSE/blob/master/cyber-portfolio/nodeDNScli/PeekscreencastDEMO.gif)

(screencast GIF realizzata con https://github.com/phw/peek)

file `rootservers.txt` contiene [Server Root](https://www.iana.org/domains/root/servers) copiati da https://www.iana.org/domains/root/servers.


> Dependencies:  
node@14.17.6  
npm@8.8.0  
inquirer@8.2.4     
node-dig-dns@0.3.2  
axios@0.27.2  
cheerio@1.0.0 

