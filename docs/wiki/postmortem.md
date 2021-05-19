# Post Mortem

## Histórico de revisão

| Data   | Versão | Modificação  | Autor  |
| :- | :- | :- | :- |
| 12/05/2021 | 0.1 | Criação da estrutura do documento |  Davi  Matheus |
| 13/05/2021 | 0.2 | Adição do Topico metodologias e Processo e Referencias utilizadas | Davi Matheus |
| 14/05/2021 | 0.3 | Adição do Escopo | Davi Matheus |
| 15/05/2021 | 0.5 | Adição das tecnologias e do topico da Release 1 | Davi Matheus | 
| 16/05/2021 | 0.6 | Adição dos sentimentos antonio | Antonio Neto | 
| 17/05/2021 | 0.7 | Adição dos sentimentos: Abraao | Abraao | 
| 17/05/2021 | 0.8 | Adição dos sentimentos: Lucas | Lucas | 
| 18/05/2021 | 0.9 | Adição dos sentimentos: Natanel | Natanel | 

# Introdução

O documento tem como objetivo relatar as experiências vivências no projeto, sendo assim, um  documento é uma reflexão do time, realizada na fase de finalização do projeto, em que levantaremos tópicos que englobam acontecimentos que tiveram grandes impactos ao decorrer do projeto, para  assim, concretizar as lições aprendida.
 # Escopo do projeto

A plataforma web Cheery Up, desenvolvida para psicólogos e profissionais da saúde psicológica, será um prontuário de monitoramento da saúde mental da uma comunidade. Nessa plataforma, o psicólogo se cadastra e tem acesso à ferrramentas que irão facilitar o monitoramento da saúde mental de cada paciente que desejar cadastrar, além do usufruto de Dashboards para a observação geral da comunindade. Também há o business inteligence a partir dos dados inseridos pelos psicológos. 

Com isso dito, precisariamos ter uma comunicação fluida com os clientes, que seriam as psicologas, que nos ajudariam em adquirir metricas e parametros para o aprimorar e credibilizar nosso projeto, além de guiar nossas decisões para ter um site de facil entendimento e de rapido uso. Entrando, tivemos algumas dificuldades logo no incio do contato, em que o numero que estavamos tentando contatar era o numero errado, assim , tivemos que buscar denovo o contato com a professora, em que, novamente, estava errado.

A partir daí, nosso grupo decidiu procurar contatos com outras psicologas, em que obtivemos contatos com duas, a mãe de um dos menbros e uma amiga de outro, depois de diversas reuniões e contantos frequentes, consequimos adquirar uma boa base de como que os graficos do nosso trabalho ia ser feitos, em que nesse graficos seriam compostos de informações adquiridas no cadastro do paciente e no cadastro de uma consulta desse paciente, e que devido ao nosso pouco prazo de entrega focamos em realizar 5 graficos:

- Um grafico em pizza das regiões dos pacientes.
- Um grafico de linha da evolução do paciente.
- Um grafico de linha da qualidade de vida do paciente.
- Um gradico de linha da estabilidade emocional do paciente.
- Um grafico de DOnut da produtividade do psicologo em relação a uma consulta.

Nesse contesto , foram priorizadas funcionalidades chaves da aplicação que permitissem ao psicologo poder cadastrar um paciente,uma consulta e visualizar os graficos que surgiram a partir dessas informações.Além das necessidades básicas de uma pagina web como: cadastrar e listar objetos,deletar  e alterar suas inforamções e etc. Assim, nossa plataforma reduzida do escopo da professora, propõe, de uma forma mais simplificada,um prontuário de monitoramento da saúde mental dos seus pacientes.
# Metodologia e Processo

Noso grupo optou seguindo os conselhos da professora e dos monitores utilizar um metodo misto entre o Scrum e o XP Programming, na sua grande parte, principalmente na Realese 2, os método foram seguidos corretamente, em que, todos os grupos conseguiram captar os conceitos base dessas metodologias, e suas importancias para o desenvolvimento de um grande escopo como o nosso.

O Scrum mostrou seu poder principalmente nas áreas de produtividade e de revisão, em que a cada planning alocamos algumas issues em timebox, marcando um dia que as funcionalidades não estejam só funcionando mas estejam de boa qualidade, aumentando a nossa produtividade em geral. No fechamento da sprint, nosso grupo se reunia para todos juntos lermos a review do ScrumMaster, fazendo assim, uma retrospectiva da Sprint, analisando indicadores que o grupo como todo podia melhorar, Utilizando principalmente do grafico de Velocity tracking e do grafico de Burndown,e tambem vendo a evolução da equipe por sprint, sendo um fator de impulsamento muito grande para equipe toda a semana ver o quanto nosso conhecimento evoluia. As dailies deixaram de ser diárias devido ao decorrer complicado da semana que impedia contribuições diárias ao projeto, porém nunca deixaram de ter pelo menos 4 por semana, assim não perdendo seu valor. Um dos fatores que mais complicou o andamneto do trabalho foi a comunicação do grupo fora as reuniões,as vezes não sendo tão fluida, assim   houveram falhas em informar as tarefas incompletas.

Quanto ao Extreme Programming, utilizamos principalmente a programação pareada, em que a cada planning nós discutiamos quem iria parear com quem, para ter mais fluxo de conhecimento, contudo houveram falhas nas entregas pequenas e tambem em padronização de codigo, assim exigindo mais tempo para refatorar e alterar algumas mudanças.


- ***Pontos Postivos:*** Um dos principais pontos positivos do grupo, em relação as metodolgias, foram as Reviews do ScumMaster sendo muito bem detalhada e especifica, contendo tanto o gráfico de Velocity, o de burndown, o de riscos e os quadros de conhecimento, sendo uma review tão completa em relação a dados quanto a conselhos, em que o ScrumMaster sempre deixava comentarios construtivos para melhorarmos não só para o projeto mas como programadores em si.

- ***Pontos Negativos:*** A comunicação em geral foi algo que precisavamos melhorar muito no trabalho, principalmente na reta final com o desfoco de alguns membros devido ao aumento da carga horaria em otras materias.

# Tecnologias utilizadas
## Tecnologias utilizadas no backend
### Django, Django REST Framework e Postgres

No backend desse projeto as 3 principais tecnologias que foi utilizadas foram o Django, o app Django REST Framework e o sistema gerenciador de banco de dados relacional Postgres.

Foram decididas esses Frameworks devido a facilidade do grupo na linguegam Python, e tambem a facilidade que esses frameworks prometem, com a automatização de muitas funções que o projeto demandava, como o login, e o User padrão do Django, assim tendo uma curva de aprendizagem compatível com o tempo de desenvolvimento do projeto.
## Tecnologias utilizadas no frontend
### React.JS

React JS é uma biblioteca JavaScript para a criação de interfaces de usuário — ou UI (user interface).

O JS é uma das mais versáteis e populares linguagens de programação do mundo e conta com um grande número de bibliotecas e outras tecnologias que a utilizam. Entre elas, Node.js, Angular, VueJS, jQuery, Ember.js e, é claro, o React.

Durante as fases iniciais do projeto, até o começo da Release 2 a falta de conhecimento de React, por parte da equipe, teve um grande peso negativo em cima da velocidade des funcionalidades e entregas, diminuindo o ritmo de produção consideravelmente, e para sanar essa dificuldade aumentamos a concentração do time no front em que, 5 dos 7 integrantes estavam desenvolvendo nessa ferramenta, o que fez com que a velocidade das entregas fosse incrementada mas longe do que era a velocidade ideal que o nosso escopo demandava.

## Tecnologias utilizadas na configuração dos ambientes
### Docker e docker-compose

Docker é um software contêiner que fornece uma camada de abstração e automação para virtualização. o Docker utiliza isolamento em camadas de núcleo de sistemas operacionais e melhora o desempenho da comunicação entre a imagem virtualizada e os recursos de hardware.

Já o docker-compose funciona como um orquestrador de contêiners Docker.

Não tendo o grupo de EPS para nos ajudar com o a configuração do Docker no começo foi meio complicado mexer e programar direitinho o ambiente, porém com os treinamenrto oferecido e com algumas horas aprendemos muito e conseguimos configurara-lo paraa nosso projeto.
# Entrega da R1

A preparação da Release 1 foi muito tranquila para o nosso grupo, em que os documentos e artefatos foram feitos com qualidade e revisados com cuidado uma sprint antes da apresentação, porém a gravação do video foi algo meio caótico, em que alguns integrantes do grupo tiveram que comprar outro microfone porque o deles estava estragado, outro estava tendo problema com a internet, em meio dessas dificuldades conseguimos gravar o video e entregar faltando 10 minutos. 

Com isso dito, a  release 1  teve como objetivo principal a validação de documentos e artefatos que preparavam para o andamento do projeto e concretização do produto,foi exposta a viabilidade técnica do produto e a visão da equipe quanto a ele. Os feedback realizado pelos professores e pelos monitores , em gerais foram positivos, sendo muito bons e necessários para aumentar a moral da equipe, principalmente em um  periodo no qual foram testados diversas vezes a  capacidade de trabalho em equipe e comunicação fluída, além de uma fase de muitos aprendizados e de decisões e com isso erros.

Assim, alguns erros e pontos que precisam ser aprimorados expostos no feedback:

- Design do projeto mal trabalhado, precisando de estudo e refatoração;
- Alguns problemas na arquitetura do projeto, havendo alguns pontos que faltou detalhamento e uma explicação mais aprofundada.
- Refatoração do Canva do Projeto.

# Entrega da R2


# Sentimentos da Equipe


### Abraao 

No inicio da disciplina eu e o grupo estávamos meio perdidos em relação ao que tinha que ser feito,já que nenhum de nós não tínhamos experiencia em projetos mais profissionais e muito menos sobre as tecnologias que iriamos ultilizar em nosso projeto , porém, apesar de tudo isso
na release 1 tivemos um excelente trabalho em equipe o que nos ajudou muito na organização do projeto e também a entender melhor as metodologias de desenvolvimento de software mais adequadas para o nosso projeto.

Mas a partir da release 2 tanto eu como o Davi perdemos muito contato com a galera do frontend
que acabou deixando agente bastante preocupado em relação a conclusão do projeto. Acho que uma questão muito interessante do projeto foi manter um contato constante com o nosso cliente para saber o que deveria ser feito e realizar essa comunicação foi um tanto confusa já que não sabemos nada sobre psicologia e os psicólogos que tivemos contato não sabiam muito sobre como falar no que eles estavam pensando tanto que uma delas disse que agente tava lá tentando fazer mais com que agente entendesse o que o outro dizia do que realmente fazer e implementar o projeto. Mas no final das contas agente conseguiu entender o que se passava na mente de cada um.

E apesar de todas essas dificuldade fiquei contente com o resultado na disciplina e hoje com tantas ferramentas e tecnologias estudadas, metodologias usadas, trabalho em grupo e com uma comunicação direta com um possível cliente, entendo sua importância em um curso como esse.
### Nilvan



### Davi





### Antonio



### Natanael



### Lucas


### Arthur


# Conclusão


# Referencias: 

> [Postmortem da Acacia](https://fga-eps-mds.github.io/2019.2-Acacia/#/postmortem)

> [Postmortem da MaisMonitoria](https://fga-eps-mds.github.io/2019.1-MaisMonitoria/docs/doc-postmortem)

> [Postmortem da Gaia](https://fga-eps-mds.github.io/2019.1-Gaia/#/projeto/postMortem)


