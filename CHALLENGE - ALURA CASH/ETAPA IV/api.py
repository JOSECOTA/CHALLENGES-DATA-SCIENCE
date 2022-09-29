import uvicorn
from fastapi import FastAPI
import pandas as pd


one_hot_enc = pd.read_pickle('one_hot_enc.pkl')
scaler = pd.read_pickle('scaler.pkl')
gbc = pd.read_pickle('gcb.pkl')

app = FastAPI()

@app.get('/')
def previsao(
            devendo,
            tempo_solicitacao,
            motivo_emprestimo,
            pontuacao_emprestimo,
            valor_emprestimo,
            taxa_juros,
            idade_usuario,
            salario_usuario,
            tipo_propriedade,
            anos_de_trabalho):

    dados_usuario = {
        'tipo_propriedade': [str(tipo_propriedade)],
        'motivo_emprestimo': [str(motivo_emprestimo)],
        'pontuacao_emprestimo': [str(pontuacao_emprestimo)],
        'devendo': [float(devendo)],
        'tempo_solicitacao': [float(tempo_solicitacao)],
        'valor_emprestimo': [float(valor_emprestimo)],
        'taxa_juros': [float(taxa_juros)],
        'idade_usuario': [float(idade_usuario)],
        'salario_usuario': [float(salario_usuario)],
        'anos_de_trabalho': [float(anos_de_trabalho)]
    }

    dados = pd.DataFrame(dados_usuario)

    dados = one_hot_enc.transform(dados)
    dados_transformados = pd.DataFrame(dados, columns=one_hot_enc.get_feature_names_out())

    dados_transformados = scaler.transform(dados_transformados)
    dados_transformados = pd.DataFrame(dados_transformados, columns=one_hot_enc.get_feature_names_out())

    if gbc.predict(dados_transformados).tolist()[0] == 0:
        result = "Adimplente"
    else:
        result = "Inadimplente"

    return {'Resultado': result,
            'Probabilidade de Inadimplência': round(gbc.predict_proba(dados_transformados).tolist()[0][1],4)*100,
            'tipo_propriedade': str(tipo_propriedade),
            'motivo_emprestimo': str(motivo_emprestimo),
            'pontuacao_emprestimo':str(pontuacao_emprestimo),
            'devendo': float(devendo),
            'tempo_solicitacao': float(tempo_solicitacao),
            'valor_emprestimo': float(valor_emprestimo),
            'taxa_juros': float(taxa_juros),
            'idade_usuario': float(idade_usuario),
            'salario_usuario': float(salario_usuario),
            'anos_de_trabalho': float(anos_de_trabalho)
            }


uvicorn.run(app)