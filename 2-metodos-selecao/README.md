<h2>Metodos de seleção dos pixels de uma imagem</h2>

O python, juntamente com a biblioteca OpenCV, permite trabalhar de forma mais simples utilizando diretamenet imagens .jpg, portanto, deste momento em diante, são extenções mais conhecidas que começarei a utilizar. Em questão, irei trabalhar com a imagem de uma estrela do mar(estrela.jpg), tentando seleciona-la e consequentemenete, separando-a do fundo.

* O arquivo "estrela-cubo.py" é responsavel por fazer a seleção utilizando um cubo dentro do RGB:
* * estrela-cubo.jpg : é a imagem resultante da estrela.jpg com seleção de cubo
* * Os valores para RGB usados na seleção foram: R<160 , G<255 e B<255. (As imagens contem 8bits, portanto, 255 é o máximo)

O mesmo ocorre para o outro arquivo, porém agora trabalhamos com uma esfera RGB no lugar de um cubo.

* O arquivo "estrela-esfera.py" é responsavel por fazer a seleção utilizando uma esfera dentro do RGB:
* * estrela-esfera.jpg : é a imagem resultante da estrela.jpg com seleção de uma esfera
* * Os valores para RGB usados na seleção são valores digitados pelo usuário, variando de 0 a 255 para RGB (limite de 8 bits) e um raio.

O arquivo "estrela-vizinho.py", trabalha na forma de <b>K-vizinhos</b>, ou seja, pega-se vários pontos distintos da imagem em que se quer selecionar, e aplica a seleção para cada uma delas, neste exemplo utilizei a seleção com esfera para cada ponto.
* * estrela-vizinho.jpg : é a imagem resultante da estrela.jpg com seleção de um número de esferas definido pelo usuário.

O método da <b>Distância de Mahalanobis</b> é o mais complexo na minha opinião. Uma explicação mais detalhada deste metodo pode ser encontrada <a href="https://pt.wikipedia.org/wiki/Dist%C3%A2ncia_de_Mahalanobis"> AQUI </a>.

* O arquivo "estrela-mahalanobis.py" é responsavel pela seleção da imagem utilizando a distância de mahalanobis.
* * estrela-mahalanobis.jpg : é a resultante do método aplicado.

-------------------------

Gustavo Gino Scotton    |   Engenharia da Computação - UFSC   |   gustavo.gino@outlook.com
