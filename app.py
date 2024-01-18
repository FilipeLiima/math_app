import streamlit as st

st.set_page_config(layout="wide")

# Criar as colunas
row1 = st.columns(1)
row2 = st.columns(3)

# Adicionar título ao contêiner
with row1[0].container():
    st.title("Math app v1")

# Adicionar conteúdo às colunas
with row2[0]:
    st.markdown("**DIMENSIONAMENTO ESTRUTURAL DE SAPATAS ISOLADAS**")
    st.image("src/a1.png")

with row2[1]:
    st.markdown("**INSERÇÃO DAS VARIÁVEIS DE ANÁLISE:**")

    bp = st.number_input('Insira a menor dimensão da seção do pilar - bp (cm)')
    ap = st.number_input('Insira a maior dimensão da seção do pilar - ap (cm)')
    carga_atuante = st.number_input('Insira a carga atuante (Kgf/cm²)')
    tensao_admissivel_solo = st.number_input('Insira a tensão admissível do solo (Kgf/cm²)')

    st.markdown("**RESUMO**")
    st.write('Menor dimensão da seção do pilar - bp:', bp)
    st.write('Maior dimensão da seção do pilar - ap:', ap)
    st.write('Carga atuante:', carga_atuante)
    st.write('Tensão admissível do solo:', tensao_admissivel_solo)

with row2[2]:
    st.markdown("**MEMORIAL DE CÁLCULO**")
    
    # Verificar se tensao_admissivel_solo é diferente de zero antes de realizar a divisão
    if tensao_admissivel_solo != 0:
        # Majorando a carga através de um coeficiente de segurança de 1,1
        majorar = carga_atuante * 1.1
        st.write('Força majorada:', majorar, 'kgf')

        area_base = majorar / tensao_admissivel_solo
        st.write('Área da base é:', area_base, 'cm²')
    else:
        st.warning("A tensão admissível do solo não pode ser zero. Insira um valor diferente.")
