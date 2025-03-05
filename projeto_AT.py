# Importar as bibliotecas necessárias
import yfinance as yf
import matplotlib.pyplot as plt

# Solicitar ao usuário o nome do ticker
ticker = input("Digite o ticker da ação: ")

# Baixar dados históricos da ação fornecida pelo usuário
dados = yf.download(ticker, start="2019-01-01", end="2024-01-01")

# Verificar se os dados foram baixados corretamente
if dados.empty:
    print(f"Erro: Não foi possível encontrar dados para o ticker {ticker}. Verifique o nome e tente novamente.")
else:
    # Mostrar as primeiras linhas do dataset
    print(dados.head())

    # Plotar o gráfico do preço de fechamento
    plt.figure(figsize=(10,5))
    plt.plot(dados["Close"], label=f"Preço de Fechamento de {ticker}")
    plt.title(f"Evolução do preço da ação {ticker} (2019-2024)")
    plt.xlabel("Data")
    plt.ylabel("Preço (USD)")
    plt.legend()
    plt.grid(True)
    plt.show()

