# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 16:18:18 2025

@author: alexa
"""

import streamlit as st

def parse_input(input_str):
    """Converte a string de entrada em uma lista de números."""
    try:
        return [float(num.strip()) for num in input_str.split(',') if num.strip()]
    except ValueError:
        return []

# Configuração da interface
st.title("Soma de Vetores")

# Campos de entrada para os vetores
A_str = st.text_input("Insira os números do vetor A, separados por vírgula:")
B_str = st.text_input("Insira os números do vetor B, separados por vírgula:")
C_str = st.text_input("Insira os números do vetor C, separados por vírgula:")

if st.button("Somar"):
    # Converter entradas para listas numéricas
    A = parse_input(A_str)
    B = parse_input(B_str)
    C = parse_input(C_str)
    
    # Somar os elementos dos vetores
    A_soma = sum(A)
    B_soma = sum(B)
    C_soma = sum(C)
    soma_total = A_soma + B_soma + C_soma
    
    # Exibir resultados
    st.write(f"A_soma: {A_soma}")
    st.write(f"B_soma: {B_soma}")
    st.write(f"C_soma: {C_soma}")
    st.write(f"Soma Total: {soma_total}")