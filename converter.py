def readConfig(filename):
    param = []
    defined_param = {}
    with open(filename, "r") as f:  
        undParm = f.read().split("\n")
        for i in undParm:
            param.append(i.split("="))
    for i in param:
        defined_param[i[1]] = i[0]
    if defined_param == {}:
        defined_param = None
    return defined_param

def decimalParaBase(num, base, param=None):
    if num == "ERRO ANIMAL": return "Numero maior ou igual a primeira base."
    final = ""
    arrayDoProcesso = []
    num = int(num)
    base = int(base)
    while num >= base:
        num_sobra = int(num%base)
        arrayDoProcesso.append(num_sobra)
        num = int(num//base)
    arrayDoProcesso.append(num)
    if param == None:
        for i in range(len(arrayDoProcesso)):
            final+=str(arrayDoProcesso[-i-1])
    else:
        for i in list(reversed(arrayDoProcesso)):
            for _ in param:
                i = str(i).replace(_, param[_])
            final+=i
    return final

def baseParaDecimal(num, base):
    split_num = list(reversed(list(num)))
    base = int(base)
    currentSplit = 0
    final = 0
    for i in split_num:
        if int(i) >= base: return "ERRO ANIMAL"
        final += int(i)*(pow(base, currentSplit))
        currentSplit+=1
    return str(final)
