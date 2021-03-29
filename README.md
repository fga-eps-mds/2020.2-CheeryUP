<p align="center"><a href="image" target="_blank"><img width="600"src="./docs/assets/images/logo.png"></a></p>   


## ℹ️ Sobre o projeto
<p align="justify"> O CheeryUP é um sistema direcionado para psicólogos que foi arquitetado por Carla Silva Rocha Aguiar, com a ideia de disponibilizar uma plataforma online para prontuário de atendimento de pacientes que estão em fase de recuperação da COVID-19.</p>
<p align="justify"> O principal intuito do projeto, é auxiliar a saúde mental dos indivíduos que se encontram em isolamento social. Outro fator, é coletar dados para definir quais ações preventivas e corretivas, podem ser realizadas em um cenário semelhante.</p> 

## Principais funcionalidades
* Registro de pacientes, consultas e sintomas.
* Monitoramento clínico dos pacientes, com quadro evolutivo dos mesmos.
* Dashboards para monitorar todo o banco de dados do sistema.


## Release 1
 >[Slides](https://docs.google.com/presentation/d/1elaS3Q-Id5pkRb8AqTLDucXgC8hOcXoflT59Aqu-xfI/edit#slide=id.gca54601322_0_0)

> [Video](https://www.youtube.com/watch?v=-i132rXQbEE)
<br>

## Tecnologias
<a href="https://habrastorage.org/webt/zt/rm/bk/ztrmbknpfaz9ybmoy3j12x5tlcw.gif"><img src="https://habrastorage.org/webt/zt/rm/bk/ztrmbknpfaz9ybmoy3j12x5tlcw.gif" width=15% height=20%></a>
<a href="https://ibb.co/sQLLDgH"><img src="https://i.ibb.co/tcyyNHX/3112.png" width=15% height= 10% alt="3112" border="0"></a>
<a href="https://ibb.co/gVGVB9s"><img src="https://i.ibb.co/sHhHMRL/django-logo-negative.png" width=20% height=8% alt="django-logo-negative" border="0"></a>
<a href="https://ibb.co/6HtXYh3"><img src="https://i.ibb.co/48S1Wy6/drive.gif" width=20% alt="drive" border="0"></a>
<a href="https://ibb.co/DYqcbFk"><img src="https://i.ibb.co/m0xZBKt/git.gif" width=20% alt="git" border="0"></a>
<a href="https://ibb.co/RB8GqM1"><img src="https://i.ibb.co/7RhxqTH/html-jss-css.jpg" width=25% alt="html-jss-css" border="0"></a>
<a href="https://ibb.co/PNTxb43"><img src="https://i.ibb.co/9Nwnf2z/postgres.png" width=15% alt="postgres" border="0"></a>
<a href="https://ibb.co/4fvxvkW"><img src="https://i.ibb.co/RSrWr82/python-powered-h-140x182.png" width=13% alt="python-powered-h-140x182" border="0"></a>
<a href="https://ibb.co/V33Pn7J"><img src="https://i.ibb.co/DLLScxz/React-native.png" width=20% alt="React-native" border="0"></a>
<a href="https://ibb.co/T0tLqjj"><img src="https://i.ibb.co/HPqdpww/wpp.gif" alt="wpp" width=20% border="0"></a>
<a href="https://ibb.co/xf44jWM"><img src="https://i.ibb.co/9VMMT6q/zenhub.png" width=18% alt="zenhub" border="0"></a>



<br>




## Como contribuir ?
Para contrubuir com o projeto você deve seguir esses padrões:
* [Guia de contruibuição](https://github.com/fga-eps-mds/2020.2-CheeryUP/blob/main/CONTRIBUTING.md)
* [Código de conduta](https://github.com/fga-eps-mds/2020.2-CheeryUP/blob/main/CODE_OF_CONDUCT.md)
* [Como rodar o Cheery ?](#como-rodar-o-cheery-?)
* [Template para ISSUES](https://github.com/fga-eps-mds/2020.2-CheeryUP/tree/main/.github/ISSUE_TEMPLATE)
* [Template para commit's](https://github.com/fga-eps-mds/2020.2-CheeryUP/blob/main/docs/templates/commit_template.md)
* [Template para pull requests](https://github.com/fga-eps-mds/2020.2-CheeryUP/blob/main/.github/pull_request_template.md)

## Como rodar o Cheery ?
1. Instalar o docker e o docker-compose
Como o projeto foi desenvolvido em containers é necessário a instalação do Docker , você pode instalar o docker [aqui](https://docs.docker.com/engine/install/), e o docker-compose [aqui](https://docs.docker.com/compose/install/)
Após a instalação conferir se o mesmo encontra em sua máquina.

     docker --v && docker-compose --v

2. Clone o projeto  

    git clone https://github.com/fga-eps-mds/2020.2-CheeryUP.git
3. Crie uma conexão local para os containers do back e front se comuniquem:

    network create network-api

4. Comandos 

* Para executar o container:

    make build  

**Após esses passos o mesmo ficará disponível em** 

    0.0.0.0:8000

* Para derrubar o container:

    make down

## Sobre o produto
* [Documentação](https://fga-eps-mds.github.io/2020.2-CheeryUP/#/)
* [Front-end](https://github.com/fga-eps-mds/2020.2-CheeryUP-FrontEnd)

<!-- ## Ambientes de homologação -->

## Integrantes
<table>
    <tr>
     <!-- Abraão   -->
        <td align="center"><a href="https://github.com/Abraao1231"><img style="border-radius: 5%;" src="https://i.ibb.co/4m7rnWB/abraao.jpg" width="100px;" alt=""/><br /><sub><b>Abraão Alves</b><br><b>Back-End</b></sub></a><br /></td>
        <!-- Antônio   -->
        <td align="center"><a href="https://github.com/antoniotoineto"><img style="border-radius: 5%;" src="https://i.ibb.co/wCJ6tks/antonio.jpg" width="100px;" alt=""/><br /><sub><b>Antônio Neto</b><br><b>Front-End</b></sub></a><br /></td>
        <!-- Arthur   -->
        <td align="center"><a href="https://github.com/art1505"><img style="border-radius: 5%;" src="https://i.ibb.co/xKbQ89h/arthur.jpg" width="100px;" alt=""/><br /><sub><b>Arthur Thalles</b><br><b>Front-End</b></sub></a><br /></td>
        <!-- Davi   -->
        <td align="center"><a href="https://github.com/DaviMatheus"><img style="border-radius: 5%;" src="https://i.ibb.co/4PbbmJs/davi.jpg" width="100px;" alt=""/><br /><sub><b>Davi Matheus</b><br><b>Product Owner</b><br><b>Back-End</b></sub></a><br /></td>
        <!-- Lucas   -->
        <td align="center"><a href="https://github.com/mibasFerraz"><img style="border-radius: 5%;" src="https://i.ibb.co/pdLPCfw/lucas.jpg" width="100px;" alt=""/><br /><sub><b>Lucas Ferraz</b><br><b>Back-End</b></sub></a><br /></td>
        <!-- Natanael   -->
        <td align="center"><a href="https://github.com/fernandes-natanael"><img style="border-radius: 5%;" src="https://i.ibb.co/sQ813nD/natanael.jpg" width="100px;" alt=""/><br /><sub><b>Natanael Filho</b><br><b>Front-End</b></sub></a><br /></td>
        <!-- Nilvan   -->
        <td align="center"><a href="https://github.com/juninhigh"><img style="border-radius: 5%;" src="https://i.ibb.co/KbmLWzW/nilvan.jpg" width="100px;" alt=""/><br /><sub><b>Nilvan Jr.</b><br><b>Scrum Master</b><br><b>Front-End</b></sub></a><br /></td>
    </tr>
</table>
