<h1> CHALLENGE - ALURA VOZ </h1>

<b><h2> INTRODUÇÃO </h2> </b>
A Alura Voz é uma empresa de telecomunicação que nos contratou para atuar como cientistas de dados na equipe de vendas. Logo na primeira semana, a liderança nos informa que é muito necessário realizar um estudo quanto ao Churn da empresa. É explicado que o churn indica se um cliente cancelou ou não o contrato com a empresa, e também que, nos casos de perda do cliente a empresa também perde faturamento, o que ocasiona prejuizos na receita final.

Desse modo, nossa liderança informa que temos 4 semanas para buscar uma alternativa que possa minimizar a saída de clientes e nos entrega um conjunto de dados da Alura Voz que contém diversas informações sobre os clientes e também informa se eles deixaram ou não a empresa.

Sabemos que, antes de pensar em qualquer alternaiva, é preciso entender as informações que recebemos e, após uma pequena reunião, concluímos que na primeira semana nós nos dedicaríamos a entender o banco de dados, descobrir os tipos de dados, verificar a existencia de valores incoerentos e corrigi-los caso seja necessário.

<h2> ETAPA I </h2>

Nessa etapa foi realizado o tratamento da base de dados, que consistiu em separar as colunas que continham mais de uma informação, traduzir para o português e excluir os dados irrelevantes para a análise.
Após o tratamento dos dados, foi realizada uma análise exploratória das variáveis a fim de identificar possíveis padrões de taxa de evasão entre os clientes.

<h2> ETAPA II </h2>

A segunda etapa consistiu no ajuste da base de dados para possibilitar criar modelos de predição, e na construção de três diferentes modelos de machine learning (Random Forest, SVC e Logistic Regression). O modelo Random Forest apresentou maior desempenho, porém é importante ressaltar que a base de dados não possuia muitos dados, logo isso dificulta o treinamento do modelo e portanto sua eficácia.
