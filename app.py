import streamlit as st

st.title("Calculadora de V de Aiken")

st.write("Ingrese las valoraciones de los evaluadores en una escala de 1 a 5.")

n = st.number_input("Número de evaluadores", min_value=1, step=1)

valores = []

for i in range(int(n)):
    r = st.number_input(
        f"Valoración del evaluador {i+1}",
        min_value=1,
        max_value=5,
        step=1,
        key=f"eval_{i}"
    )
    valores.append(r)

if st.button("Calcular V de Aiken"):
    X = sum(valores) / n
    k = 4
    V = (X - 1) / k

    st.subheader("Resultado")
    st.write(f"Promedio de evaluaciones: {X:.2f}")
    st.write(f"V de Aiken: {V:.2f}")

    if V >= 0.80:
        st.success("El ítem presenta una validez de contenido alta.")
    elif V >= 0.70:
        st.warning("El ítem presenta una validez aceptable, pero conviene revisarlo.")
    else:
        st.error("El ítem presenta una validez baja y requiere ajustes.")
