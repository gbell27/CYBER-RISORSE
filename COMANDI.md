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
`ln`    crea un link `ln TARGET LINK_NAME` ex. `ln file.txt gabriele`, `cat gabriele` mostra il contenuto di file.txt .

