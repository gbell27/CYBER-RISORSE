# CLASSI E RANGE DI IP
Ci sono cinque classi: A B C D E.  
Questa è la struttura di ognuno, `x` rappresentano i numeri per i network, `h` i numeri per gli host.  
Sono quattro numeri separati da punti in decimale, ma diventano 32 quando convertiti in binario.  
A: `x.h.h.h` 1 bit e 3 bit  
B: `x.x.h.h` 2 e 2  
C: `x.x.x.h` 3 e 1  


Ogni classe ha un intervallo pubblico e uno privato. La classe A ha indirizzi di loopback (da `127.0.0.1` a `127.255.255.255`)

### Range degli IP
- A:  
  - PUBBLICI da `` a ``  
  - privati sono quelli di loopback detti prima  
- B:  
  - PUBBLICI da `` a ``  
  - PRIVATI da `` a ``   
- C  
  - PUBBLICI da `` a ``  
  - PRIVATI da `` a ``   
- D  
  - PUBBLICI da `` a ``  
  - PRIVATI da `` a ``  
- E:  
  - PUBBLICI da `` a ``  
  - PRIVATI da `` a ``  
