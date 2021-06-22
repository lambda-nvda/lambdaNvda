# Complemento Lambda para NVDA (Lambda Add-On for NVDA) #

* Autor: Alberto Zanella e a equipe lambda-nvda.
* Baixe a [versão estável][1]
* Baixe a [versão em desenvolvimento][2]

Esse projeto é um appModule (módulo de aplicativo) para o Software LAMBDA. Foi inspirado no trabalho de Peter Lecky na Universidade Comenius. 
LAMBDA (Acesso Linear à Matemática para Dispositivos Braille e síntese de Áudio — Linear Access to Mathematic for Braille Device and Audio-synthesis) é um software que ajuda as pessoas cegas a ler e escrever matemática usando uma linha braille e/ou um sintetizador de fala.
LAMBDA é o resultado de um Projeto da UE (União Europeia). Para mais informações sobre o LAMBDA, visite [https://www.lambdaproject.org/](https://www.lambdaproject.org/).  
A versão atual do complemento possui tabelas braille para os idiomas
Italiano e Espanhol e sua interface está disponível na maioria dos idiomas
oficiais do NVDA, porque é traduzida pela comunidade de traduções do
NVDA. Se você é um usuário não italiano do LAMBDA e gostaria de contribuir
com o porte da tabela braille em seu idioma, entre em contato com o autor
(veja abaixo) ou inscreva-se na lista de discussão do projeto.

**Atenção:** Esse complemento foi desenvolvido por Alberto Zanella como uma atividade voluntária. Nem o autor ou os colaboradores estão envolvidos na venda e / ou desenvolvimento do software Lambda. Se você precisar de mais informações sobre o Lambda, ou precisar de suporte sobre como usá-lo, entre em contato com o seu distribuidor local. Se você encontrar alguma dificuldade ao usar ou instalar este complemento, entre em contato com o autor ou use o link "Issues" (Questões/Problemas) na página do projeto do Github.

### [Repositório Oficial no Github](https://github.com/lambda-nvda/lambdaNvda/)

## Recursos do Complemento:

### Suporte de fala:

* Diálogo e menus são informados corretamente;
* Suporte natural à fala para fórmulas matemáticas usando o mecanismo de
  matemática Lambda, ou seja, "compound root 3 sep compound root 3 x plus
  24, close compound root, minus 3 equals 0";
* implementada a leitura por caractere, palavras, linhas e Leitura Contínua;
* Fala quando um bloco de texto é selecionado ou estendido (usando CTRL+B e
  SHIFT+CTRL+B);
* Fala ao mover-se no editor de texto usando comandos padrão do Windows e
  comandos específicos do Lambda;
* Os modos de fala estendida e curta são suportados (pode selecioná-lo
  usando o menu Ferramentas no Lambda);
* Diálogos especiais como modo de estrutura, calculadora e janela de matriz
  agora são relatados corretamente e o NVDA lê corretamente ao mover o
  cursor ou quando um novo texto é digitado;
* O eco de digitação usa o processador de texto Lambda, para que símbolos e
  marcadores sejam relatados corretamente.

### Suporte a braille:

* O complemento é instalado (dentro do diretório de perfil do usuário) e
  ativa uma tabela braille personalizada. Esta tabela pode ser diferente
  para diferentes idiomas. As tabelas braille personalizadas foram feitas
  com as do plug-in Lambda para JAWS (arquivo jbt). Por conseguinte,
  símbolos e marcadores são representados usando os mesmos padrões de
  pontos;
* O complemento cria um perfil NVDA para uma configuração braille
  padrão. Por isso, a saída é configurada para a tabela braille
  personalizada somente quando o aplicativo Lambda está ativo;
* Diálogos e menus são informados corretamente em braille;
* O conteúdo do editor é renderizado corretamente em braille e o usuário
  pode se mover usando as teclas de rolagem em braille ou as teclas de
  roteamento do cursor;
* A partir da versão 1.1.0 do complemento, há duas maneiras pelas quais o
  texto no editor Lambda é renderizado: "Modo plano" e "Modo não
  Plano". Quando o "Modo plano" estiver ativado, o NVDA usará o Display
  Model (Modelo de Exibição) para recuperar informações do editor e
  determinar a posição do cursor. Isso é especialmente benéfico quando o
  usuário precisa se movimentar na tela, mesmo em espaços em branco. Quando
  o "Modo Plano" está definido como "desativado", a renderização de texto na
  tela em braille fica mais estável, pois o NVDA usa a API do Windows para
  recuperá-lo. No entanto, quando o cursor é movido em espaços em branco ao
  lado do final da linha de texto, a linha braille não segue o cursor real,
  desde que um espaço não em branco seja adicionado pelo usuário.

O "modo plano" está ativo por padrão. Você pode ativar ou desativar o "modo
plano" pressionando NVDA+SHIFT+F.

É altamente recomendável desativar o Modo Plano se você estiver usando DPI
personalizado no Windows (opção de dimensionamento personalizado),
especialmente quando tiver configurações de tela com mais de 96 dpi (maiores
que 100%).

* A estrutura das caixas de diálogo está mais fácil, informações repetidas
  foram removidas;
* A seleção será marcada corretamente usando os pontos 7 e 8, e a marcação
  será atualizada corretamente enquanto os comandos padrão do Windows
  (SHIFT+SETAS) ou comandos específicos do Lambda (CTRL+B, CTRL+SHIFT+B) são
  pressionados.

## Antes de começar a usar este complemento.

Este complemento cria um perfil NVDA chamado "lambda" associado ao
aplicativo "lambda.exe". O perfil define automaticamente todas as opções de
braille: a tabela de braille personalizada, as configurações de
compartilhamento de foco e modo plano.

Se um perfil anterior com o mesmo nome estiver presente em seu sistema, o
complemento não o substituirá e você deverá ajustar manualmente seu perfil
de configuração.

Para evitar essa situação, se você tiver configurações específicas que
gostaria de preservar, use o "Reverter o Assistente de Perfil LAMBDA". O
atalho para iniciar esta ferramenta é NVDA+alt+r (quando focalizado no
LAMBDA).

Uma opção fácil também é excluir as versões antigas do perfil "lambda" após
a instalação do complemento. Para fazer isso, abra o menu NVDA, selecione o
item do menu "Perfis de configuração" e pressione ENTER.

No diálogo Perfis de configuração, poderá localizar e excluir o perfil
"lambda". O perfil será recriado na próxima vez que o aplicativo Lambda for
iniciado.

Excluir o perfil "lambda" também deve ser uma solução fácil quando o
complemento tiver algum problema. Por exemplo, se a tabela braille não
estiver configurada corretamente, em vez de configurar manualmente o perfil,
você pode simplesmente excluí-lo. O complemento criará um novo na próxima
vez que você carregar o editor Lambda.

Cada vez que o editor Lambda é iniciado, esse complemento verifica se existe
um perfil com o nome "lambda". Caso contrário, ele gera automaticamente um
perfil com o seguinte formato:

```
filename : userData\profiles\lambda.ini :

[braille]
	readByParagraph = False
	tetherTo = focus
	translationTable = path-to-the-addon-brailleTable-dir\tableName

[lambda]
	brailleFlatMode = True

```

Onde :

* caminho-para-diretório-da-tabelaBraille-do-complemento : é o caminho
  absoluto do diretório do complemento + "\tabelaBraille"
* nomeDaTabela : depende do idioma ativo do NVDA. Atualmente, apenas as
  tabelas braille italiana e espanhola "lambda-ita.utb" e "lambda-esp.utb",
  respectivamente, estão presentes.

## Atalhos de teclado do complemento:

* **NVDA+Shift+f**: Ativa ou desativa o modo plano em braille;
* **NVDA+alt+r**: Abra o "Reverter o Assistente de Perfil LAMBDA";
* **NVDA+d: Linhas duplicadas (use isso em vez de control+d).

## Problemas conhecidos:

Devido a uma falha (bug) presente no LAMBDA, o complemento fornece uma
lógica extra que relata espaços em branco. Essa lógica pode falhar nas
seguintes situações:

* Quando palavras como "space" (espaço), "spazio" "Espacio" etc. são
  inseridas no texto, elas podem ser informadas pelo NVDA como a tradução
  local do idioma do NVDA.
* Linhas em branco não são informadas pelo mecanismo de fala LAMBDA. O
  usuário ouvirá a tradução da palavra "space" (espaço). Pode ser uma linha
  em branco ou uma linha que contém apenas a palavra "espaço".

## Dicas úteis

Este é um conjunto de dicas que ajudarão você a usar o complemento de
maneira mais eficiente.

* Informar caractere por caractere: Normalmente, ao trabalhar com
  matemática, você gostaria que o NVDA informe o que está escrevendo
  caractere por caractere. Para fazer isso, existem algumas etapas simples:
  garanta o foco na janela do LAMBDA ou em uma de suas variantes (a
  representação dos seis pontos, por exemplo); pressione NVDA+2 (número
  dois) ou navegue até o menu NVDA>Preferências>Configurações do teclado e
  marque a caixa para Falar caracteres digitados; vá para
  LAMBDA>Opções>Parâmetros de voz e verifique se a caixa de seleção "eco"
  está LIGADA; caso contrário, o NVDA não receberá nada do mecanismo de fala
  enquanto você estiver digitando. E pronto, o NVDA falará caracteres
  escritos, mas não se preocupe, apenas no LAMBDA ou em suas janelas
  especiais, as configurações para o restante dos aplicativos permanecerão
  como estavam.

## Lista de discussão do complemento:

Para relatar bugs, sugestões ou se você quiser contribuir, pode se inscrever
no Grupo do Complemento (em Inglês). Pode se inscrever no site:
<https://groups.io/g/lambda-nvda>.

## Registro de alterações (Change log)

Abaixo está uma lista de alterações entre as diferentes versões do
complemento. Ao lado do número da versão, entre parênteses, está o status de
desenvolvimento. A versão atual em desenvolvimento não está incluída, pois
pode ter alterações até ser sinalizada como estável ou descartada como
candidata.

### Versão 1.3.0 (estável)

* Suporte para a versão mais recente do NVDA (Suporte para Python 3)
* Resolvido um problema ao pressionar o comando de linha duplicada NVDA+d em
  uma linha em branco, fazia com que o conteúdo da área de transferência
  fosse colado. Agora, quando você pressiona NVDA+d e você está em uma linha
  em branco, uma nova linha em branco aparece conforme o esperado.

### Versão 1.2.2 (estável)

* Compatibilidade aprimorada com o WX Python versão 4 (introduzido no NVDA
  2018.3). O aviso relacionado ao wx.NewId() não é mais exibido no log de
  depuração.
* Implementado guiHelper para melhorar a aparência dos diálogos.
* Novos idiomas. Traduções atualizadas.

### Versão 1.2.1a (estável)

Essa atualização pretende ser uma versão de suporte de longo prazo. Isso
significa que até, pelo menos, junho de 2018, não será lançada uma versão
tão estável como esta. Fazemos isso para proporcionar aos alunos a máxima
estabilidade e minimizar as mudanças durante o ano acadêmico.

* Novos idiomas. Traduções atualizadas.

### Versão 1.2.1 (estável)

* Adicionado compatibilidade com a maneira que o NVDA 2017.3 usa para
  gerenciar braille. Compatibilidade com versões anteriores mantida.
* corrigimos muitos problemas de braille.

### Versão 1.2.0 (desenvolvimento)

Essa versão não foi publicada como estável porque a versão 1.2.1 incluiu
correções principais.

* Novos locais (idiomas). Localizações (traduções) atualizadas.

### Versão 1.1.8 (estável)

* Versão estável inicial.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=lambda

[2]: https://addons.nvda-project.org/files/get.php?file=lambda-dev
