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


def bintoip(bits):
    """
    Questa funzione ritorna un numero ip a partire da 32 bit.
    Prende un int di lunghezza 32, lo divide in pezzi di 8,
    ogni pezzo lo converte in decimale, restituisce l'ip come stringa.
    """
    bits = str(bits)
    bit_res = []
    if len(bits) == 32:
        for i in range(0,32, 8):
            bit_res.append(bits[i: i+8])
    else:
        raise Exception

    res = []
    for i in bit_res:
        res.append(str(int(i, 2)))

    return ".".join(res)


def bitwise_and_ip(ip, netmask, formatted=False):
    """
    Questa funzione prende due ip stringhe, le converte in binario
    per ottenere un int, poi sugli int si può effettuare bitwise AND
    (??? non ci riesco su numeri binari)
    e infine di nuovo convertiti in binario, 
    poi presi 8 bit alla volta e 
    tornato un ip risultato dell'operazione.
    """
    ip = str(iptobin(ip))
    netmask = str(iptobin(netmask))
    int1 = int(ip, 2)
    int2 = int(netmask, 2)
    bin_res = bin(int1 & int2)[2:]  #risultato ancora non è un ip 
    #dividere in chunks
    ip_res = bintoip(bin_res)
    if formatted:
        #cidr notation è prefisso/range
        # numero di bit della netmask
        print(f"CIDR NOTATION: {ip_res}/{netmask.count('1')}")       
        return "nil" 
    else:
        return ip_res


def create_netmask(hosts): #ricerca binaria?
    """
    Questa funzione ritorna il numero di bit da dedicare agli
    host. 32 meno questo numero è il numero di bit riservati
    alla rete.
    Ritorna la maschera in binario, la maschera come ip e il
    numero di bit degli host.
    """
    guess = 1
    while (2**guess - 2) < hosts:
        guess+=1
    # making netmask as a string
    netmask = (32-guess) * "1"
    while len(netmask) < 32:
        netmask += "0"
    #making mask for hosts, used for creating broadcast address
    hostmask = (32-guess) * "0" + guess*"1"
    return bintoip(netmask), hostmask


def add_n_to_bin(binary, n):
    """
    Questa funzione aggiunge un numero n a un numero binario.
    """
    n = int(n)
    binary = str(binary)
    res = bin(int(binary, 2) + n)
    return res[2:]


#input
import argparse

parser = argparse.ArgumentParser("Divide into subnets containing a chosen number of hosts")


parser.add_argument("-i", "--ip", \
                    help="IP address to process")
parser.add_argument("-o", "--hosts", type=int, nargs="+", \
                    help="Number of hosts that can populate the network")
parser.add_argument("-v", "--verbose", action="store_true", \
                    help="Verbose mode, display first, last and broadcast network addresses")
parser.add_argument("-c", "--cidr", action="store_true", \
                    help="Format into CIDR notation")

args = parser.parse_args()

local_scope_ip = args.ip
for net in args.hosts: 
    masks = create_netmask(net)
    netmask = masks[0]
    hostmask = masks[1]
    base = bitwise_and_ip(local_scope_ip, netmask)
    
    first = add_n_to_bin(iptobin(base), 1)
    first_str = bintoip(first)
    
    broadcast = bin(int(str(iptobin(base)), 2) | int(hostmask, 2))[2:]  # bitwise OR to turn all host bits on
    broadcast_str = bintoip(broadcast)
    
    last = add_n_to_bin(broadcast, "-1") # SUBTRACTING one from broadcast.
    last_str = bintoip(last)
    
    local_scope_ip = add_n_to_bin(broadcast, 1)
    if args.cidr:
        ip_cidr = bintoip(local_scope_ip)
        net_cidr = str(iptobin(netmask))
        print(f"CIDR NOTATION: {ip_cidr}/{net_cidr.count('1')}") 

    if args.verbose:
        print(f"""CREATING NETWORK OF {net} hosts
            BASE: {base}
            FIRST: {first_str}
            LAST: {last_str}
            BROADCAST: {broadcast_str} \n\n
            """)





"""
#TESTS

import unittest

class BasicTest(unittest.TestCase):
    def test_functions(self):
        self.assertEqual(iptobin("192.168.35.15"), 11000000101010000010001100001111 )
        self.assertEqual(iptobin("192.168.35.15", formatted=True), '11000000.10101000.00100011.00001111')
        self.assertEqual(iptobin("255.255.0.0"), 11111111111111110000000000000000)
        self.assertEqual(iptobin("255.255.0.0", formatted=True), '11111111.11111111.00000000.00000000')
        #self.assertEqual(create_netmask(1000), (22, 10))
        self.assertEqual(bintoip(11111111111111110000000000000000), "255.255.0.0")
        self.assertEqual(bitwise_and_ip("192.168.35.15", "255.255.224.0"), "192.168.32.0")
        self.assertEqual(bitwise_and_ip("192.168.35.15", "255.255.224.0", formatted=True), "nil")

if __name__ == "__main__":
        unittest.main(verbosity=2)

"""
