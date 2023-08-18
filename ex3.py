#Nested Dictionary (Dicionario ALinhado)
clientes = {
    "cliente1" : {"nome" : "Astrogildo", "ano" : 1998},
    "cliente2" : {"nome" : "Berislvado", "ano" : 2003},
    "cliente3" : {"nome" : "Lucas", "ano" : 2010}
}

#print (clientes)
#print (len(clientes["cliente2"]))
print (clientes["cliente2"]["nome"])