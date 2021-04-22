## Histórico de Versões

| Versão  |  Data  | Autor  |  Descrição  |
| ------------------- | ------------------- | ------------------- | ------------------- |
| 1.0.0 | 17/02/2021  | Davi Matheus  | Estrutura inicial  |
| 1.0.1 | 17/02/2021  | Nilvan Peres  | Adição dos tópicos 1,2 e 3 |
| 1.0.2 | 25/02/2021  | Antonio e Arthur | Implementação da Visão de Dados |
| 1.0.3 | 25/02/2021  | Natanel Fernandes | Adição do DER |
| 1.0.4 | 25/02/2021  | Davi e Aabrão | Implementação da Visão de Caso de Uso |
| 1.1.0 | 04/03/2021  | Davi e Aabrão | Atualização da Visão de Caso de Uso |
| 1.1.1 | 04/03/2021  | Antônio e Arthur | Atualização da Visão de Dados |
| 1.1.2 | 09/03/2021  | Nilvan Peres | Atualização link's sumários |
| 1.1.3 | 10/03/2021  |Lucas Lima | Adição do MTV ao Padrão Arquitetural |
| 1.2.0 | 14/03/2021  | Antônio | Atualização geral do documento |  
| 1.2.1 | 15/03/2021  | Davi | Atualização do topico 5 | 
| 1.2.2 | 16/03/2021  | Lucas Lima | Atualização no tópico 2.2 |
| 1.2.3 | 23/03/2021  | Lucas Lima | Adição dos tópicos 6, 7 e 8 |
| 1.2.4 | 24/03/2021  | Arthur Talles | Adição do tópico 2.3 |
| 1.2.5 | 25/03/2021  | Davi Matheus | Mudanças no diagrama casos de Uso |
| 2.0.0.| 11/04/2021  | Davi Matheus | Adição da documenação do Django Rest |
| 2.0.1 | 11/04/2021  | Arthur Talles | Adição da documentação do React |
## Sumário
[1 - Introdução](#1---introdução)
* [1.1 - Objetivo](#1.1---objetivo)
* [1.2 - Escopo](#1.2---escopo)
* [1.3 - Visão Geral](#1.3---Visão-Geral)
* [1.4 - Definições, acrônimos e abreviações](#1.4---Definições,-acrônimos-e-abreviações)

[2 - Represetanção de Arquitetura](#2---Represetanção-de-Arquitetura)

* [2.1 - Padrão Arquitetural](###2.1---Padrão-Arquitetural)
* [2.2 - Tecnologias](#2.2---Tecnologias)
* [2.3 - Diagrama de Pacotes](#2.3---Diagrama-de-Pacote)

[3 - Metas e Restrições da Arquitetura](#3---Metas-e-Restrições-da-Arquitetura)

* [3.1 - Metas](#3.1---Metas)
* [3.2 - Restrições da Arquitetura](#3.2---Restrições-da-Arquitetura)

[4 - Visão de Dados](#4---Visão-de-Dados)
* [4.1 - Modelo Entidade Relacionamento (MER)](#4.1---Modelo-Entidade-Relacionamento-(MER)) 
    * [4.1.1 - Entidades](#4.1.1---Entidades)
    * [4.1.2 - Relacionamentos](#4.1.2---Relacionamentos)
* [4.2 - Diagrama Entidade Relacionamento (DER)](#4.2---Diagrama-Entidade-Relacionamento-(DER)) 

[ 5 - Visão de Caso de Uso](#5---Visão-de-Caso-de-Uso)

* [5.1 - Diagrama de caso de Uso](#5.1---Diagrama-de-caso-de-Uso)
* [5.2 - Atores de Caso de Uso](#5.2---Atores-de-Caso-de-Uso)
* [5.3 - Descrições de Caso de Uso](#5.3---Descrições-de-Caso-de-Uso)

[ 6 - Visão Lógica](#6---Visão-Lógica)

[ 7 - Tamanho e Desempenho](#7---Tamanho-e-Desempenho)
* [7.1 - Tamanho](#7.1---Tamanho)
* [7.2 - Desempenho](#7.2---Desempenho)

[ 8 - Qualidade](#8---Qualidade)
## 1 - Introdução

### 1.1 - Objetivo 
O objetivo deste documento é dissecar a arquitetura do projeto ***Cheery Up***, de modo que, todo a visão arquitetural do sistema que será desenvolvido esteja clara.  
Outro ponto que será abordado, são as principais características do software permitindo que desenvolvedores/gestores entendam os processos que levaram na escolha das tecnologias e decisões a respeito dessa arquitetura.

### 1.2 - Escopo
A plataforma web ***Cheery Up***, desenvolvida para psicólogos e profissionais da saúde psicológica, será um prontuário de monitoramento da saúde mental da uma comunidade. Nessa plataforma, o psicólogo se cadastra e tem acesso à ferrramentas que irão facilitar o monitoramento da saúde mental de cada paciente que desejar cadastrar, além do usufruto de Dashboards para a observação geral da comunindade. Também há o business inteligence a partir dos dados inseridos pelos psicológos.
Os componenete de software, frameworks, plataformas de desenvolvimento utilizados serão descritos neste documento.

### 1.3 - Visão Geral
Este documento é dividio nas seguintes seções:
* Introdução: Explica o propósito e organização do documento.
* Representação Arquitetural: Apresenta a arquitetura adotada para desenvolver o projeto.
* Metas e Requisitos de Software: Destrincha os requisistos de usabilidade do software, e as metas mais relevantes para o sistema que será desenvolvido.
* Visão de dados: Apresentação de todos os dados e métricas da aplicação.
* Visão de Casos de uso: Apresentação de todos os casos de uso da aplicação.
* Referências bibliográficas: Material de apoio na elaboração desse documento

### 1.4 - Definições, acrônimos e abreviações

| **Sigla/Termo/Acrônimo** | **Definição** |
| ------------------------ | ------------- |
| API | Application Programming Interface | 
| OMR | Mapeamento de objeto Relacional | 
| MDS | Métodos de Desenvolvimento de Software | 
| EPS | Engenharia de Produto de Software| 
| FGA | Faculdade do Gama | 
| UnB | Universidade de Brasília | 
| DRF | Django Rest Framework |
| MTV | Model Template View |
| MVC | Model View Controller |

## 2 - Represetanção de Arquitetura
<p align="center">
	<img src="../../assets/diagrama/ImagemArquitetura.png" width="60%" height="30%">
</p>


### 2.1 - Padrão Arquitetural

### 2.1.1 Back-end 
####  Django 

O padrão de aquitetura MVC (Modelo Visão e Controle) é um modelo que contribui na otimização da velocidade entre as requisições feitas pelo comando do usuário. Cada componente da arquitetura é construído para lidar com alguma parte específica do desenvolvimento da aplicação. Os três componentes que serão utilizados nesse projeto serão destrinchados abaixo: 
* Model: Esse componente armazena dados, e está relacionado com a parte lógica. Essa parte será desempenhada pelos framework Django e com o mySQL para a manipulação de dados;
* View: É parte da aplicação que será visível ao usuário, a apresentação dos dados. A ferramenta que fará isso no nosso projeto é o react.js;
* Controller: É parte que lida com a interação do usuário com a aplicação, ele interpreta as inputs do usuário, comunica a model e a view muda de acordo as mudanças feitas.

O Django utiliza o MTV (Modelo de template e visão). Toda esta arquitetura é interligada e conversam entre si. Uma depende da outra para realizar um determinado serviço e, no final, executar a tarefa que o usuário solicitou. Quando o usuário faz uma requisição pelo browser, utilizando uma rota, é executado um método das Views, que utiliza os Models para acessar o banco de dados e retornar as informações. Estas informações são renderizadas pela camada de Template e, finalmente, é renderizado para o usuário pelo navegador.
* Model: Mapeamento do banco de dados para o projeto;
* Template: Páginas para visualização de dados. Normalmente, é aqui que fica o HTML que será renderizado nos navegadores;
* View: Lógica de negócio. É aqui que determinamos o que irá acontecer em nosso projeto.

#### Django Rest Framework

A estrutura Django REST é um kit de ferramentas poderoso e flexível para a construção de APIs da Web, em que o foco do nosso projeto  é desenvolver uma web API's de forma mais simples e ágil fatores importantíssimos devido ao pouco tempo de curso, em que, segundo a documentação oficial, o Django Rest gera uma API navegável que auxilia na usabilidade para os desenvolvedores. Além disso, possui um sistema de autenticação e serialização dos dados, esse é um dos motivos que o nosso grupo optou  para usar o Django REST Framework, porque ele torna a serialização mais fácil. 

O Django Rest funciona como um complemento ao Django, isso significa que é necessária a instalação do Django, e consequentemente, do Rest Framework.

### 2.1.2 Front-end
###  React JS

React JS é uma biblioteca JavaScript para a criação de interfaces de usuário — ou UI (user interface).

Criado em 2011 pelo time do Facebook, o React surgiu com o objetivo de otimizar a atualização e a sincronização de atividades simultâneas no feed de notícias da rede social, entre eles chat, status, listagem de contatos e outros.

A princípio, todas essas atividades, chamadas de estados, tinham uma descrição muito complexa. Com o React, esta descrição torna-se mais simples, bem como também é simplificada a conexão entre HTML, CSS e JavaScript e todos os componentes de uma página.

O JS é uma das mais versáteis e populares linguagens de programação do mundo e conta com um grande número de bibliotecas e outras tecnologias que a utilizam. Entre elas, Node.js, Angular, VueJS, jQuery, Ember.js e, é claro, o React.

Por essa razão, se você quer aprender a manipular esta biblioteca e extrair dela todo o seu potencial, é preciso antes ter uma sólida base de conhecimento em JavaScript, bem como em suas outras duas linguagens de marcação: HTML e CSS.


### 2.2 - Tecnologias
|tecnologias | descrição |
| ------------------- | ------------------- |
| Python | Linguagem para o desenvolvimento do backend |
| Django | Framework que segue a arquitetura MTV, fará comunicação do back com o banco de dados |
| Django Rest | Framework para criação de API's Web |
| MkDocs | Gerador de site estático, voltado a criação de documentações markdown
|Bootstrap |  Framework para desenvolvimento em HTML e JS. |
| React |  Biblioteca em javascript com foco em criar inteface de usuário em páginas web. |
|Docker | Criação e administração de ambientes de desenvolvimento |
|Docker-compose |  Para a comunicação dos containers criados pelo docker |
|Git | Git é um sistema de controle de versão distruibuído, com estímulos a projetos open source |
|HTML |  Será utiliza para implementação do frontend junto ao JS e CSS |
|CSS | Linguagem para estilização de uma interface web |
|JavaScript |  Alia-se no desenvolvimento do frontend junto com HTML e CSS|
|mySQL | Banco de dados relacional, será usado para gerir a base de dados|

### 2.3 Diagrama de Pacotes

  <p align="center">
	<img src="../../assets/diagrama/Diagrama Pacote Back-end e Front-end.png" width="90%" height="90%">
</p>

* Front-end

*  React JS: biblioteca JavaScript para a criação de interfaces de usuário — ou UI (user interface).
    * Public: pacote mais externo, que contém um mais interno, "Images", responsável pelo armazenamento de imagens a serem utilizadas na realização do projeto.
    * Components: pacote mais externo, que contém um mais interno, "Forms", responsável pelas funcionalidades relativas aos formulários a serem utilizados na realização do projeto.
    * Style: pacote mais externo, que contém um mais interno, "CSS", responsável pelo armazenamento de arquivos relacionados à personalização do conteúdo visível.
    * Tests: pacote responsável pelo armazenamento de informações relativas aos testes unitários a serem realizados durante o projeto.
    * Screen: pacote mais externo, que contém um mais interno, "Pages", responsável pelo armazenamento do conteúdo que produzirá, efetivamente, a interação com o usuário por meio das páginas web.
    * Docker-Compose: conjunto de containers dockers. 

* Backend

* Django REST API: framework para criação de API's Web.

	* settings.py: o arquivo ou modulo settings.py contém a configuração do nosso project, ele que armazena as configurações da base de dados, timezone, e aplicativos externos baixados.
	* urls.py: armazena entry-points e endpoints da API.
	* app: diretório constituído de models, viewsets, testes, urls, serializers e admin.
	* models: arquivo de models do app, ele contém os campos e comportamentos essenciais dos dados que você armazena. 
	* views: arquivo de views do app.
	* urls: mapeia as views com template de cada app.
	* serializer: Os Serializers permitem que dados complexos, como querysets e model instances, sejam convertidos em tipos de dados Python nativos que podem ser facilmente renderizados, no nosso caso o JSON.
	* admin: arquivo de conexão do app com o admin padrão do Django.
	* Docker-Compose: conjunto de containers dockers.
	* PostgreSQL: banco de dados da aplicação.

### 3 - Metas e Restrições da Arquitetura

#### 3.1 - Metas
* Facilitar o acompanhamento psicológico;
* Automatizar registros de atendimentos;
* Acompanhamento no quadro de evolução dos pacientes;
* Dashboards com métricas e indicadores da saúde mental de determinada comunidade; 

#### 3.2 - Restrições da Arquitetura
* Ter acesso a internet;
* Possuir um navegador de internet (Google Chrome 60, Safari, Mozilla Firefox 55, Opera 47 e Microsoft Edge);
* Cadastro no site;

## 4 - Visão de Dados

### 4.1 - Modelo Entidade Relacionamento (MER)

### 4.1.1 - Entidades
* ### Psicólogo 
|Atributos| Propriedade | Tipo | Descrição|
|-----|-----|------|-----|
| idPsicologo | Chave primária obrigatória | Integer | Identificação do Psicólogo |
| nome | Obrigatório | String | Nome do Psicólogo |
| email | Obrigatório | String | Email do Psicólogo |
| nCRP | Obrigatório | Integer | Número do Conselho Regional do Psicólogo |
| senha | Obrigatório | String | Senha de login |
| listaPacientes | Optativo | Paciente | Lista de pacientes do psicólogo|

* ### Paciente
|Atributos| Propriedade | Tipo | Descrição|
|-----|-----|------|-----|
| idPaciente | Chave primária obrigatória | Integer | Identificação do paciente |
| idPsicologo | Chave estrangeira obrigatória | Integer | Identificação do psicólogo |
| nome | Obrigatório | String | Nome do paciente |
| nascimento | Obrigatório | Date | Data de nascimento do paciente |
| genero | Obrigatório | Char | Gênero do paciente |
| regiao | Obrigatório | String | Região onde mora o paciente |
| descricao | Optativo | String | Descrição do caso do paciente |
| listaConsulta | Optativo | Consulta | Lista das consultas do paciente |


* ### Consulta
|Atributos| Propriedade | Tipo | Descrição|
|-----|-----|------|-----|
| idConsulta | Chave primária obrigatória | Integer | Identificação da Consulta |
| idPaciente | Chave estrangeira obrigatória | Integer | Identificação do Paciente |
| idPsicologo | Chave estrangeira obrigatória | Integer | Identificação do Psicólogo |
| dataConsulta| Obrigatório | String| Data que ocorre a consulta |
| situacaoPaciente | Obrigatório | String | Situação mental do paciente problema |
### 4.1.2 - Relacionamentos

**Psicólogo** -- cadastra/exclui -- **Paciente**: Um psicólogo cadastra ou exclui os pacientes. (Cardinalidade 1:N)

**Psicólogo** -- cadastra/exclui -- **Psicólogo**: Um psicólogo realiza seu próprio cadastro e eventual exclusão do mesmo. (Cardinalidade 1:1)

**Psicólogo** -- cadastra/exclui -- **Consulta**: Psicólogo cadastra ou exclui consultas de um paciente. (Cardinalidade 1:N)

**Psicólogo** -- insere -- **Paciente**: Psicólogo insere novos dados de uma consulta com paciente. (Cardinalidade 1:N)

**Psicólogo** -- acessa -- **Consulta**: Psicólogo altera dados de uma consulta com paciente. (Cardinalidade 1:N)

**Psicólogo** -- acessa -- **Paciente**: Psicólogo acessa seus pacientes e respectivos dados. (Cardinalidade 1:N)


### 4.2 - Diagrama Entidade Relacionamento (DER)

<p align="center">
	<img src = "../../assets/diagrama/DER.png" width="60%" height="60%">
</p>


## 5 - Visão de Caso de Uso

### 5.1 - Diagrama de caso de Uso

<p align="center">
	<img src = "../../assets/diagrama/Caso_De_Uso.png"  width="80%" height="80%">
</p>


### 5.2 - Atores de Caso de Uso

|Ator | Descrição | 
|-----|-----|
| Usúario | São todos que forem utilizar o site, ou seja, o psicólogo | 
| Psicologo | É quem vai utilizar o site para o cadastro e gerenciamento do paciente, visualizar o laudo e acessar os dashboards  | 

### 5.3 - Descrições de Caso de Uso

|Casos de uso| Ator | Descrição|
|-----|-----|------|
| UC01 - Editar Dados da Conta | Psicologo | O psicologo poderá realizar seu cadastro e dar login e logout na plataforma quando quiser |
| UC02 - Acesar a Pagina do Psicologo | Psicologo | O psicologo poderá acessar a pagina cadastra, fazer o login e realizar as determinadas funções presentes no site.
| UC03 - Cadastrar/Exlcluir paciente | Psicologo | O psicólogo poderá acessar cadastrar ou exluir um paciente em específico |
| UC04 - Alterar dados do  Paciente| Psicologo | O psicologo poderá alterar o perfil dos seus pacientes quando desejar |
| UC05 - listar Pacientes | Psicologo |  O psicólogo poderá acessar e visualizar as informações de um paciente em específico   |
| UC06 - Acessar consulta dos pacientes | Psicologo | O psicólogo poderá acessar as consultas que ele preencher |
| UC07 - Alterar relatorio Consulta | Psicologo | O psicólogo podera alterar os dados da consulta |
| UC08 - Acessar Dashboards |  Psicologo | O psicólogo poderá ver os dashbords de saúde mental disponiblizados pela comunidade |

## 6 - Visão Lógica

O psicólogo acessa o site através de um computador ou celular, realiza seu cadastro com CRP, faz o login, cadastra seus pacientes e atualiza os dados. Após ter os dados atualizados com as informações adquiridas na consulta, são gerados relatórios com infográficos.\
Os dados do psicólogo e dos clientes serão armazenados no banco de dados. No momento em que o psicólogo atualizar os dados, automaticamente os infográficos serão gerados e disponibilizados para que sejam vistos. 

## 7 - Tamanho e Desempenho
### 7.1 - Tamanho
O software é feito para rodar diretamente no navegador, sem qualquer tipo de instalação fora o próprio navegador.

### 7.2 - Desempenho
Basicamente todas as ações realizadas no front-end enviam requisições ao back-end para serem feitas. Por exemplo, no cadastro do psicólogo é feita uma requisição ao back-end para guardar os dados no banco de dados e utilizar posteriormente. Não há requisitos computacionais para que o site seja aberto.

## 8 - Qualidade
O site terá uma interface simples, facilitando o acesso para qualquer pessoa, mesmo que ela não tenha muita facilidade com tecnologia, e garantindo a plena funcionalidade proposta. Nada do back-end será mostrado ao psicólogo, apenas a parte inteligível do front-end.

## Referências 

>  Django Documentation. Disponivel em: < [https://docs.djangoproject.com/en/3.1/](https://docs.djangoproject.com/en/3.1/) > Acesso em: 17 de Fevereiro de 2021 

> React Documentation. Disponivel em: < [https://pt-br.reactjs.org/docs/getting-started.html](https://pt-br.reactjs.org/docs/getting-started.html) > Acesso em: 17 de Fevereiro de 2021

> About PostgreSQL. Disponível em: < [https://www.postgresql.org/about/](https://www.postgresql.org/about/) > Acesso em 17 de Março de 2021

> Documento de arquitetura Acácia. Disponível em: < [https://fga-eps-mds.github.io/2019.2-Acacia/#/architecture_document](https://fga-eps-mds.github.io/2019.2-Acacia/#/architecture_document) > Acesso em: 25 de Fevereiro de 2021

> Documento de arquitetura ArBC. Disponível em: < [ https://jlucassr.github.io/ArBC-Pages/mds/Documento_de_arquitetura/ ](https://jlucassr.github.io/ArBC-Pages/mds/Documento_de_arquitetura/) > Acesso em: 25 de Fevereiro de 2021

> Quickstart - Django REST framework. Disponivel em: < [https://www.django-rest-framework.org/tutorial/quickstart/](https://www.django-rest-framework.org/tutorial/quickstart/) > acesso em: 25 de Fevereiro de 2021

> Introdução ao Django REST framework. Disponivel em : <[https://nelziositoe.medium.com/introducao-ao-django-rest-framework-47ecb9ae0e6b](https://nelziositoe.medium.com/introducao-ao-django-rest-framework-47ecb9ae0e6b) > acesso em : 10 de abril de 2021 
