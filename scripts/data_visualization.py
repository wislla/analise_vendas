import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_sales_over_time(df):
    """Plot total sales over time."""
    df.set_index('Date', inplace=True)
    df.resample('M')['Sales'].sum().plot()
    plt.title('Total Sales Over Time')
    plt.ylabel('Sales')
    plt.xlabel('Date')
    plt.show()


def plot_sales_by_category(df):
    """Plot sales by category."""
    sns.barplot(x='Category', y='Sales', data=df)
    plt.title('Sales by Category')
    plt.ylabel('Sales')
    plt.xlabel('Category')
    plt.show()
    

if __name__ == "__main__":
    # Carregar os dados limpos
    df = pd.read_csv('../data/cleaned_sales_data.csv')
    
    # Plotar vendas ao longo do tempo
    plot_sales_over_time(df)
    
    # Plotar vendas por categoria
    plot_sales_by_category(df)
