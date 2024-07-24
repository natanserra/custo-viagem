
def calcular_preco_passagem(distancia):
    """Calcula o preço da passagem com base na distância da viagem."""
    if distancia <= 0:
        return "A distância deve ser um valor positivo."

    if distancia <= 200:
        preco = distancia * 0.50
    else:
        preco = distancia * 0.45
    
    return preco

def main():
    """Função principal para calcular e exibir o preço da passagem."""
    try:
     
        distancia = float(input("Digite a distância da viagem em Km: "))
        

        preco = calcular_preco_passagem(distancia)
        
   
        if isinstance(preco, str):
            print(preco)
        else:
     
            print(f"O preço da passagem é R${preco:.2f}")
    
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")

if __name__ == "__main__":
    main()
