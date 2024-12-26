import pandas as pd

def importar_dados():
    dados = 'aluguel.csv'
    leitura_dados = pd.read_csv(dados, sep=";")
    return leitura_dados

def escolher_tipo_imovel(df):
  tipos_disponiveis = df['Tipo'].unique()
  print("Tipos de imóveis disponíveis:")
  for i, tipo in enumerate(tipos_disponiveis):
      print(f"{i + 1}. {tipo}")
  
  escolha = int(input("\nEscolha o número correspondente ao tipo de imóvel que você deseja filtrar: ")) - 1
  tipo_escolhido = tipos_disponiveis[escolha]
  return tipo_escolhido

def filtrar_imoveis_por_tipo(df, tipo):
  df_tipo = df[df['Tipo'] == tipo]
  
  # Criando um DataFrame com os dados filtrados
  tipo_dict = {
      'Bairro': df_tipo['Bairro'].tolist(),
      'Quartos': df_tipo['Quartos'].tolist(),
      'Vagas': df_tipo['Vagas'].tolist(),
      'Valor': df_tipo['Valor'].tolist()
  }
  
  df_tipo_novo = pd.DataFrame(tipo_dict)
  
  # Gerando os subplots
  fig, axs = plt.subplots(1, 3, figsize=(18, 6))
  
  # Subplot 1: Número de Quartos vs. Valor de Aluguel
  axs[0].scatter(df_tipo_novo['Quartos'], df_tipo_novo['Valor'], alpha=0.6)
  axs[0].set_title(f"Nº de Quartos vs. Valor de Aluguel - {tipo}")
  axs[0].set_xlabel("Número de Quartos")
  axs[0].set_ylabel("Valor de Aluguel (R$)")
  axs[0].grid(True)
  
  # Subplot 2: Número de Vagas vs. Valor de Aluguel
  axs[1].scatter(df_tipo_novo['Vagas'], df_tipo_novo['Valor'], alpha=0.6)
  axs[1].set_title(f"Nº de Vagas vs. Valor de Aluguel - {tipo}")
  axs[1].set_xlabel("Número de Vagas")
  axs[1].set_ylabel("Valor de Aluguel (R$)")
  axs[1].grid(True)
  
  # Subplot 3: Histograma da Distribuição dos Valores de Aluguel
  axs[2].hist(df_tipo_novo['Valor'], bins=20, edgecolor='black')
  axs[2].set_title(f"Distribuição dos Valores de Aluguel - {tipo}")
  axs[2].set_xlabel("Valor de Aluguel (R$)")
  axs[2].set_ylabel("Frequência")
  
  plt.tight_layout()
  plt.show()
  
  return df_tipo_novo

def main():
    df = pd.read_csv('aluguel.csv', sep=';')

    # Exibir os tipos de imóveis e permitir ao usuário escolher
    tipo_escolhido = escolher_tipo_imovel(df)

    # Filtrar o DataFrame e gerar os subplots
    df_tipo_novo = filtrar_imoveis_por_tipo(df, tipo_escolhido)
    print(df_tipo_novo.head())

if __name__ == "__main__":
    main()
