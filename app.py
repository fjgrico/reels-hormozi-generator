import streamlit as st
from prompts.generador_guiones import generar_guion

st.set_page_config(page_title='Generador de Reels IA', page_icon='🎬', layout='centered')

st.title('🎬 Generador de Guiones estilo Hormozi con IA')
st.subheader('1. Genera tu guion brutal:')

with st.form('guion_form'):
    col1, col2 = st.columns(2)
    with col1:
        sector = st.text_input('¿A qué te dedicas?')
        producto = st.text_input('¿Qué vendes?')
        beneficios = st.text_area('Beneficios del producto/servicio')
    with col2:
        problemas = st.text_area('Problemas que soluciona')
        avatar = st.text_input('Describe tu cliente ideal')
        tematica = st.selectbox('Temática del Reel', ['Objeciones', 'Resultado', 'Historia', 'CTA'])

    tono = st.selectbox('Tono', ['Automático', 'Agresivo', 'Emocional', 'Inspirador', 'Polémico'])
    copy = st.selectbox('Fórmula', ['PAS', 'AIDA', 'FAB', 'Hormozi Style', 'Storytelling'])
    duracion = st.slider('Duración', 20, 60, 30)
    submit = st.form_submit_button('🚀 Generar Guion')

if submit:
    datos = {
        'a_que_se_dedica': sector,
        'producto_servicio': producto,
        'beneficios': beneficios,
        'problemas': problemas,
        'avatar': avatar,
        'tematica': tematica,
        'tono': tono,
        'copywriting': copy,
        'duracion': duracion
    }
    with st.spinner('Generando...'):
        resultado = generar_guion(datos)
        st.success('✅ Guion generado:')
        st.markdown(f"```{resultado}```")
        st.download_button('📥 Descargar', resultado, file_name='guion.txt')

st.divider()
st.subheader('2. Próximamente: voz y vídeo IA (activado en tu versión pro)')
