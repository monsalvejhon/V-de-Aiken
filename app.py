import streamlit as st

st.title("Calculadora de V de Aiken")

st.write("Esta aplicación calcula la V de Aiken para dos criterios: relevancia y redacción.")

n_validadores = st.number_input("Número de validadores", min_value=1, step=1)
n_items = st.number_input("Número de ítems", min_value=1, step=1)

resultados = []

for item in range(1, int(n_items) + 1):
    st.subheader(f"Ítem {item}")

    relevancia = []
    redaccion = []

    for validador in range(1, int(n_validadores) + 1):
        col1, col2 = st.columns(2)

        with col1:
            r = st.number_input(
                f"Relevancia - Validador {validador} - Ítem {item}",
                min_value=1,
                max_value=5,
                step=1,
                key=f"rel_{item}_{validador}"
            )
            relevancia.append(r)

        with col2:
            d = st.number_input(
                f"Redacción - Validador {validador} - Ítem {item}",
                min_value=1,
                max_value=5,
                step=1,
                key=f"red_{item}_{validador}"
            )
            redaccion.append(d)

    if st.button(f"Calcular ítem {item}"):
        promedio_relevancia = sum(relevancia) / n_validadores
        promedio_redaccion = sum(redaccion) / n_validadores

        v_relevancia = (promedio_relevancia - 1) / 4
        v_redaccion = (promedio_redaccion - 1) / 4

        st.write(f"Promedio en relevancia: {promedio_relevancia:.2f}")
        st.write(f"V de Aiken en relevancia: {v_relevancia:.2f}")

        st.write(f"Promedio en redacción: {promedio_redaccion:.2f}")
        st.write(f"V de Aiken en redacción: {v_redaccion:.2f}")
