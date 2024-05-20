def calcular_imc(peso, altura):
    # Fórmula do IMC: peso (kg) / (altura (m) * altura (m))
    imc = peso / (altura ** 2)
    return imc

def interpretar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

def main():
    peso = float(input("Digite o seu peso em kg: "))
    altura = float(input("Digite a sua altura em metros: "))

    imc = calcular_imc(peso, altura)
    interpretacao = interpretar_imc(imc)

    print("Seu IMC é:", imc)
    print("Sua categoria de peso é:", interpretacao)

if __name__ == "__main__":
    main()
