import streamlit as st
import joblib
import pandas as pd

@st.cache_resource
def load_model():
    return joblib.load(r'C:\Users\Davi Lee\Documents\ML-Obesidade\model\svc_modelo_obesidade.pkl')

@st.cache_resource
def load_scaler():
    return joblib.load(r'C:\Users\Davi Lee\Documents\ML-Obesidade\model\scaler.pkl')

if "historico" not in st.session_state:
    st.session_state.historico = []

def main():
    model = load_model()
    scaler = load_scaler()

    st.title("📝 Questionário - Previsão Obesidade")
    prev = st.selectbox("Deseja iniciar o questionário ?", ["Sim", "Não"])
    if prev == "Sim":
        with st.form(key="formulario_padrao"):
            genero = st.selectbox("Qual seu gênero ?", [(1, 'Masculino'), (0, 'Feminino')], format_func=lambda x: x[1])
            idade = st.number_input("Qual é a sua idade?", min_value=0, max_value=120, step=1)
            altura = st.number_input("Qual é a sua altura (em metros)?", min_value=0.0, max_value=2.5, step=0.01)
            peso = st.number_input("Qual é o seu peso (kg)?", min_value=0.0, max_value=300.0, step=0.1)
            historico_familiar_de_sobrepoeso = st.selectbox("Tem histórico familiar de sobrepeso ?", [(1, 'Sim'), (0, 'Não')], format_func=lambda x: x[1])
            consumo_frequente_alimentos_caloricos = st.selectbox("Tem consumo frequente de alimentos calóricos ?", [(1, 'Sim'), (0, 'Não')], format_func=lambda x: x[1])
            frequencia_consumo_vegetais = st.selectbox("Qual a frequência de consumos de vegetais ?", [(1, 'Raramente'), (2, 'As vezes'), (3, 'Todo dia')],  format_func=lambda x: x[1])
            numero_refacoes_dia =  st.number_input("Qual o número de refeições que tem no dia ?", min_value=0, max_value=120, step=1)
            consumo_alimentos_entre_refacoes = st.selectbox("Costuma comer algo nos intervalos de refeições ?", [(1, 'Sim'), (0, 'Não')], format_func=lambda x: x[1])
            ingestao_agua = st.selectbox("Qual a frequência que bebe água ?", [(1, 'Raramente'), (2, 'As vezes'), (3, 'Todo dia')],  format_func=lambda x: x[1])
            frequencia_atividade_fisica = st.selectbox("Qual a frequência que pratica atividade física ?", [(0, 'Nunca'), (1, 'Raramente'), (2, 'As vezes'), (3, 'Todo dia')],  format_func=lambda x: x[1])
            uso_tecnologia = st.selectbox("Qual a frequência que utiliza tecnologia ?", [(0, 'Nunca'), (1, 'Raramente'), (2, 'As vezes'), (3, 'Todo dia')],  format_func=lambda x: x[1])
            consumo_alcool = st.selectbox("Você consome alcool ?", [(1, 'Sim'), (0, 'Não')], format_func=lambda x: x[1])

            submit_button = st.form_submit_button(label="Fazer Predição")

            if submit_button:
                colunas = [
                    'GENERO', 'IDADE', 'ALTURA', 'PESO',
                    'HISTORICO_FAMILIAR_DE_SOBREPOESO',
                    'CONSUMO_FREQUENTE_ALIMENTOS_CALORICOS',
                    'FREQUENCIA_CONSUMO_VEGETAIS',
                    'NUMERO_REFACOES_DIA',
                    'CONSUMO_ALIMENTOS_ENTRE_REFACOES',
                    'INGESTAO_AGUA',
                    'FREQUENCIA_ATIVIDADE_FISICA',
                    'USO_TECNOLOGIA',
                    'CONSUMO_ALCOOL'
                ]

                # Dados como lista
                inputs = [
                    genero[0], idade, altura,
                    peso, historico_familiar_de_sobrepoeso[0], consumo_frequente_alimentos_caloricos[0], frequencia_consumo_vegetais[0],
                    numero_refacoes_dia, consumo_alimentos_entre_refacoes[0], ingestao_agua[0], 
                    frequencia_atividade_fisica[0], uso_tecnologia[0],
                    consumo_alcool[0]
                ]


                st.write(inputs)

                # Convertendo inputs para um array 2D
                inputs_2d = [inputs]

                # Transformar os dados
                inputs_scaled = scaler.transform(inputs_2d)

                # Fazendo a predição
                resultado = model.predict(inputs_scaled)[0]

                # Mostrando o resultado
                if resultado == 1:
                    st.write("Está com um alto risco de obesidade, procure um médico !")
                else:
                    st.write("Você está saudável ! Continue mantendo hábitos saudáveis.")


if __name__ == "__main__":
    main()
