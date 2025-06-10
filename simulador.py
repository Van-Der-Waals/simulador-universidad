
import streamlit as st
import json

# Cargar preguntas desde archivo JSON
with open("preguntas_razonamiento_logico.json", "r", encoding="utf-8") as f:
    preguntas = json.load(f)

st.set_page_config(page_title="Simulador Razonamiento Lógico", layout="centered")
st.title("🧠 Simulador de Razonamiento Lógico")
st.write("**Preparación para ingreso a la universidad**")

# Iniciar variables de sesión
if "respuestas" not in st.session_state:
    st.session_state.respuestas = {}
if "mostrar_resultado" not in st.session_state:
    st.session_state.mostrar_resultado = False

# Mostrar preguntas
for i, p in enumerate(preguntas):
    st.markdown(f"### Pregunta {i + 1}")
    st.write(p["pregunta"])
    opciones = list(p["opciones"].items())
    seleccion = st.radio(
        label="Selecciona una opción:",
        options=[op[0] for op in opciones],
        format_func=lambda x: f"{x}) {p['opciones'][x]}",
        key=f"pregunta_{i}"
    )
    st.session_state.respuestas[i] = seleccion

# Botón para finalizar
if st.button("Finalizar prueba y ver resultados"):
    st.session_state.mostrar_resultado = True

# Mostrar resultados
if st.session_state.mostrar_resultado:
    st.subheader("📊 Resultados Finales")
    aciertos = 0
    for i, p in enumerate(preguntas):
        seleccion = st.session_state.respuestas.get(i)
        correcta = p["respuesta_correcta"]
        if seleccion == correcta:
            aciertos += 1
    st.success(f"Respondiste correctamente {aciertos} de {len(preguntas)} preguntas.")
    porcentaje = (aciertos / len(preguntas)) * 100
    st.write(f"**Tu puntaje:** {porcentaje:.2f}%")

    if porcentaje >= 80:
        st.balloons()
        st.markdown("🎉 ¡Excelente resultado! Estás muy bien preparado.")
    elif porcentaje >= 60:
        st.markdown("💡 Buen intento, pero puedes mejorar con más práctica.")
    else:
        st.markdown("📘 Revisa los temas de razonamiento lógico para mejorar tu desempeño.")
