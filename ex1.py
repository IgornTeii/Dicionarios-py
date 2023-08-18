dicionario = { 
    "montadora" : "Ford",
    "modelo" : "Mustang",
    "ano" : 2000
}

#dicionario["ano"] = 1964
dicionario.update({"ano":1999, "modelo" : "Ferarri"})
dicionario.pop("montadora")
print(dicionario)


