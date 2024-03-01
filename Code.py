import random
meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "XD":"Risa",
            "MELO":"Genial,bueno",
            "PARCERO":"amigo conocido",
            "IDK":"No lo se",
            }
word =input("Que palabra no entiendes(En mayusculas)")

if word in meme_dict.keys():
    print(word +":", meme_dict[word] )
else:
    print("No tengo la definicion de esa palabra pero puedo darte la siguiente:")
    clave = random.choice(meme_dict.keys())
    print(clave + ":", meme_dict[clave])
