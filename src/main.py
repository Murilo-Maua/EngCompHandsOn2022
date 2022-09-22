import streamlit as st
from deepface import DeepFace

st.title("Mauá Hands On - 2022 - Engenharia da Computação 💻")

st.image("./assets/logo.jpg")

imagem = st.file_uploader("Selecione o arquivo para carregar")

if imagem != None:
    #Exibe a imagem carregada
    st.image(imagem)

    #Salva a imagem em um arquivo
    with open(f"./images/{imagem.name}", "wb") as f:
        f.write(imagem.getvalue())

    #Processa a imagem
    try:
        resultados = DeepFace.analyze(img_path = f"./images/{imagem.name}", 
            actions = ['age', 'gender', 'race', 'emotion']
        )
        st.header("Resultados:")
        st.write(resultados)
    except:
        st.write("Puxa não foi possível analizar a imagem")
