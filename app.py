import streamlit as st

# Configuración de página optimizada para celular
st.set_page_config(
    page_title="Calculadora Profe",
    page_icon="🌸",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- INYECCIÓN DE ESTILOS CSS (Estética Girly, Zephyr #C89FA5 y Comfortaa) ---
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    
    /* Configuración de fuentes generales */
    html, body, [data-testid="stAppViewContainer"], .stMarkdown, p, span, label {
        font-family: 'Comfortaa', cursive !important;
    }
    
    /* Variaciones tipográficas específicas */
    .comfortaa-bold {
        font-family: 'Comfortaa', cursive !important;
        font-weight: 700 !important;
    }
    .comfortaa-cursive {
        font-family: 'Comfortaa', cursive !important;
        font-style: italic !important;
    }
    
    /* Fondo general sutilmente rosado */
    [data-testid="stAppViewContainer"] {
        background-color: #FAF4F5;
    }
    
    /* Tarjeta estilo Portada 1: Comunicación (Rosados y Zephyr) */
    .card-comunicacion {
        background-color: #FCEFF2;
        border: 3px dashed #C89FA5;
        border-radius: 20px;
        padding: 25px;
        margin-bottom: 25px;
        box-shadow: 2px 4px 10px rgba(200, 159, 165, 0.2);
    }
    
    /* Tarjeta estilo Portada 2: Informática (Líneas / Bloques Celestes y Amarillos) */
    .card-informatica {
        background: linear-gradient(135deg, #E3F2FD 25%, #FFFDE7 100%);
        border: 2px solid #C89FA5;
        border-radius: 20px;
        padding: 25px;
        margin-bottom: 25px;
        box-shadow: 2px 4px 10px rgba(0,0,0,0.05);
    }
    
    /* Tarjeta estilo Portada 3: Integración (Minimalista Blanco con detalles) */
    .card-integracion {
        background-color: #FFFFFF;
        border: 2px solid #C89FA5;
        border-radius: 12px;
        padding: 25px;
        margin-bottom: 25px;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.05);
    }
    
    /* Estilo para las métricas de notas gigantes */
    .nota-display {
        font-size: 32px !important;
        font-weight: 700;
        color: #C89FA5;
        text-align: center;
        background-color: #FFFFFF;
        border-radius: 10px;
        padding: 10px;
        border: 1px solid #C89FA5;
        margin-top: 15px;
    }
    
    /* Estilo del botón del Sello IA */
    div.stButton > button {
        background-color: #C89FA5 !important;
        color: white !important;
        font-family: 'Comfortaa', cursive !important;
        font-weight: 700 !important;
        border-radius: 15px !important;
        border: none !important;
        width: 100% !important;
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        background-color: #B3868D !important;
        transform: scale(1.02);
    }
    </style>
""", unsafe_allow_html=True)

st.write('<h1 class="comfortaa-bold" style="color:#C89FA5; text-align:center; margin-bottom:0px;">🌸 Mis Calculadoras Escolares</h1>', unsafe_allow_html=True)
st.write('<p class="comfortaa-cursive" style="text-align:center; color:#777; margin-top:0px;">Herramienta ágil de corrección en aula física</p>', unsafe_allow_html=True)

# Creación de pestañas para las materias
tab1, tab2, tab3 = st.tabs(["📢 Comunicación (4to)", "🤖 Informática (4to)", "⚙️ Integración (2do)"])

# =============================================================================
# 📢 PESTAÑA 1: COMUNICACIÓN, DISCURSOS Y PROD. DE SENTIDOS (CPEM 56 - 4to B)
# =============================================================================
with tab1:
    st.write("""
        <div class="card-comunicacion">
            <h2 class="comfortaa-bold" style="color:#C89FA5; margin-top:0px; text-align:center;">📢 CPEM 56 — 4to B</h2>
            <p class="comfortaa-cursive" style="text-align:center; color:#8A6D71; margin-bottom:0px;">Rúbrica basada en Escritura, Voz Propia y Debates</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.write('<h3 class="comfortaa-bold" style="color:#C89FA5;">🎛️ 1. Rúbrica del TP</h3>', unsafe_allow_html=True)
    
    # Checkbox rápido o criterio estrella para aplicar tu Sello directamente
    sello_ia_activo = st.checkbox("🚨 APLICAR SELLO DE EXCESO DE IA (Fuerza nota de TP al mínimo)")
    
    if sello_ia_activo:
        c1_com = 1.0; c2_com = 1.0; c3_com = 1.0; c4_com = 1.0
        st.error("⚠️ Sello activado: Los parámetros de redacción se calcularán en el nivel mínimo (Copia Total).")
    else:
        c1_com = st.radio(
            "¿Lo escribió solo? (Autoría)",
            [3.0, 2.0, 1.0],
            format_func=lambda x: f"{int(x)} Pts - Solo / Mitad y mitad / Exceso de IA" if x==3.0 else (f"{int(x)} Pts - Mitad y mitad / Estructura robótica" if x==2.0 else f"{int(x)} Pts - Copia total o descarada")
        )
        c2_com = st.radio(
            "Pensamiento Propio (Preguntas compuestas)",
            [3.0, 2.0, 1.0],
            format_func=lambda x: f"{int(x)} Pts - Sí, incluyó posturas o ejemplos reales" if x==3.0 else (f"{int(x)} Pts - Cumplió a medias" if x==2.0 else f"{int(x)} Pts - Cero pensamiento propio, todo genérico")
        )
        c3_com = st.radio(
            "Lenguaje y Registro",
            [3.0, 1.5],
            format_func=lambda x: f"{x} Pts - Registro propio y adecuado de estudiante" if x==3.0 else f"{x} Pts - Lenguaje acartonado o robótico del bot"
        )
        c4_com = st.radio(
            "Tiempo y Forma (Entrega en Comunicación)",
            [3.0, 2.0, 1.0],
            format_func=lambda x: f"{int(x)} Pts - Puntual y prolijo" if x==3.0 else (f"{int(x)} Pts - Retraso leve (un par de días)" if x==2.0 else f"{int(x)} Pts - Tarde (una semana o más)")
        )
        
    nota_tp_com = round((c1_com + c2_com + c3_com + c4_com) / 4, 2)
    st.info(f"Promedio del TP calculado: {nota_tp_com} / 3.0")
    
    st.write('<h3 class="comfortaa-bold" style="color:#C89FA5; margin-top:20px;">📊 2. Planilla General Cuaderno</h3>', unsafe_allow_html=True)
    
    eval_f_com = st.number_input("Evaluación Final / Parcial / Defensa (Máx. 4.0)", min_value=0.0, max_value=4.0, value=4.0, step=0.5, key="ev_com")
    
    tareas_com = st.selectbox(
        "Tareas Diarias (Día a día)",
        [1.5, 1.0, 0.0],
        format_func=lambda x: f"Siempre ({x} pts)" if x==1.5 else (f"A medias ({x} pt)" if x==1.0 else f"Casi nunca ({x} pts)"),
        key="tar_com"
    )
    
    part_com = st.selectbox(
        "Participación en Clase (Dinámica Dispersos)",
        [1.5, 1.0, 0.0],
        format_func=lambda x: f"Aportó al debate / Conectado ({x} pts)" if x==1.5 else (f"Disperso / Charlaba sin molestar ({x} pt)" if x==1.0 else f"No conectó en toda la clase ({x} pts)"),
        key="part_com"
    )
    
    nota_final_com = min(round(eval_f_com + nota_tp_com + tareas_com + part_com, 2), 10.0)
    st.markdown(f'<div class="nota-display">Nota Cuaderno Comunicación: {nota_final_com} / 10</div>', unsafe_allow_html=True)


# =============================================================================
# 🤖 PESTAÑA 2: INFORMÁTICA (IFES - 4to A)
# =============================================================================
with tab2:
    st.write("""
        <div class="card-informatica">
            <h2 class="comfortaa-bold" style="color:#2b5c8f; margin-top:0px; text-align:center;">🤖 IFES — 4to A</h2>
            <p class="comfortaa-cursive" style="text-align:center; color:#5c6b73; margin-bottom:0px;">Rúbrica Técnica: Lógica, Estructura y Código</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.write('<h3 class="comfortaa-bold" style="color:#2b5c8f;">🎛️ 1. Rúbrica del TP Técnico</h3>', unsafe_allow_html=True)
    
    c1_inf = st.radio(
        "Resolución Lógica y Estructura",
        [3.0, 2.0, 1.0],
        format_func=lambda x: f"{int(x)} Pts - Funciona correctamente y resuelve el problema técnico" if x==3.0 else (f"{int(x)} Pts - Funciona de forma desordenada o mecánica" if x==2.0 else f"{int(x)} Pts - No funciona o estructura rota")
    )
    c2_inf = st.radio(
        "Uso Crítico de la IA en Informática",
        [3.0, 1.0],
        format_func=lambda x: f"{int(x)} Pts - Utilizada como guía de soporte para corregir o comprender" if x==3.0 else f"{int(x)} Pts - Copiar y pegar ciego sin entender la lógica interna"
    )
    c3_inf = st.radio(
        "Tiempo y Forma (Entrega Informática)",
        [3.0, 2.0, 1.0],
        format_func=lambda x: f"{int(x)} Pts - Entrega puntual" if x==3.0 else (f"{int(x)} Pts - Demora leve" if x==2.0 else f"{int(x)} Pts - Entrega fuera de término")
    )
    
    nota_tp_inf = round((c1_inf + c2_inf + c3_inf) / 3, 2)
    st.info(f"Promedio del TP Técnico calculado: {nota_tp_inf} / 3.0")
    
    st.write('<h3 class="comfortaa-bold" style="color:#2b5c8f; margin-top:20px;">📊 2. Planilla General Cuaderno</h3>', unsafe_allow_html=True)
    
    eval_f_inf = st.number_input("Evaluación Final / Parcial / Defensa (Máx. 4.0)", min_value=0.0, max_value=4.0, value=4.0, step=0.5, key="ev_inf")
    
    tareas_inf = st.selectbox(
        "Tareas Diarias (Día a día)",
        [1.5, 1.0, 0.0],
        format_func=lambda x: f"Siempre ({x} pts)" if x==1.5 else (f"A medias ({x} pt)" if x==1.0 else f"Casi nunca ({x} pts)"),
        key="tar_inf"
    )
    
    part_inf = st.selectbox(
        "Participación en Clase (Dinámica Intermitente)",
        [1.5, 1.0, 0.0],
        format_func=lambda x: f"Trabaja activo / Consulta dudas reales ({x} pts)" if x==1.5 else (f"A media máquina / Intermitente ({x} pt)" if x==1.0 else f"Desconectado de la actividad práctica ({x} pts)"),
        key="part_inf"
    )
    
    nota_final_inf = min(round(eval_f_inf + nota_tp_inf + tareas_inf + part_inf, 2), 10.0)
    st.markdown(f'<div class="nota-display" style="color:#2b5c8f; border-color:#2b5c8f;">Nota Cuaderno Informática: {nota_final_inf} / 10</div>', unsafe_allow_html=True)
# =============================================================================
# ⚙️ PESTAÑA 3: INTEGRACIÓN TECNOLÓGICA (IFES - 2do A)
# =============================================================================
with tab3:
    st.write("""
        <div class="card-integracion">
            <h2 class="comfortaa-bold" style="color:#333333; margin-top:0px; text-align:center;">⚙️ IFES — 2do A</h2>
            <p class="comfortaa-cursive" style="text-align:center; color:#666666; margin-bottom:0px;">Uso de Herramientas Prácticas y Control de Atención</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.write('<h3 class="comfortaa-bold" style="color:#333333;">🎛️ 1. Rúbrica de Prácticos</h3>', unsafe_allow_html=True)
    
    c1_int = st.radio(
        "Apropiación del Texto e Ideas",
        [3.0, 2.0, 1.0],
        format_func=lambda x: f"{int(x)} Pts - Redacción propia acorde al nivel" if x==3.0 else (f"{int(x)} Pts - Intento estándar" if x==2.0 else f"{int(x)} Pts - Copia evidente de IA o compañero")
    )
    c2_int = st.radio(
        "Uso Práctico de Herramientas",
        [3.0, 2.0, 1.0],
        format_func=lambda x: f"{int(x)} Pts - Excelente desempeño práctico con el recurso" if x==3.0 else (f"{int(x)} Pts - Cumple con lo mínimo indispensable" if x==2.0 else f"{int(x)} Pts - Mal uso o nula integración técnica")
    )
    c3_int = st.radio(
        "Tiempo y Forma (Entrega Integración)",
        [3.0, 2.0, 1.0],
        format_func=lambda x: f"{int(x)} Pts - Puntual" if x==3.0 else (f"{int(x)} Pts - Retraso de días" if x==2.0 else f"{int(x)} Pts - Mucha demora")
    )
    
    nota_tp_int = round((c1_int + c2_int + c3_int) / 3, 2)
    st.info(f"Promedio del TP calculado: {nota_tp_int} / 3.0")
    
    st.write('<h3 class="comfortaa-bold" style="color:#333333; margin-top:20px;">📊 2. Planilla General Cuaderno</h3>', unsafe_allow_html=True)
    
    eval_f_int = st.number_input("Evaluación Final / Parcial / Defensa (Máx. 4.0)", min_value=0.0, max_value=4.0, value=4.0, step=0.5, key="ev_int")
    
    tareas_int = st.selectbox(
        "Tareas Diarias (Día a día)",
        [1.5, 1.0, 0.0],
        format_func=lambda x: f"Siempre ({x} pts)" if x==1.5 else (f"A medias ({x} pt)" if x==1.0 else f"Casi nunca ({x} pts)"),
        key="tar_int"
    )
    
    part_int = st.selectbox(
        "Participación en Clase (Dinámica Desatentos)",
        [1.5, 1.0, 0.0],
        format_func=lambda x: f"Logró prestar atención y aportar activamente ({x} pts)" if x==1.5 else (f"Pasivo / Hay que estarle encima para que copie ({x} pt)" if x==1.0 else f"No prestó atención nunca / Totalmente en la suya ({x} pts)"),
        key="part_int"
    )
    
    nota_final_int = min(round(eval_f_int + nota_tp_int + tareas_int + part_int, 2), 10.0)
    st.markdown(f'<div class="nota-display" style="color:#333333; border-color:#333333;">Nota Cuaderno Integración: {nota_final_int} / 10</div>', unsafe_allow_html=True)
