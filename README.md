# cadastro_automatizado_de_produtos_com_python

Neste projeto do bootcamp, criamos uma automação de processo de cadastro de produtos de uma empresa ficticia utilizando python,
com o auxílio das bibliotecas pyautoGUI, openpyxl, mouseinfo e pyperclip
As informações dos produtos a serem cadastrados com a automação vieram da tabela "produtos" em formato excel.

O local usado para ser cadastrado o produto foi um ssistema web fornecido pelo ministro do curso.
site: https://cadastroprodutos-devaprender.netlify.app/

Lembrando que as coordenadas constantes no código foram extraidas da ferramente mouseinfo, portanto, será necessário redefinir as coordenadas
para que funcione em sua máquina.

Para executar o mouseinfo, abra o CMD e digite os seguintes comandos:

python # Para executar o python

>>> from mouseinfo import mouseInfo
# aperte enter
>>> mouseInfo()
# aperte enter

Logo após, extraia todas as coordenadas necessárias.

***Para a boa execução do seu código, garanta que toda vez que for roda-lo, as janelas estejam abertas nas mesmas coordenadas, caso contrário, redefina sempre que for rodar novamente.

