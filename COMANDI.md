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
MACOS    `netstat -p tcp -p udp` oppure `lsof -n -i4TCP -i4UDP`  
WINDOWS  `netstat -ano`

# COMANDI LINUX
Le directory sono le cartelle che possono contenere più file.
Tab serve per il completamento automatico di nomi di comandi, directory o file.
Ctrl-r serve a cercare un comando nella storia (reverse-find).
I file o directory che hanno il nome che inizia con `.` risultano nascosti, ma si possono vedere con `ls -a`.

> `echo`    print, crea un output, con  `>` oppure `>>` l'output può essere ridirezionato a un file.  
`>` sovrascrive il file, quindi cancella il contenuto del file, `>>` aggiunge il testo senza sovrascrivere.  
`clear`   pulisce lo schermo.  
`date`    stampa data corrente.  
`tty`     stampa il nome del file del terminale connesso all'input.  
`history` stampa la cronologia dei comandi come lista numerata.  
`exit`    esce dal terminale.  
`Ctrl-d`  termina la comunicazione.  
`cat`     stampa il contenuto di un file, se chiamato senza argomento, loop di echo.  

>`man`    cerca l'argomento nel manuale.  
`man -k` o `apropos` fanno una ricerca per argomento, stampano le pagine del manuale dove se ne parla.  
`info`    è una guida alternativa.  
`whatis`  è come `man`, però stampa solo la descrizione breve del comando.  
`whereis` stampa la location del comando e la location del file della pagina del manuale che lo spiega.  
`type`    stampa il tipo di comando, ex. alias, built-in, function.  
`file`    stampa il tipo di file.  
`id`      stampa l'id dell'utente.  
`who am i` o `whoami` o `who mom likes`  stampa il nome utente.  
`who`     stampa i nomi degli utenti, il terminale al quale sono collegati e la data in cui hanno fatto il login.  
`which`	  stampa la location del comando, quindi simile a `whereis`.  

> `find`   cerca una risorsa con un nome che matcha il parametro dalla directory corrente a tutte le subdirectory.  
Ha due opzioni: `-size` e `-type`.  
`-size +2M`   Per esempio stampa solamente file o directory con dimensione maggiore di 2 Megabyte.  
`-type f` oppure `-type d` mostra solamente i risutati della ricerca che sono rispettivamente file o directory.  


> `ls` 	stampa il contenuto di una directory o i nomi dei file e altre informazioni.  
Ha le opzioni `-a -l -t -h -r`, si possono usare insieme tipo: `ls -altrh` o `ls -alt` o `ls -l` .    
`-a`	mostra anche i file e le directory nascoste, quelli che iniziano col punto ex. `.ssh`  
`-l`    long format, mostra privilegi, timestamp, size e autore.  
`-t`    ordina in senso cronologico, dal più recente al più antico.  
`-r`    ordina in senso inverso.  
`-h`    mostra le informazioni in format human-readable. Invece di 4096 byte, mostra 4,0K ovvero 4 kilobytes.  


> Una directory vuota, quindi senza file, contiene sempre e comunque `.` e `..`.  
`~`     simbolo per la home directory.  
`.`     simbolo per la directory corrente.  
`..`    simbolo per la parent directory, directory precedente.  
`touch` modifica il timestamp di un file, oppure crea un nuovo file vuoto.  
`cd`    cambia la directory corrente. `cd` senza argomento ha lo stesso effetto di `cd ~`, riportano alla home directory.  
`pwd`   "print working directory" stampa il path relativo della directory corrente rispetto alla home directory oppure rispetto a "root" `/`.    
`mkdir` crea una nuova directory, opzione `-p` crea tutto un percorso di directory.  
`rmdir` rimuove una directory se non contiene niente.  
`cp`    crea una copia.  
`mv`    modifica il path di una risorsa, come conseguenza può essere anche usato per rinominare file o directory.  
`rm`    rimuove un file, con l'opzione `-R` (ricorsivo) rimuove una directory perché rimuove tutti file. Ciò che non potrebbe fare `rmdir`.  
`ln`    crea un HARDlink `ln TARGET LINK_NAME` ex. `ln file.txt gabriele`, `cat gabriele` mostra il contenuto di file.txt. Con l'opzione `-s` crea un link simbolico, quindi legato al path specificato.

> `tac`  è l'inverso di `cat`, non stampa dalla prima all'ultima riga, stampa dall'ultima alla prima.  
`more`   mostra il file impaginandolo. Premendo `q` si ritorna alla riga di comando.  
`less`   mostra il file impaginandolo, ma dentro a una finestra tipo un editor. Premendo `q` si esce.  
`tail`   `tail file.txt` stampa le ultime 10 righe di un file di default, con l'opzione `-n 5` oppure `-5` per esempio ne stampa 5.  
`head`   `head file.txt` stampa le prime 10 righe di un file di default, con l'opzione `-n 5` oppure `-5` per esempio ne stampa 5.  
`grep`  serve a trovare una particolare parola in un file, l'opzione `-n`  `-l` `-r`   
`wc`    "word count", senza opzioni mostra numero di righe, n. parole, n. caratteri. Altrimenti per visualizzarli separatamente si usano le rispettive opzioni `-l` `-w` e `-c`.  


#### Struttura permessi di un file o directory  
Si possono vedere con `ls -l`

esempio: `ls -l`
`dr--r--r-- 1 root root    4096 apr  9 20:41  Testi`
è una directory, ha permessi di lettura per utente, gruppi e altri, creata da root, del gruppo root, ha una dimensione di 4096 byte, timestamp è 9 aprile alle 20:41, chiamata "Testi".
la prima `d` rappresenta il tipo di file, infatti è una directory, i seguenti sono i permessi.
I 9 bit dei permessi seguono la regola UGO.

Ecco una tabella:

|  user | group | other |
| :---: | :---: | :---: |
|  rwx  |  rwx  |  rwx  |
| 4+2+1 | 4+2+1 | 4+2+1 |  

ex.
tutti i bit attivati `rwxrwxrwx` in ottale sono `777`, tutti hanno tutti i permessi.
`rwxrwxr--` in ottale è `4+2+1 4+2+1 4 = 774`. Quindi utente e gruppo hanno tutti i permessi, gli altri solo di leggere.


> `chown`    cambia l'utente `chown uid file`, si può usare lo userid o semplicemente il nome.  
`chgrp`    cambia il gruppo `chgrp groupid file`, si può usare il groupid o semplicemente il nome.  
`chmod`    cambia i permessi, si possono usare i simboli `+ e -` tipo `chmod u+r file` oppure i numeri in ottale `chmod 777 file`. Nel primo, AGGIUNGE il permesso di lettura all'utente, nel secondo attiva tutti i bit, quindi dà tutti i permessi a tutti.  

