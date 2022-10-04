<h1> CHALLENGE - ALURA CASH </h1>

## INTRODUÇÃO
Você foi contratado(a) como pessoa cientista de dados para trabalhar em um banco digital internacional chamado Alura Cash. Na primeira reunião do seu novo trabalho, a diretoria financeira informa que, recorrentemente, estão surgindo pessoas inadimplentes após a liberação de créditos. Portanto, é solicitada uma solução para que seja possível diminuir as perdas financeiras por conta de pessoas mutuarias que não quitam suas dívidas.
Como cientista de dados, você sugere um estudo das informações financeiras e de solicitação de empréstimo para encontrar padrões que possam indicar uma possível inadimplência.
Desse modo, você solicita um conjunto de dados que contenha as informações de clientes, da solicitação de empréstimo, do histórico de crédito, bem como se a pessoa mutuaria é inadimplente ou não. Com esses dados, você sabe que consegue modelar um classificador capaz de encontrar potenciais clientes inadimplentes e solucionar o problema do Alura Cash.

## ETAPA I
A partir de uma fonte 'dump' contendo as tabelas ('dados_mutuarios', 'emprestimos', 'historico_bancos', 'ids'), que podem ser encontrados na pasta RAW, foi realizado a junção das quatro tabelas utilizando o MySQL através da função ‘JOIN’, gerando uma nova tabela denominada ‘dados_aluracash.csv’, que pode ser encontrada na pasta BRONZE.

## ETAPA II
Nessa etapa foi realizado a limpeza dos dados, uma análise exploratória em que foram encontrados e removidos outliers, e uma análise de correlação entre as variáveis. A base de dados passou de 34501 para 29673 linhas e foi exportada para a pasta SILVER como ‘dados_ml.csv’.

## ETAPA III
Essa etapa consistiu no encoding das variáveis categóricas, normalização e balanceamento dos dados. Com os dados ajustados foi gerado três modelos para a predição de inadimplência (Decision Tree Classifier, Gradient Boosting Classifier e LogistRegression). Dentre os três modelos escolheu-se o Gradient Boosting Classifier que apresentou melhor desempenho. A partir desse modelo foi executado um Grid Search a fim de otimizar os hiperparâmetros e melhorar o desempenho do modelo. Os modelos foram exportados em formato ‘pickle’.

## ETAPA IV
Nessa última etapa foi feita uma API com o modelo de predição escolhido e um dashboard interativo no PowerBI.

