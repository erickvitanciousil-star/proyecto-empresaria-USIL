import streamlit as st
import os

# Configuración de la página
st.set_page_config(
    page_title="Desayunos Express - USIL",
    page_icon="🍳",
    layout="wide"
)

# Estilos visuales sencillos
st.title("🍳 Desayunos Express - USIL")
st.subheader("¡Haz tu pedido de desayunos de forma rápida y sencilla!")

st.divider()

# Lista de productos con sus imágenes y precios
productos = [
    {"nombre": "Pan con Chicharrón", "precio": 8.50, "imagen": "assets/Pan_con_chicharron.jpg"},
    {"nombre": "Pan con Camote", "precio": 5.00, "imagen": "assets/Pan_con_camote.png"},
    {"nombre": "Pan con Lomo", "precio": 9.00, "imagen": "assets/Pan_con_lomo.png"},
    {"nombre": "Pan con Palta", "precio": 4.50, "imagen": "assets/Pan_con_palta.png"},
    {"nombre": "Pan con Pollo Deshilachado", "precio": 6.00, "imagen": "assets/Pan_con_pollo_deshilachado.png"},
    {"nombre": "Pan con Tamal", "precio": 5.50, "imagen": "assets/Pan_con_tamal.png"},
    {"nombre": "Pan con Torreja", "precio": 4.00, "imagen": "assets/Pan_con_torreja.png"},
]

# Inicializar carrito en la sesión
if "carrito" not in st.session_state:
    st.session_state.carrito = []

# Disposición en columnas para los productos
col1, col2 = st.columns([2, 1])

with col1:
    st.header("Menú de Desayunos")
    
    # Crear filas de 2 productos
    for i in range(0, len(productos), 2):
        cols = st.columns(2)
        for idx, col in enumerate(cols):
            if i + idx < len(productos):
                prod = productos[i + idx]
                with col:
                    st.markdown(f"### {prod['nombre']}")
                    st.markdown(f"**Precio:** S/ {prod['precio']:.2f}")
                    
                    if os.path.exists(prod["imagen"]):
                        st.image(prod["imagen"], use_container_width=True)
                    else:
                        st.info("Imagen promocional")
                        
                    if st.button(f"Agregar {prod['nombre']}", key=f"btn_{i+idx}"):
                        st.session_state.carrito.append(prod)
                        st.toast(f"¡{prod['nombre']} agregado al pedido!", icon="✅")

with col2:
    st.header("🛒 Tu Pedido")
    
    if not st.session_state.carrito:
        st.write("El carrito está vacío.")
    else:
        total = 0
        for item in st.session_state.carrito:
            st.write(f"- {item['nombre']}: **S/ {item['precio']:.2f}**")
            total += item["precio"]
            
        st.divider()
        st.markdown(f"### Total: S/ {total:.2f}")
        
        if st.button("Vaciar Pedido", type="secondary"):
            st.session_state.carrito = []
            st.rerun()
            
        if st.button("Confirmar Pedido 🚀", type="primary"):
            st.success("¡Pedido confirmado con éxito! En breve nos pondremos en contacto.")
            st.session_state.carrito = []