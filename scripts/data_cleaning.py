import pandas as pd


def load_data(filepath):
    """Load sales data from a CSV file."""
    return pd.read_csv(filepath)


def clean_data(df):
    """Clean sales data."""
    # Exemplo de limpeza de dados:
    # Remover colunas desnecessárias
    df = df.drop(columns=['UnnecessaryColumn1', 'UnnecessaryColumn2'])
    
    # Tratar valores ausentes
    df = df.dropna(subset=['ImportantColumn'])
    
    # Converter tipos de dados
    df['Date'] = pd.to_datetime(df['Date'])
    
    return df


if __name__ == "__main__":
    # Caminho para o arquivo CSV
    filepath = '../data/sales_data.csv'
    
    # Carregar os dados
    df = load_data(filepath)
    
    # Limpar os dados
    df = clean_data(df)
    
    # Salvar os dados limpos
    df.to_csv('../data/cleaned_sales_data.csv', index=False)
