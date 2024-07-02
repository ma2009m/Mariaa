class residencia():

    imobiliaria = 'gandini'
    
    def __init__(self, rua, bairro, CEP):
        self.rua = rua 
        self.bairro = bairro
        self.CEP = CEP

    def enderecoCompleto(self): 
        return "Endereço Completo: "+self.rua+  ", " +self.bairro+ " CEP: "+self.CEP

residencia1 = residencia(rua="Santana", bairro="centrao", CEP="13300220" )

residencia2 = residencia(rua="7 de Abril", bairro="centrinho", CEP="13300230")


print(residencia1.imobiliaria)
print(residencia2.imobiliaria)
