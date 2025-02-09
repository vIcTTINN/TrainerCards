import streamlit as st
import pandas as pd

# Título do aplicativo
st.title("Coleção de Cards Pokémon")

# Formulário de inserção de informações
st.header("Cadastro de Cartas Pokémon")

# Campos para inserção de dados
nome_carta = st.text_input("Nome da Carta")
estado_carta = st.selectbox("Estado da Carta", ["Nova", "Usada", "Danificada"])
foil = st.selectbox("Tipo de Carta", ["Normal", "Foil", "Reverse Foil"])
raridade = st.selectbox("Raridade", ["Comum", "Incomum", "Rara", "Ultra Rara", "Lendária"])

# Adicionar botão para salvar a carta
if st.button("Adicionar Carta"):
    # Cria um dicionário com os dados inseridos
    carta = {
        "Nome": nome_carta,
        "Estado": estado_carta,
        "Tipo": foil,
        "Raridade": raridade
    }
    
    # Exibe os dados da carta cadastrada
    st.write("Carta Adicionada!")
    st.json(carta)

# Armazenar as cartas em um DataFrame (para mais adiante)
if 'cartas' not in st.session_state:
    st.session_state.cartas = pd.DataFrame(columns=["Nome", "Estado", "Tipo", "Raridade"])

# Mostrar as cartas cadastradas
st.write("Cartas Cadastradas:")
st.write(st.session_state.cartas)