# Projeto AdventureWorks Dashboard

Este projeto é um dashboard interativo para visualização de dados de vendas usando Python, Streamlit, e Plotly. O dashboard se conecta a um banco de dados SQL Server, permitindo análises e visualização de dados em tempo real.

---

## Visão Geral do Projeto

_Bem-vindo ao Dashboard AdventureWorks!_

![Alt text](https://github.com/sanss021/Vendas_AdventureWorks/issues/1)



_Bem-vindo ao Dashboard AdventureWorks!_

Este dashboard foi desenvolvido para simplificar a análise de dados de vendas. Ele oferece uma interface amigável para a visualização de KPIs e gráficos interativos.

---

## Configuração do Ambiente

Para garantir uma instalação organizada e isolada das dependências, siga os passos abaixo para configurar o ambiente.

### 1. Requisitos

- Python 3.x
- Banco de dados SQL Server com o banco de dados AdventureWorks2022
- Permissão de acesso ao servidor SQL Server

### 2. Configuração do Ambiente Virtual

1. **Instale o `virtualenv`** (caso não tenha):

   ```bash
   pip install virtualenv

### Crie um ambiente virtual dentro da pasta do projeto :

```
python3 -m venv venv
```

### Ative o ambiente virtual que está na pasta:

```
venv/scripts/activate 
```


Isso nos permite manter um ambiente limpo e independente para o nosso projeto, garantindo que as dependências sejam gerenciadas de forma eficaz e evitando conflitos com outras aplicações ou projetos em execução em nossa máquina. Com essa base sólida, estamos prontos para exigir a configuração e o desenvolvimento do dashboard.

Instalação das Bibliotecas
Agora que configuramos o ambiente e estamos prontos para avançar, o próximo passo importante é garantir que todas as bibliotecas e dependências estejam instaladas. Fundamental para garantir que nosso projeto funcione sem problemas.

### Você pode usar o seguinte comando para instalar as bibliotecas essenciais para o nosso projeto:

````
pip install streamlit pandas plotly-express
````

### Para simplificar esse processo, podemos usar o comando abaixo para instalar todas as bibliotecas específicas no arquivo requirements.txt, caso você tenha baixado o repositório do tutorial:

````
pip install -r requirements.txt
````

### Install requirements.txt:
For the Python 3 version, the command is:
````
pip3 install -r requirements.txt
````

Essas bibliotecas são fundamentais para criar nosso dashboard de forma eficiente e interativa. O Streamlit é a ferramenta principal que usaremos para construir uma interface, enquanto o Pandas e o Plotly Express nos ajudam a manipular e visualizar os dados de maneira eficaz. Com as bibliotecas instaladas, estamos prontos para continuar!