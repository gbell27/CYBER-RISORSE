## COMANDI STUDIATI FINORA
(ci si riferisce a macOS anche come \*nix o Unix)

# Visualizzare la tabella di routing
LINUX    `ip route`  
MACOS    `route print`  
WINDOWS  `netstat -r`

# Visualizzare configurazione delle schede di rete.
LINUX    `ip addr`  
MACOS    `ifconfig`  
WINDOWS  `ipconfig /all`  

# Visualizzare la ARP table
LINUX    `ip neighbour`  
MACOS    `arp`  
WINDOWS  `arp -a`

# Visualizzare le connessioni in corso e le porte in ascolto
LINUX    `netstat -tunp`  
MACOS    `netstat -p tcp -p udp` `lsof -n -i4TCP -i4UDP`  
WINDOWS  `netstat -ano`

LINUX    ``  
MACOS    ``  
WINDOWS  ``  
