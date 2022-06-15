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
`ln`    crea un HARDlink (come un pointer) `ln TARGET LINK_NAME` ex. `ln file.txt gabriele`, `cat gabriele` mostra il contenuto di file.txt perché l'HARD LINK e il file puntano allo stesso indirizzo di memoria, il file esiste finché ogni riferimento alla memoria non viene cancellato. Con l'opzione `-s` crea un link simbolico, quindi copia soltanto il path relativo del file, infatti muovendo il file link, non funzionerà più (risulterà rotto).

> `tac`  è l'inverso di `cat`, non stampa dalla prima all'ultima riga, stampa dall'ultima alla prima.  
`more`   mostra il file impaginandolo. Premendo `q` si ritorna alla riga di comando.  
`less`   mostra il file impaginandolo, ma dentro a una finestra tipo un editor. Premendo `q` si esce.  
`tail`   `tail file.txt` stampa le ultime 10 righe di un file di default, con l'opzione `-n 5` oppure `-5` per esempio ne stampa 5.  
`head`   `head file.txt` stampa le prime 10 righe di un file di default, con l'opzione `-n 5` oppure `-5` per esempio ne stampa 5.  
`grep`  serve a trovare una particolare parola in un file, l'opzione `-n` mostra la riga in cui è stata trovata la parola, `-l` mostra solo il nome del file contenente la parola cercata, `-r` serve a leggere tutti i file in una directory quindi fa una ricerca ricorsiva.   
`wc`    "word count", senza opzioni mostra numero di righe, n. parole, n. caratteri. Altrimenti per visualizzarli separatamente si usano le rispettive opzioni `-l` `-w` e `-c`.  


#### Struttura permessi di un file o directory  
Si possono vedere con `ls -l`

esempio: `ls -l` ritorna  
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

> Caratteri speciali per il GLOBBING (facilitano il lavoro, sembrano delle regex, ovvero regular expressions)  
`~`   Come detto più su, questo simbolo viene espanso con il "Nome della home directory".  
`*`   Qualsiasi carattere, qualsiasi numero di ripetizioni. "AD LIBITUM".  
`?`   Può essercene uno solo oppure no, è opzionale.  
`[]`    Dei possibili caratteri che si possono trovare tipo: [123] uno di questi tre, oppure [0-9] un solo qualsiasi numero da 0 a 9, oppure [A-Z] una sola qualsiasi lettera maiuscola dalla A alla Z.  
ex. `rm *.txt` elimina qualsiasi file di testo (.txt) nella working directory.  
ex. `rm file[0-9]`  elimina qualsiasi file che abbia come nome "file" e un numero come: `file3 file5 file9 file1`.    
ex. `echo *`  stampa il nome di tutto ciò che è presente nella working directory, quindi potrebbe sostituire `ls`.  

> Ci sono tre file collegati a un processo:    
stdin, ci si riferisce anche usando &0  
stdout &1  
stderr &2  
File speciali  
`/dev/null` se viene utilizzato come output, lo distrugge e viene perso.  
`/dev/zero` fornisce uno stream binario infinito di valori zero che verranno visualizzati come `^@`.  
`/dev/random` fornisce uno stream binario di valori random.  

> Direttive per il redirezionamento  
`<`  redireziona l'input  
`<<`  redireziona l'input quando la sorgente è l'interprete dei comandi  
`>`  redireziona l'output sovrascrivendo  
`>>`  redireziona l'output in "append mode", non sovrascrive, aggiunge alla fine.  
EX. `cp file1 file2` è equivalente a `cat file1 > file2`  
`<` è una direttiva del linguaggio SHELL, perciò anche se posto all'inizio del comando, viene interpretato correttamente.  
`cat < file1` è equivalente a `< file1 cat`    
Redirezionare stdout e stderr a due file diversi, magari per loggare gli errori.  
ex. Comando volutamente sbagliato che produce un errore.  
`cp file cartella_non_esistente/file 1> success.log 2> error.log`  
l'errore verrà scritto nel file `error.log`  

> `tee`  permette il redirezionamento dell'output a un file e allo stdout contemporaneamente.  
`sort`   mostra le righe in maniera ordinata, `-n` considera tutti i caratteri non numerici come zero, quindi ordina solo secondo i valori numerici, `-k` serve a specificare il campo della chiave secondo cui effettuare l'ordinamento.  
`uniq`  serve ad eliminare le ripetizioni degli stessi valori adiacenti, `-c` conta il numero di ripetizioni dei singoli valori unici, solitamente utilizzato con `sort`  
`nl`  numera le linee, come `grep -n`    
`tr`  Translate, sostituisce un carattere con un altro.  
`cut`  serve a spezzare le righe in campi, `-d` specifica il delimitere dei campi, `-f` specifica il campo da selezionare.  

> REGEX  
`^` comincia con   
`$` finisce con  
`.` qualsiasi carattere  
`*` zero o qualsiasi numero di occorrenze di qualsiasi carattere   

> PIPING `|`  
passa l'output del primo comando all'input del secondo.  
I comandi vengono eseguiti in maniera sequenziale e, dato che sono disposti in serie,  
se l'output di un comando alla sinistra del pipe fallisce, i seguenti non verranno eseguiti.  


> `sed` "Stream editor"   
`-n` "quiet mode", non stampa tutto il match, ma solo quello che ci interessa.  
`p`  stampa  
`d`  cancella  
`s`  `s/from/to/`   sostituisce una parola con un'altra.  
EX. `sed 2,5d` cancella dalla seconda alla quinta riga, `sed /ciao/d` cancella tutte le righe in cui ci sia scritto "ciao".  

> `awk`  Aho Weinberger Kernighan, i record sono le linee, i field sono i campi in cui vengono spezzate.  
la sintassi è awk ' {statement} ', si può specificare il delimiter con `-F`, all'interno delle graffe si possono usare i seguenti simboli:  
`$FS` è il delimiter corrente  
`$n`  seleziona l'n-esimo campo    
`$0`  seleziona l'intero record  
`$NF` è il numero di campi  
`$NR` è il numero di record  
`substr($n, from, to)`  seleziona i caratteri di un campo da un indice a un altro. ex. `substr($0, 2, 4)` seleziona solo dal secondo al quarto carattere di tutto il record. 

> VARIABILI IN BASH  
sono dei nomi a cui è stato assegnato un valore.  
`=`    operatore di assegnamento, serve ad assegnare un valore alla variabile.  
`$`    operatore di riferimento, serve a vedere il valore della variabile.  
`env`  mostra tutte le variabili ambientali.  
`unset` cancella una variabile.  

> _VARIABILI SPECIALI_  
`PATH`  l'insieme di directory in cui vengono cercati gli eseguibili dei comandi, la priorità va da sinistra verso destra. Le directory sono separate da `:`, ex. `PATH=$PATH:.` a PATH è stato riassegnato il valore di sé stessa più la directory corrente.  
`TERM`  le informazioni sull'emulatore del terminale in utilizzo.  
`USER`  il nome utente con cui si è collegati.  
`PWD`   il path della directory corrente. Equivalente a `pwd`, ma questa è una variabile.  

> VARIABILI E COMANDI SUI PROCESSI.  
3 stati possibili di un processo: esecuzione, attesa, interrotto, zombie.  
Un "job" è un insieme di comandi eseguiti insieme.  
`$?`  contiene l'exit code dell'ultimo comando eseguito.  
`$$`  contiene il process id (PID) della shell attiva.  
`$PPID` "parent pid", contiene il pid del processo che ha attivato la shell.  
`$!`  contiene il pid dell'ultimo comando eseguito.  
`&`  indica di eseguire il job in background. Viene posto alla fine del comando.  
`pidof`  trova il pid di un processo che esegue un determinato comando.  
`fg`  riporta un processo in foreground ex. `fg %1` rimette in foreground il processo il cui [id] è 1.  
`sleep`  "dorme" per un numero di secondi.  
`jobs`   mostra una lista dei comandi in esecuzione in background.  
`ps`    "process show", mostra i processi attivi nel sistema, `-f` (notazione estesa) mostra altre informazioni, `-e` mostra **tutti** i processi.  
`top`    mostra una "top 10" dei processi che consumano le risorse del sistema.  

> SEGNALI  
In risposta a un segnale un processo può: ignorarlo, eseguire un'azione in default o "catturarlo".  
`kill [sengale] pid` invia un segnale, di default invia `SIGTERM (15)`, ma si può specificare con il numero o con il nome. ex. `-15 -TERM -SIGTERM` si riferiscono allo stesso segnale.  

|SIGname|SIGnum|description|keyboard shortcut|
|:--:|:--:|:--:|:--:|
|SIGHUP| 1 | hangup |ctrl-d|
|SIGINT| 2 | interrupt da tastiera |ctrl-c|
|SIGKILL| 9 | terminazione forzata ||
|SIGPIPE| 13 |pipe interrotta a causa di un fallimento||
|SIGTERM| 15 |come SIGKILL, ma può essere gestito dal processo||
|SIGCHLD| 17 |processo figlio terminato||
|SIGCONT| 18 |ripresa da sospensione||
|SIGSTOP| 19 |sospensione temporanea| ctrl-z|

> SCRIPTING  
PREMESSA: utilizzare un editor di testo ( dal più "semplice" al più comple(ss|t)o )  
nano -> vim -> EMACS. (quindi è preferibile usare emacs).  
OK, dato che l'ho già scritto:  
`nano`  
NELLA PARTE BASSA c'è una reference immediata (anche per questo è il più semplice).  
`ctrl-x` uscire, `ctrl-o` write out (SALVARE).  
Quindi si apre `nano`, si scrive quello che si vuole, poi `ctrl-o` si inserisce un nome [ENTER], `ctrl-x`.
\
COMANDI:  
`source` oppure `.`  legge il file come se fosse un programma, non serve scrivere lo SHEBANG all'inizio di un file del genere perché `source` assicura la sua interpretazione.  
`test -x`  restituisce 1 (VERO) se l'argomento è eseguibile, 0 (FALSO) se non lo è.  
`bc`    è una calcolatrice, può lavorare con il floating point values (float, numeri con la virgola) ex. `echo '3.0 + 2.1' | bc` restituisce `5.1`.  

[FREE ENTRANCE: BASH STRIPPERS (no ok, è una guida concisa e breve di bash)](https://learnxinyminutes.com/docs/bash/)

