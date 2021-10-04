#transforma de cualquier sistema numerico a hexadecimal
def transformaSistema(numero):
    transformado = ""
    aux = 0
    if(numero[0]=="%"):
        aux = int(numero,2)
        transformado = hex(aux)[2:]
    elif (numero[0] == "@"):
        aux = int(numero, 8)
        transformado = hex(aux)[2:]
    elif (numero[0] == "$"):
        transformado = numero
    else:
        aux = numero
        transformado = hex(aux)[2:]
    return  transformado

def obtieneContloc(palabras, arregloTraducidas, longitud):
    proximaPosicion = "0"
    if(palabras[0]=="ORG"):
        proximaPosicion = palabras[1][1:]
    elif(palabras[0]=="START"):
        proximaPosicion = "0000"
    elif (len(arregloTraducidas) == 0):
        proximaPosicion = "0000"
    else:
        #hacer validacion de sistema numerico, solo suma hex + dec por el momento
        suma = int(arregloTraducidas[-1][0],16) + arregloTraducidas[-1][4]
        proximaPosicion = hex(suma)[2:]
    return  proximaPosicion


def traduccion1fase(palabras,arregloTraducidas):
    contloc = ""
    etiqueta = ""
    mnemonico = ""
    direccionamiento = ""
    longitud = 0
    salida = []
    directiva = []
    #1 palabra
    if(len(palabras)==1):
        if (palabras[0] == "START"):
            mnemonico = "START"
            direccionamiento = ""
            longitud = 0
            contloc = obtieneContloc(palabras, arregloTraducidas, longitud)
        elif (palabras[0] == "DC.B"):
            mnemonico = "DC.B"
            direccionamiento = ""
            longitud = 1
            contloc = obtieneContloc(palabras, arregloTraducidas, longitud)
        elif (palabras[0] == "DC.W"):
            mnemonico = "DC.W"
            direccionamiento = ""
            longitud = 2
            contloc = obtieneContloc(palabras, arregloTraducidas, longitud)
        elif(palabras[0]=="ABA"):
            mnemonico = "ABA"
            direccionamiento = "INH"
            longitud = 2
            contloc = obtieneContloc(palabras, arregloTraducidas, longitud)
        elif (palabras[0] == "ASLD"):
            mnemonico = "ASLD"
            direccionamiento = "INH"
            longitud = 1
            contloc = obtieneContloc(palabras, arregloTraducidas, longitud)
        elif (palabras[0] == "BGND"):
            mnemonico = "BGND"
            direccionamiento = "INH"
            longitud = 1
            contloc = obtieneContloc(palabras, arregloTraducidas, longitud)
        elif (palabras[0] == "END"):
            mnemonico = "END"
            direccionamiento = ""
            longitud = 0
            contloc = obtieneContloc(palabras, arregloTraducidas, longitud)
        #2 palabras
    elif (len(palabras) == 2):
        if (palabras[0] == "FBC"):
            mnemonico = "FBC"
            direccionamiento = ""
            longitud = 1
            contloc = obtieneContloc(palabras, arregloTraducidas, longitud)
        elif (palabras[1] == "END"):
            etiqueta = palabras[0]
            mnemonico = "END"
            direccionamiento = ""
            longitud = 0
            contloc = obtieneContloc(palabras, arregloTraducidas, longitud)
            directiva.append(etiqueta)
            directiva.append(contloc)
            tabSim.append(directiva)
        elif (palabras[0] == "FCC"):
            mnemonico = "FCC"
            direccionamiento = ""
            longitud = len(palabras[1])
            contloc = obtieneContloc(palabras, arregloTraducidas, longitud)
        elif (palabras[0] == "DC.W"):
            mnemonico = "DC.W"
            direccionamiento = ""
            lonAux = palabras[1].split(",")
            longitud = len(lonAux)*2
            contloc = obtieneContloc(palabras, arregloTraducidas, longitud)
        elif (palabras[0] == "DC.B"):
            mnemonico = "DC.B"
            direccionamiento = ""
            lonAux = palabras[1].split(",")
            longitud = len(lonAux)
            contloc = obtieneContloc(palabras, arregloTraducidas, longitud)
        elif (palabras[0] == "FILL"):
            mnemonico = "FILL"
            direccionamiento = ""
            longitud = int(palabras[1].split(",")[1])
            contloc = obtieneContloc(palabras, arregloTraducidas, longitud)
        elif (palabras[0] == "BSZ"):
            mnemonico = "BSZ"
            direccionamiento = ""
            longitud = int(palabras[1])
            contloc = obtieneContloc(palabras, arregloTraducidas, longitud)
        elif (palabras[0] == "ORG"):
            mnemonico = "ORG"
            direccionamiento = ""
            longitud = 0
            contloc = obtieneContloc(palabras, arregloTraducidas, longitud)
        elif (palabras[0] == "ADCA"):
            mnemonico = "ADCA"
            if(palabras[1][0]=="#"):
                direccionamiento = "IMM"
                longitud = 2
                contloc = obtieneContloc(palabras, arregloTraducidas, longitud)
            else:
                direccionamiento = "DIR"
                longitud = 2
                contloc = obtieneContloc(palabras, arregloTraducidas, longitud)
        elif (palabras[0] == "ADCB"):
            mnemonico = "ADCB"
            direccionamiento = "IMM"
            longitud = 2
            contloc = obtieneContloc(palabras, arregloTraducidas, longitud)
        elif (palabras[0] == "ADDA"):
            mnemonico = "ADDA"
            direccionamiento = "IMM"
            longitud = 2
            contloc = obtieneContloc(palabras, arregloTraducidas, longitud)
        elif (palabras[0] == "ADDB"):
            mnemonico = "ADDB"
            direccionamiento = "IMM"
            longitud = 2
            contloc = obtieneContloc(palabras, arregloTraducidas, longitud)
        elif (palabras[0] == "ADDD"):  # 16 bits
            mnemonico = "ADDD"
            if(palabras[1][0]=="#"):
                direccionamiento = "IMM"
                longitud = 3
                contloc = obtieneContloc(palabras, arregloTraducidas, longitud)
            else:
                direccionamiento = "DIR"
                longitud = 2
                contloc = obtieneContloc(palabras, arregloTraducidas, longitud)
        elif (palabras[0] == "ANDA"):
            mnemonico = "ANDA"
            direccionamiento = "IMM"
            longitud = 2
            contloc = obtieneContloc(palabras, arregloTraducidas, longitud)
        elif (palabras[0] == "ANDB"):
            mnemonico = "ANDB"
            direccionamiento = "IMM"
            longitud = 2
            contloc = obtieneContloc(palabras, arregloTraducidas, longitud)
        elif (palabras[0] == "ANDC"):
            mnemonico = "ANDC"
            direccionamiento = "IMM"
            longitud = 2
            contloc = obtieneContloc(palabras, arregloTraducidas, longitud)
        elif (palabras[0] == "ASL"):  # 16
            mnemonico = "ASL"
            direccionamiento = "EXT"
            longitud = 3
            contloc = obtieneContloc(palabras, arregloTraducidas, longitud)
        elif (palabras[0] == "ASR"):  # 16
            mnemonico = "ASR"
            direccionamiento = "EXT"
            longitud = 3
            contloc = obtieneContloc(palabras, arregloTraducidas, longitud)
        elif (palabras[0] == "BCC"):
            mnemonico = "BCC"
            direccionamiento = "REL"
            longitud = 2
            contloc = obtieneContloc(palabras, arregloTraducidas, longitud)
        elif (palabras[0] == "BCS"):
            mnemonico = "BCS"
            direccionamiento = "REL"
            longitud = 2
            contloc = obtieneContloc(palabras, arregloTraducidas, longitud)
        elif (palabras[0] == "BEQ"):
            mnemonico = "BEQ"
            direccionamiento = "REL"
            longitud = 2
            contloc = obtieneContloc(palabras, arregloTraducidas, longitud)
        elif (palabras[0] == "BEG"):
            mnemonico = "BEG"
            direccionamiento = "REL"
            longitud = 2
            contloc = obtieneContloc(palabras, arregloTraducidas, longitud)
        elif (palabras[0] == "BGT"):
            mnemonico = "BGT"
            direccionamiento = "REL"
            longitud = 2
            contloc = obtieneContloc(palabras, arregloTraducidas, longitud)
        elif (palabras[0] == "BHI"):
            mnemonico = "BHI"
            direccionamiento = "REL"
            longitud = 2
            contloc = obtieneContloc(palabras, arregloTraducidas, longitud)
    #3 palabras
    elif (len(palabras) == 3):
        if (palabras[1] == "EQU"):
            etiqueta = palabras[0]
            mnemonico = "EQU"
            direccionamiento = ""
            longitud = 0
            contloc = obtieneContloc(palabras, arregloTraducidas, longitud)
            directiva.append(etiqueta)
            directiva.append(hex(int(palabras[2]))[2:])
            tabSim.append(directiva)
        elif (palabras[0] == "BCLR"):
            mnemonico = "BCLR"
            direccionamiento = "DIR"
            longitud = 3
            contloc = obtieneContloc(palabras, arregloTraducidas, longitud)
    salida.append(contloc)
    salida.append(etiqueta)
    salida.append(mnemonico)
    salida.append(direccionamiento)
    salida.append(longitud)
    arregloTraducidas.append(salida)

def limpiarOS():
    for linea in arregloTraducidas:
        if (linea[2] == "ORG"):
            if (linea == arregloTraducidas[0]):
                linea[0] = "0"
            else:
                indice = arregloTraducidas.index(linea)
                suma = int(arregloTraducidas[indice-1][0], 16) + arregloTraducidas[indice-1][4]
                linea[0] = hex(suma)[2:]
        if (linea[2] == "START"):
            if (linea == arregloTraducidas[0]):
                linea[0] = "0"
            else:
                indice = arregloTraducidas.index(linea)
                suma = int(arregloTraducidas[indice - 1][0], 16) + arregloTraducidas[indice - 1][4]
                linea[0] = hex(suma)[2:]

#tratamos el archivo asm
lee = open("P6.asm", 'r')
palabras = []
arregloTraducidas = []
tabSim = []
for linea in lee:#se lee linea por linea
    linea = linea.rstrip("\n")
    palabras = linea.split(" ")
    traduccion1fase(palabras,arregloTraducidas)
lee.close()
#quitamos la direccion temporal de ORG y el START
limpiarOS()
#escribimos el lst ya creado
escribe = open("P6.lst",'w')
for linea in arregloTraducidas:#se lee linea por linea
    escribe.write(linea[0].upper().zfill(4) + "\t" + linea[1]+ "\t" + linea[2] + "\t" + linea[3] + "(LI=" + str(linea[4]) + ")\n")
escribe.close()
#escribimos el tamsim ya creado
escribe = open("P6.tabsim",'w')
for linea in tabSim:#se lee linea por linea
    if(len(linea[1])%2==0):
        escribe.write(linea[0] + "\t" + "$" + linea[1] + "\n")
    else:
        escribe.write(linea[0] + "\t" + "$0" + linea[1] + "\n")
escribe.close()
