# CLASSI E RANGE DI IP
Ci sono cinque classi: A B C D E.  
Questa è la struttura di ognuno, `x` rappresentano i numeri per i network, `h` i numeri per gli host.  
Sono quattro numeri separati da punti in decimale, ma diventano 32 quando convertiti in binario.  
A: `x.h.h.h` 1 bit e 3 bit  
B: `x.x.h.h` 2 e 2  
C: `x.x.x.h` 3 e 1  


Ogni classe ha un intervallo pubblico e uno privato. La classe A ha indirizzi di loopback (da `127.0.0.1` a `127.255.255.255`)  
Una macchina può riferirsi a sé stessa sia con gli indirizzi di loopback sia con gli _indirizzi ZERO_ che vanno da `0.0.0.0` a `0.255.255.255`

**Gli indirizzi pubblici sono tutti quelli che non sono privati né riservati.**

### Range degli IP
- A:
  - vanno da `0.0.0.0` a `127.255.255.255`
  - privati vanno da `10.0.0.0` a `10.255.255.255`
  - riservati sono quelli di loopback e gli _indirizzi ZERO_ detti qualche riga più su. 
  - gli indirizzi pubblici cominciano da `1.0.0.0`
- B:  
  - vanno da `128.0.0.0` a `191.255.0.0`  
  - PRIVATI da `172.16.0.0` a `172.31.255.255`   
- C  
  - vanno da `192.0.0.0` a `223.255.255.0`  
  - PRIVATI da `192.168.0.0` a `192.168.255.255`   
- D  
  - sono indirizzi multicast  
  - vanno da `224.0.0.0` a `239.255.255.255`  
  - PRIVATI non ce ne sono.  
- E:  
  - sono indrizzi per la ricerca, sperimentali, riservati  
  - vanno da `240.0.0.0` a `255.255.255.255`  
  - PRIVATI non ce ne sono.  
