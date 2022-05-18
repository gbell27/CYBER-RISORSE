def iptobin(ip, formatted=False):
    """
    questa funzione parsa un ip stringa ex. 192.168.1.1
    ogni numero convertito in binario, poi aggiunto padding di zeri
    e infine se formatted viene ritornato separato da punti, altrimenti
    un numero
    """
    fields = ip.split(".")
    binfields = [bin(int(x))[2:] for x in fields]
    res = []
    for i in binfields:
        temp = i[::-1] #reverse
        while len(temp) < 8:
            temp += "0"
        res.append(temp[::-1])
    if formatted:
        return ".".join(res)
    else:
        return int("".join(res))


def bitwise_and_ip(ip, netmask, formatted=False):
    """
    Questa funzione prende due ip stringhe, le converte in binario
    per ottenere un int, poi sugli int si può effettuare bitwise AND
    (??? non ci riesco su numeri binari)
    e infine di nuovo convertiti in binario, 
    poi presi 8 bit alla volta e 
    tornato un ip risultato dell'operazione.
    """
    ip = "0b" + str(iptobin(ip))
    netmask = "0b" + str(iptobin(netmask))
    int1 = int(ip, 2)
    int2 = int(netmask, 2)
    bin_res = bin(int1 & int2)[2:]  #risultato ancora non è un ip 
    #dividere in chunks
    ip_res = []   # risultato ip
    for i in range(0, 32, 8): # da zero a 32 con step di 8
        field = bin_res[i:i+8]
        ip_res.append(str(int(field, 2)))
    if formatted:
        #cidr notation è prefisso/range
        # numero di bit della netmask
        print(f"CIDR NOTATION: {'.'.join(ip_res)}/{netmask.count('1')}")        
        return "nil" 
    else:
        return ".".join(ip_res)


#TESTS
"""
print(iptobin("192.168.35.15", formatted=True))
print(iptobin("192.168.35.15"))
print(iptobin("255.255.224.0", formatted=True))
print(bitwise_and_ip("192.168.35.15", "255.255.224.0"))
"""

#input
import sys

if len(sys.argv) == 1:
    print("""EXIT: [usage] python iptobin.py IP1 IP2 [cidr]
             ex. python iptobin.py 192.168.35.15 255.255.224.0
             ex. python iptobin.py 192.168.35.15 255.255.224.0 cidr 
            """)
else:
    ip1 = sys.argv[1]
    ip2 = sys.argv[2]
    cidr = sys.argv[-1]

    if cidr == "cidr":
        print(bitwise_and_ip(ip1, ip2, formatted=True))
    else:
        print(bitwise_and_ip(ip1, ip2))

