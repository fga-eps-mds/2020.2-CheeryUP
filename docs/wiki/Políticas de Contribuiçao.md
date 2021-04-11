# Políticas do Repositório
## Histórico de versão

| Data | Versão | Modificação | Autor |
| :- | :- | :- | :- |
| 11/04/2021 | 1.0 | Criação da primeira versão do documento | Nilvan Peres |

## Introdução

O principal intuito desse documento é elucidar o processo e as práticas que devem ser seguidas para a **criação de branches** e de **criação de commits.**


## Políticas de Branch

Para a criação de branches, deve ser seguido as seguintes políticas abaixo.

Exemplos do gitflow das branches:

- A branch **master** concentra uma versão estável do produto, contendo código já testado e versionado, pronto para ser entregue ao usuário final ou cliente. Essa branch parte da branch **develop** através de pull requests aprovados no fim de cada release.

  Regras:

  1. Existe apenas uma branch **master**.
  2. **Não** são permitidos commits feitos diretamente na **master**.


- A branch **develop** contém a versão mais atualizada do código que está sendo desenvolvido. Essa branch está sempre sincronizada com a **master** e é base para as branches **feature**.

  Regras:

  1. Existe apenas uma branch **develop**.
  2. Essa branch está sempre sincronizada com a branch **master**.


- As branches **feature** representam as funcionalidades do sistema a serem desenvolvidas, elas devem ter a branch **develop** como sua origem e fim.

  Regras:

  1. Essa branch sempre é criada a partir da branch **develop**.
  2. Essa branch sempre é mesclada à branch **develop**.

  Regras de nomenclatura:

  `feature/titulo-da-issue`


- A branch **release** representa o conjunto de funcionalidades provenientes de um ponto específico da branch **develop**. Essa branch contém funcionalidades prontas que, provavelmente, estarão presentes na próxima versão estável do produto. Apenas **bug fixes** são permitidos nessa branch.

  Regras:

  1. Essa branch sempre é criada a partir da branch **develop**.
  2. Essa branch sempre é mesclada às branches **develop** e **master**.
  3. Essa branch aceita apenas mesclagens de branches do tipo **bugfix**.

  Regras de nomenclatura:

  `release/vNúmero-da-versão`




- As branches do tipo **bugfix** são utilizadas para implementar soluções para bugs, encontrados através de testes realizados em releases específicas, na branch **release**. Isso significa que a branch **bugfix** deve ter a branch **release** como sua origem e fim.

  Regras:

  1. Essa branch sempre é criada a partir da branch **release**.
  2. Essa branch sempre é mesclada na branch **release**.

  Regras de nomenclatura:

  `bugfix/issueID-titulo-da-issue`



  A branch **hotfix** é utilizada para implementar soluções para problemas urgentes encontrados no ambiente de produção. Isso significa que essa branch deve ter a branch **master** como sua orgigem e fim.


- Regras:

  1. Essa branch sempre é criada a partir da branch **master**.
2. Essa branch sempre é mesclada à branch **master**.

  Regras de nomenclatura:

  `hotfix/issueID-titulo-da-issue`




Observações: O título da issue utilizado no nome das branches deve ser mantido em português.


 Imagens para ajudar a visualizar o fluxo de trabalho descrito:

  ![](https://fpy.cz/pub/slides/git-workshop/images/gitflow.png)

  ![](https://miro.medium.com/max/640/0*FTwKYpFGADX-5Y0O)

## Políticas de Commits
Os commits deve seguir a seguinte estrutura: 

- categoria_nome do commit #issueID.

- Exemplo: bugs_Correções_Registro #10
- Exemplo2: add_Documento_de_Arquitetura #43

Categorias:

- _**del**_: Deletando algum arquivo/pasta e afins.
- _**format**_: Formatação no código.
- _**docs**_: Adição/atualização de algum documento.
- _**bugs**_: Correção de algum bug.
- _**feat**_: Adição/atualização de nova funcionalidade.
- _**test**_: Adição/modifição de um teste.
- _**refact**_: Refatoração do código.

É possível fechar uma issue automaticamente adicionando a palavra chave "Fix" antes do id da issue:

Fix categoria_ConciseMessage #issueID
 

# Política de migrações

As migrações criadas automaticamente pelo Django devem ser adicionadas nos commits dos desenvolvedores, exceto quando possuirem "_auto_" ou "_merge_" em seu nome.

## Referências

[Git-flow Applied to a Real Project](https://medium.com/empathyco/git-flow-applied-to-a-real-project-c08037e28f88)

[Writing git commit message](https://365git.tumblr.com/post/3308646748/writing-git-commit-messages)

[Acacia - Políticas de contribuição](https://fga-eps-mds.github.io/2019.2-Acacia/#/policies)