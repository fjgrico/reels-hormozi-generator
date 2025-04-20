import openai

openai.api_key = 'TU_API_KEY'

def generar_guion(datos_usuario):
    prompt = f"""
Eres experto en copywriting estilo Alex Hormozi.

DATOS:
- Dedicación: {datos_usuario['a_que_se_dedica']}
- Producto: {datos_usuario['producto_servicio']}
- Beneficios: {datos_usuario['beneficios']}
- Problemas: {datos_usuario['problemas']}
- Avatar: {datos_usuario['avatar']}
- Temática: {datos_usuario['tematica']}
- Fórmula: {datos_usuario['copywriting']}
- Tono: {datos_usuario['tono']}
- Duración: {datos_usuario['duracion']} seg

ENTREGA: guion directo, emocional, con CTA y frases potentes.
"""

    response = openai.chat.completions.create(
        model='gpt-4',
        messages=[
            {'role': 'system', 'content': 'Copywriter experto en guiones virales.'},
            {'role': 'user', 'content': prompt}
        ]
    )
    return response.choices[0].message.content.strip()
