Configurando o Ambiente
* Coloque o nome do seu servidor no campo SERVER:
* 
def connect_to_database():
    conn = pyodbc.connect(
        r'DRIVER={ODBC Driver 17 for SQL Server};'
        r'SERVER=SEU_SERVIDOR;DATABASE=AdventureWorks2022;Trusted_Connection=yes;'
    )
    return conn
    
Pensando na organização adequada e para garantir que todas as dependências sejam gerenciadas de forma isolada, criamos uma estrutura básica.

Criamos uma pasta dedicada para armazenar todos os arquivos relacionados ao projeto. Dentro dessa pasta, estabelecemos um ambiente virtual, uma prática recomendada no desenvolvimento do Python, que nos permite isolar as bibliotecas e pacotes específicos deste projeto.

Aqui estão os comandos essenciais para criar e ativar o ambiente virtual:

### Instale o virtualenv ( Windons ):

```
pip install virtualenv 
```

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
