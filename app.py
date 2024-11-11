
import pyodbc
import pandas as pd
import plotly.express as px
import streamlit as st

# Função para conectar ao banco de dados AdventureWorks
def connect_to_database():
    conn = pyodbc.connect(
        r'DRIVER={ODBC Driver 17 for SQL Server};'
        r'SERVER=DESKTOP-D41MOQK\SQLEXPRESS;DATABASE=AdventureWorks2022;Trusted_Connection=yes;'
    )
    return conn

# Função para consultar dados de vendas
def query_sales_data(conn):
    query = '''
    SELECT soh.OrderDate, soh.TotalDue, a.StateProvinceID, p.Name AS Product
    FROM Sales.SalesOrderHeader soh
    JOIN Sales.SalesOrderDetail sod ON soh.SalesOrderID = sod.SalesOrderID
    JOIN Person.Address a ON soh.ShipToAddressID = a.AddressID
    JOIN Production.Product p ON sod.ProductID = p.ProductID
    '''
    return pd.read_sql(query, conn)

# Função para processar e agrupar os dados
def process_sales_data(sales_data):
    # Conversão para pandas datetime
    sales_data['OrderDate'] = pd.to_datetime(sales_data['OrderDate'])
    
    # Criar uma coluna de ano e mês
    sales_data['Year'] = sales_data['OrderDate'].dt.year
    sales_data['Month'] = sales_data['OrderDate'].dt.month_name()

    # Vendas totais por região e produto
    sales_by_region_product = sales_data.groupby(['StateProvinceID', 'Product'])['TotalDue'].sum().reset_index()

    # Vendas totais por período (ano e mês)
    sales_by_time = sales_data.groupby(['Year', 'Month'])['TotalDue'].sum().reset_index()

    # Vendas totais por ano e região
    sales_by_year_region = sales_data.groupby(['Year', 'StateProvinceID'])['TotalDue'].sum().reset_index()

    # Garantir que os meses sejam ordenados corretamente (de Janeiro a Dezembro)
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    sales_by_time['Month'] = pd.Categorical(sales_by_time['Month'], categories=month_order, ordered=True)
    sales_by_time = sales_by_time.sort_values(by=['Year', 'Month'])  # Ordenar por ano e mês

    # Criar uma coluna combinada de 'Ano-Mês' para melhor visualização no eixo X
    sales_by_time['Year-Month'] = sales_by_time['Year'].astype(str) + '-' + sales_by_time['Month'].astype(str)

    return sales_by_region_product, sales_by_time, sales_data, sales_by_year_region

# Função para criar gráfico de barras de vendas por produto
def plot_sales_by_product(sales_by_region_product, selected_products, selected_regions):
    filtered_data = sales_by_region_product[sales_by_region_product['Product'].isin(selected_products)]
    filtered_data = filtered_data[filtered_data['StateProvinceID'].isin(selected_regions)]
    
    fig = px.bar(filtered_data, 
                 x='Product', 
                 y='TotalDue', 
                 color='StateProvinceID', 
                 title="Vendas por Produto e Região",
                 labels={'TotalDue': 'Valor Total', 'Product': 'Produto'},
                 color_continuous_scale='Plasma')
    fig.update_layout(
        plot_bgcolor='#F4F4F4',
        paper_bgcolor='#FFFFFF',
        title_x=0.5,
        title_font=dict(size=16, color='black', family='Arial, sans-serif'),
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor='lightgray', zeroline=True)
    )
    return fig

# Função para criar gráfico de linhas de vendas ao longo do tempo
def plot_sales_over_time(sales_by_time, selected_years):
    sales_filtered = sales_by_time[sales_by_time['Year'].isin(selected_years)]

    fig = px.line(sales_filtered, 
                  x='Year-Month', 
                  y='TotalDue', 
                  color='Year', 
                  title="Vendas ao Longo do Tempo",
                  labels={'TotalDue': 'Valor Total', 'Year-Month': 'Ano-Mês'},
                  markers=True)
    fig.update_layout(
        plot_bgcolor='#F4F4F4',
        paper_bgcolor='#FFFFFF',
        title_x=0.5,
        title_font=dict(size=16, color='black', family='Arial, sans-serif'),
        xaxis=dict(showgrid=True, gridcolor='lightgray', tickangle=45),
        yaxis=dict(showgrid=True, gridcolor='lightgray', zeroline=True)
    )
    return fig

# Função para criar gráfico de vendas por ano e região
def plot_sales_by_year_region(sales_by_year_region, selected_years):
    filtered_data = sales_by_year_region[sales_by_year_region['Year'].isin(selected_years)]

    fig = px.bar(filtered_data, 
                 x='Year', 
                 y='TotalDue', 
                 color='StateProvinceID', 
                 title="Vendas por Ano e Região",
                 labels={'TotalDue': 'Valor Total', 'StateProvinceID': 'Região'},
                 barmode='stack')
    fig.update_layout(
        plot_bgcolor='#F4F4F4',
        paper_bgcolor='#FFFFFF',
        title_x=0.5,
        title_font=dict(size=16, color='black', family='Arial, sans-serif'),
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor='lightgray', zeroline=True)
    )
    return fig

# Função para construir o painel de controle
def build_dashboard():
    st.set_page_config(page_title="Dashboard de Vendas AdventureWorks", layout='wide')
    st.title("📊 Dashboard de Vendas AdventureWorks")

    # Estilo global
    st.markdown("""
        <style>
            .css-1v3fvcr {font-size: 18px;}
            .css-16q4fez {font-weight: bold;}
        </style>
    """, unsafe_allow_html=True)

    # Conectar ao banco de dados
    conn = connect_to_database()

    # Obter dados de vendas
    sales_data = query_sales_data(conn)

    # Processar os dados
    sales_by_region_product, sales_by_time, sales_data_processed, sales_by_year_region = process_sales_data(sales_data)

    # Filtros interativos
    st.sidebar.header("Filtros")
    
    # Filtro para período
    years = sales_data['Year'].unique()
    selected_years = st.sidebar.multiselect("Selecione o(s) Ano(s)", options=years, default=years)
    
    # Filtro para produto
    products = sales_data['Product'].unique()
    selected_products = st.sidebar.multiselect("Selecione o(s) Produto(s)", options=products, default=products)

    # Filtro para região
    regions = sales_data['StateProvinceID'].unique()
    selected_regions = st.sidebar.multiselect("Selecione a(s) Região(ões)", options=regions, default=regions)
    
    # Filtrar os dados de acordo com os filtros selecionados
    filtered_sales = sales_data_processed[sales_data_processed['Year'].isin(selected_years)]
    filtered_sales = filtered_sales[filtered_sales['Product'].isin(selected_products)]
    filtered_sales = filtered_sales[filtered_sales['StateProvinceID'].isin(selected_regions)]

    # KPIs: Vendas Totais, Ticket Médio e Número Total de Vendas
    total_sales = filtered_sales['TotalDue'].sum()
    num_sales = filtered_sales.shape[0]
    avg_ticket = total_sales / num_sales if num_sales else 0

    # Exibir KPIs
    kpi_col1, kpi_col2, kpi_col3 = st.columns(3)
    kpi_col1.metric(label="Vendas Totais", value=f"R$ {total_sales:,.2f}")
    kpi_col2.metric(label="Ticket Médio", value=f"R$ {avg_ticket:,.2f}")
    kpi_col3.metric(label="Número de Vendas", value=f"{num_sales}")

    # Layout em duas colunas com quatro gráficos
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Vendas por Produto")
        fig_product = plot_sales_by_product(sales_by_region_product, selected_products, selected_regions)
        st.plotly_chart(fig_product)

        st.subheader("Vendas ao Longo do Tempo")
        fig_time = plot_sales_over_time(sales_by_time, selected_years)
        st.plotly_chart(fig_time)

    with col2:
        st.subheader("Vendas por Ano e Região")
        fig_year_region = plot_sales_by_year_region(sales_by_year_region, selected_years)
        st.plotly_chart(fig_year_region)

        st.subheader("Tabela de Vendas")
        table_data = filtered_sales[['OrderDate', 'TotalDue', 'StateProvinceID', 'Product']]
        table_data['OrderDate'] = table_data['OrderDate'].dt.strftime('%Y-%m-%d')
        st.dataframe(table_data)

    # Fechar a conexão
    conn.close()

# Executar o dashboard
if __name__ == "__main__":
    build_dashboard()
