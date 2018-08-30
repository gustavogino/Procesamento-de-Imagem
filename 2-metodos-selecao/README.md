<h2>Metodos de seleção dos pixels de uma imagem</h2>

O python, juntamente com a biblioteca OpenCV, permite trabalhar de forma mais simples utilizando diretamente imagens .jpg, portanto, deste momento em diante, são extenções mais conhecidas que começarei a utilizar. Em questão, irei trabalhar com a imagem de uma estrela do mar(estrela.jpg), tentando seleciona-la e consequentemenete, separando-a do fundo.

<b> O arquivo "main.py" é um menu para as funções dos outros arquivos, porém, tudo contido em um unico ".py".</b>
<i> Ou seja, é um código contendo todos os outros códigos, um simples Ctrol-C ctrol-V com acréscimo de um menu de seleção.</i>



* O arquivo "cubo.py" é responsavel por fazer a seleção utilizando um cubo dentro do RGB:
* * A imagem a ser utilizada tal como os pontos de corte RGB, podem ser digitados pelo usuário.
* * Os valores para RGB variam de 0 a 255 (se a imagem tiver 8 bits) 


O mesmo ocorre para o outro arquivo, porém agora trabalhamos com uma esfera RGB no lugar de um cubo.

* O arquivo "esfera.py" é responsavel por fazer a seleção utilizando uma esfera dentro do RGB:
* * A imagem a ser utilizada tal como os pontos de corte RGB e raio, podem ser digitados pelo usuário.
* * Os valores para RGB variam de 0 a 255  (se a imagem tiver 8 bits) 

O arquivo "vizinho.py", trabalha na forma de <b>K-vizinhos</b>, ou seja, pega-se vários pontos distintos da imagem em que se quer selecionar, e aplica a seleção para cada uma delas, neste exemplo utilizei a seleção com esfera para cada ponto.
* * A imagem a ser utilizada tal como os pontos de corte RGB e raio, podem ser digitados pelo usuário.

O método da <b>Distância de Mahalanobis</b> é o mais complexo na minha opinião. Uma explicação mais detalhada deste metodo pode ser encontrada <a href="https://pt.wikipedia.org/wiki/Dist%C3%A2ncia_de_Mahalanobis"> AQUI </a>.

* O arquivo "mahalanobis.py" é responsavel pela seleção da imagem utilizando a distância de mahalanobis.
* * A imagem a ser utilizada tal como os pontos RGB, podem ser digitados pelo usuário.
* * Os valores para RGB variam de 0 a 255 (se a imagem tiver 8 bits) 

-------------------------

Gustavo Gino Scotton    |   Engenharia da Computação - UFSC   |   gustavo.gino@outlook.com
