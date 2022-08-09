# Job Insights
Neste projeto é  implementada análises a partir de um conjunto de dados sobre empregos. As implementações serão incorporadas a um aplicativo Web desenvolvido com Flask. E são feitos testes para a implementação de uma análise de dados.
Os dados foram extraídos do site [Glassdoor](https://www.glassdoor.com.br/) e obtidos através do [Kaggle](https://www.kaggle.com/atharvap329/glassdoor-data-science-job-data), uma plataforma disponiblizando conjuntos de dados para cientistas de dados.

  🚵 Habilidades trabalhadas:
  <ul>
    <li>Utilizar o terminal interativo do Python.</li>
    <li>Utilizar estruturas condicionais e de repetição.</li>
    <li>Utilizar funções built-in do Python.</li>
    <li>Utilizar tratamento de exceções.</li>
    <li>Realizar a manipulação de arquivos.</li>
    <li>Escrever funções.</li>
    <li>Escrever testes com Pytest.</li>
    <li>Escrever módulos e importá-los em outros códigos.</li>
  </ul>
</details>

<details>
  <summary><strong>🎛 Linter</strong></summary><br />

  Para garantir a qualidade do código, vamos utilizar neste projeto o linter `Flake8`.
  Assim o código estará alinhado com as boas práticas de desenvolvimento, sendo mais legível
  e de fácil manutenção! Para rodá-lo localmente no projeto, execute o comandos abaixo:

  ```bash
  python3 -m flake8
  ```

</details>

<details>
  <summary><strong>🏕️ Ambiente Virtual</strong></summary><br />
  O Python oferece um recurso chamado de ambiente virtual, onde permite sua máquina rodar sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

  1. **criar o ambiente virtual**

  ```bash
  $ python3 -m venv .venv
  ```

  2. **ativar o ambiente virtual**

  ```bash
  $ source .venv/bin/activate
  ```

  3. **instalar as dependências no ambiente virtual**

  ```bash
  $ python3 -m pip install -r dev-requirements.txt
  ```

  Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
  Quando precisar desativar o ambiente virtual, execute o comando "deactivate". Lembre-se de ativar novamente quando voltar a trabalhar no projeto.

  O arquivo `dev-requirements.txt` contém todas as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`.
</details>
<details>
  <summary><strong>🛠 Testes</strong></summary><br />

  Para executar os testes certifique-se de que você está com o ambiente virtual ativado.

  <strong>Executar os testes</strong>

  ```bash
  $ python3 -m pytest
  ```

  O arquivo `pyproject.toml` já configura corretamente o pytest. Entretanto, caso você tenha problemas com isso e queira explicitamente uma saída completa, o comando é:

  ```bash
  python3 -m pytest -s -vv
  ```

  Caso precise executar apenas um arquivo de testes basta executar o comando:

  ```bash
  python3 -m pytest tests/nomedoarquivo.py
  ```

  Caso precise executar apenas uma função de testes basta executar o comando:

  ```bash
  python3 -m pytest -k nome_da_func_de_tests
  ```

  Se desejar que os testes parem de ser executados quando acontecer o primeiro erro, use o parâmetro `-x`

  ```bash
  python3 -m pytest -x tests/test_jobs.py
  ```
  
  Para executar um teste específico de um arquivo, basta executar o comando:

  ```bash
  python3 -m pytest tests/nomedoarquivo.py::test_nome_do_teste
  ```

</details>

# Requisitos
<i> Parte do código foi desenvolvido pela Trybe, como pode ser visto no histórico de commits, porém a resolução dos requisitos foi feita por mim</i>
## 1 - Função `read`
> **Em:** src/jobs.py

Para começarmos a processar os dados, devemos antes carregá-los em nossa aplicação. Esta função será responsável por abrir o arquivo CSV e retornar os dados no formato de uma lista de dicionários.

- A função deve receber um _path_ (uma string com o caminho para um arquivo).
- A função deve abrir o arquivo e ler seus conteúdos.
- A função deve tratar o arquivo como CSV.
- A função deve retornar uma lista de dicionários, onde as chaves são os cabeçalhos de cada coluna e os valores correspondem a cada linha.

<details>
  <summary>
    <b>📝Exemplo</b>
  </summary>
  Se o conteúdo do arquivo for:
  
```
nome,cidade,telefone
Ana,Curitiba,1111111
Bernardo,Santos,999999
```

  O retorno da função deverá ser: 
  
```python
  [
    {"nome": "Ana", "cidade": "Curitiba", "telefone": "1111111"},
    {"nome": "Bernardo", "cidade": "Santos", "telefone": "999999"}
  ]
```
</details> 

<details>
  <summary>
    <b>✍️ Teste manual</b>
  </summary>
  Abra um terminal Python importando estas funções através do comando <code>python3 -i src/jobs.py</code> e invoque a função utilizando diferentes _paths_.
</details>


## 2 - Função `get_unique_job_types`
> **Em:** `src/insights.py`

Agora que temos como carregar os dados, podemos começar a extrair informação deles. Primeiro, vamos identificar quais tipos de empregos existem.

- A função deve receber o _path_ do arquivo csv com os dados.
- A função deve invocar a função `jobs.read` com o _path_ recebido para obter os dados.
- A função deve retornar uma lista de valores únicos presentes na coluna `job_type`.

## 3 - Função `get_unique_industries`
> **Em:** `src/insights.py`

Da mesma forma, agora iremos identificar quais indústrias estão representadas nesse conjunto de dados.

- A função deve obter os dados da mesma forma que o requisito 2.
- A função deve retornar uma lista de valores únicos presentes na coluna `industry`.
- A função desconsidera valores vazios


## 4 - Função `get_max_salary`
> **Em:** `src/insights.py`

Os dados apresentam faixas salariais para cada emprego exibido. Vamos agora encontrar o maior valor de todas as faixas.

- A função deve obter os dados da mesma forma que o requisito 2.
- A função deve ignorar os valores ausentes.
- A função deve retornar *um valor inteiro* com o maior salário presente na coluna `max_salary`.


## 5 - Função `get_min_salary`
> **Em:** `src/insights.py`

Os dados apresentam faixas salariais para cada emprego exibido. Vamos agora encontrar o menor valor de todas as faixas.

- A função deve obter os dados da mesma forma que o requisito 2.
- A função deve ignorar os valores ausentes.
- A função deve retornar *um valor inteiro* com o menor salário presente na coluna `min_salary`.


## 6 - Função `filter_by_job_type`

> **Implemente em:** `src/insights.py`

Os empregos estão listados em um aplicativo web. Para permitir que a pessoa usuária possa filtrar os empregos por tipo de emprego, vamos precisar implementar esse filtro.

- A função deve receber uma lista de dicionários `jobs` como primeiro parâmetro.
- A função deve receber uma string `job_type` como segundo parâmetro.
- A função deve retornar uma lista com todos os empregos onde a coluna `job_type` corresponde ao parâmetro `job_type`.


## 7 - Função `filter_by_industry`
> **Em:** `src/insights.py`

Do mesmo modo, o aplicativo precisa permitir uma filtragem por indústria. Vamos precisar implementar esse filtro também.

- A função deve receber uma lista de dicionários `jobs` como primeiro parâmetro.
- A função deve receber uma string `industry` como segundo parâmetro.
- A função deve retornar uma lista de dicionários com todos os empregos onde a coluna `industry` corresponde ao parâmetro `industry`.


## 8 - Função `matches_salary_range`
> **Em:** `src/insights.py`

O aplicativo vai precisar filtrar os empregos por salário também. Como uma função auxiliar, implemente `matches_salary_range` para conferir que o salário procurado está dentro da faixa salarial daquele emprego. Vamos aproveitar também para conferir se a faixa salarial faz sentido -- isto é, se o valor mínimo é menor que o valor máximo.

- A função deve receber um dicionário `job` como primeiro parâmetro, com as chaves `min_salary` e `max_salary`.
- A função deve receber um inteiro `salary` como segundo parâmetro.
- A função deve lançar um erro `ValueError` nos seguintes casos:
  - alguma das chaves `min_salary` ou `max_salary` estão *ausentes* no dicionário;
  - alguma das chaves `min_salary` ou `max_salary` tem valores não-numéricos;
  - o valor de `min_salary` é maior que o valor de `max_salary`;
  - o parâmetro `salary` tem valores não numéricos;
- A função deve retornar `True` se o salário procurado estiver dentro da faixa salarial ou `False` se não estiver.


## 9 - Função `filter_by_salary_range`
> **Implemente em:** `src/insights.py`

Agora vamos implementar o filtro propriamente dito. Para esta filtragem, podemos usar a função auxiliar implementada no requisito anterior -- tomando o cuidado de descartar os empregos que apresentarem faixas salariais inválidas.

- A função deve receber uma lista de dicionários `jobs` como primeiro parâmetro.
- A função deve receber um inteiro `salary` como segundo parâmetro.
- A função deve ignorar os empregos com valores inválidos para `min_salary` ou `max_salary`.
- A função deve retornar uma lista com todos os empregos onde o salário `salary` estiver entre os valores da coluna `min_salary` e `max_salary`.


## 10 - Teste para a função `count_ocurrences`
> **Em:** `tests/counter/test_counter.py`

A empresa cliente contratou um relatório que informa a quantidade de ocorrências das palavra *Python* e *Javascript* nos dados e, para isso, temos uma implementação pronta em `src/counter.py`. Durante o desenvolvimento, sofremos com alguns `bugs`, que já foram resolvidos. Para termos certeza e confiança da nossa entrega, no entanto, e não corrermos riscos, precisaremos de *testes automatizados* que garantam isso!

O nome deste teste **deve** ser `test_counter`, e ele deve garantir que atenda estas especificações:

- **Chamar** a função `count_ocurrences` passando dois parâmetros:
  - `path` uma string com o caminho do arquivo (`src/jobs.csv`);
  - `word` uma string com a palavra a ser contabilizada.
- Garantir que a função retorna corretamente a quantidade de ocorrências da palavra solicitada 
  - A contagem de palavras deve ser _case insentitive_, ou seja, não diferenciar letras maiúsculas de minúsculas


