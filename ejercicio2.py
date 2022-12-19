


def simplify_varia(polinomi0):
    
    terminos = polinomio.split("+")
    
    coeficientes = []
    variables = []
    for termino in terminos:
        coeficientes.append(termino[:-1])
        variables.append(termino[-1])
    
    exponentes = []
    for variable in variables:
        if variable.isalpha():
            exponentes.append(1)
        else:
            exponentes.append(int(variable[1:]))
   
    variables = []
    for variable in variables:
        if variable.isalpha():
            variables.append(variable)
        else:
            variables.append(variable[0])
    
    for i in range(len(exponentes)):
        if exponentes[i] == 2:
            exponentes[i] = 1
            variables[i] = variables[i] * 2
    
    for i in range(len(coeficientes)):
        if coeficientes[i] == "1":
            coeficientes[i] = ""
        elif coeficientes[i] == "-1":
            coeficientes[i] = "-"
        elif coeficientes[i] == "-":
            coeficientes[i] = "-"
        elif coeficientes[i] == "+":
            coeficientes[i] = "+"
    
          
    for i in range(len(exponentes)):
        if exponentes[i] == 1:
            exponentes[i] = ""
    
         
    for i in range(len(variables)):
        if variables[i] == "1":
            variables[i] = ""
    
    terminos = []
    for i in range(len(coeficientes)):
        terminos.append(coeficientes[i] + variables[i] + str(exponentes[i]))
    
    polinomi0 = ""
    for termino in terminos:
        polinomi0 = polinomi0 + termino + "+"

    polinomi0 = polinomi0[:-1]
    return polinomi0
    

if __name__=="__main__":
    print(simplify_varia("3x-zx+2xy-x"))