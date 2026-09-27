import streamlit as st

# Configuración de página optimizada para celular
st.set_page_config(
    page_title="Calculadora Profe",
    page_icon="🌸",
    layout="centered"
)

# --- INYECCIÓN DE ESTILOS CSS GENERALES (Comfortaa y Caveat) ---
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    
    /* Fuentes base globales */
    .comfortaa-bold {
        font-family: 'Comfortaa', sans-serif !important;
        font-weight: 700 !important;
    }
    .caveat-cursive {
        font-family: 'Caveat', cursive !important;
        font-size: 24px !important;
        font-weight: 600 !important;
        line-height: 1.2 !important;
    }
    
    /* Aplicar fuentes a los controles nativos de Streamlit */
    label, p, span, div.stSelectbox, div.stRadio {
        font-family: 'Comfortaa', sans-serif !important;
    }
    
    /* Estilo general para el visor de Notas Gigantes */
    .nota-display {
        font-size: 34px !important;
        font-weight: 700;
        text-align: center;
        background-color: #FFFFFF;
        border-radius: 15px;
        padding: 15px;
        margin-top: 25px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
    }
    
    /* Quitamos márgenes extra para mejor visualización en celular */
    [data-testid="stAppViewContainer"] {
        padding: 10px !important;
    }
    </style>
""", unsafe_allow_html=True)

# Título de la app en la parte superior
st.write('<h1 class="comfortaa-bold" style="color:#C89FA5; text-align:center; margin-bottom:5px; font-size: 28px;">🌸 Mis Calculadoras</h1>', unsafe_allow_html=True)

# --- SECTOR DE SELECCIÓN DE MATERIA ---
materia_elegida = st.selectbox(
    "Seleccioná la materia que vas a calificar hoy:",
    ["📢 Comunicación (4to B - CPEM 56)", "🤖 Informática (4to A - IFES)", "⚙️ Integración Tecnológica (2do A - IFES)"]
)

# =============================================================================
# ESTILOS DINÁMICOS DE FONDO COMPLETO SEGÚN LA MATERIA
# =============================================================================
if "Comunicación" in materia_elegida:
    st.markdown("""
        <style>
        [data-testid="stAppViewContainer"] { background-color: #F7E9EC !important; }
        .card-materia { background-color: #FCEFF2; border: 3px dashed #C89FA5; border-radius: 20px; padding: 20px; text-align: center; }
        .nota-display { color: #C89FA5; border: 2px solid #C89FA5; }
        </style>
    """, unsafe_allow_html=True)
    
    st.write("""
        <div class="card-materia">
            <h2 class="comfortaa-bold" style="color:#C89FA5; margin:0px; font-size:24px;">📢 CPEM 56 — 4to B</h2>
            <p class="caveat-cursive" style="color:#8A6D71; margin:5px 0px 0px 0px;">Comunicación, Discursos y Producción de Sentido</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.write('<h3 class="comfortaa-bold" style="color:#C89FA5; margin-top:20px; font-size:18px;">🎛️ Rúbrica del TP</h3>', unsafe_allow_html=True)
    sello_ia_activo = st.checkbox("🚨 APLICAR SELLO DE EXCESO DE IA (Fuerza nota al mínimo)")
    
    if sello_ia_activo:
        c1, c2, c3, c4 = 1.0, 1.0, 1.0, 1.0
        st.write('<p class="caveat-cursive" style="color:#D32F2F;">Sello estampado: Redacción detectada en nivel de Copia Total.</p>', unsafe_allow_html=True)
    else:
        c1 = st.radio("¿Lo escribió solo? (Autoría)", [3.0, 2.0, 1.0], format_func=lambda x: "3 Pts - Solo" if x==3.0 else ("2 Pts - Mitad y mitad / Estructura de IA" if x==2.0 else "1 Pt - Copia total o descarada"))
        c2 = st.radio("Pensamiento Propio (Preguntas compuestas)", [3.0, 2.0, 1.0], format_func=lambda x: "3 Pts - Incluyó posturas o ejemplos locales" if x==3.0 else ("2 Pts - Cumplió a medias" if x==2.0 else "1 Pt - Cero pensamiento, todo genérico"))
        c3 = st.radio("Lenguaje y Registro", [3.0, 1.5], format_func=lambda x: "3 Pts - Registro propio de estudiante" if x==3.0 else "1.5 Pts - Lenguaje acartonado del bot")
        c4 = st.radio("Tiempo y Forma", [3.0, 2.0, 1.0], format_func=lambda x: "3 Pts - Puntual y prolijo" if x==3.0 else ("2 Pts - Retraso leve" if x==2.0 else "1 Pt - Tarde (una semana o más)"))
        
    nota_tp = round((c1 + c2 + c3 + c4) / 4, 2)
    st.write(f'<p class="caveat-cursive" style="color:#8A6D71;">Promedio de TP: {nota_tp} / 3.0</p>', unsafe_allow_html=True)
    
    st.write('<h3 class="comfortaa-bold" style="color:#C89FA5; margin-top:20px; font-size:18px;">📊 Planilla General Cuaderno</h3>', unsafe_allow_html=True)
    eval_f = st.number_input("Evaluación Final / Parcial / Defensa (Máx. 4.0)", 0.0, 4.0, 4.0, 0.5, key="ev1")
    tareas = st.selectbox("Tareas Diarias", [1.5, 1.0, 0.0], format_func=lambda x: f"Siempre ({x} pts)" if x==1.5 else (f"A medias ({x} pt)" if x==1.0 else f"Casi nunca ({x} pts)"), key="t1")
    part = st.selectbox("Participación en Clase (Dispersos)", [1.5, 1.0, 0.0], format_func=lambda x: f"Aportó al debate / Conectado ({x} pts)" if x==1.5 else (f"Disperso / Charlaba sin molestar ({x} pt)" if x==1.0 else f"No conectó ({x} pts)"), key="p1")
    
    nota_final = min(round(eval_f + nota_tp + tareas + part, 2), 10.0)
    st.markdown(f'<div class="nota-display">Nota Cuaderno: {nota_final} / 10</div>', unsafe_allow_html=True)
elif "Informática" in materia_elegida:
    st.markdown("""
        <style>
        [data-testid="stAppViewContainer"] { background: linear-gradient(180deg, #E3F2FD 0%, #FFFDE7 100%) !important; }
        .card-materia { background-color: #FFFFFF; border: 3px solid #90CAF9; border-radius: 20px; padding: 20px; text-align: center; box-shadow: 0px 4px 8px rgba(0,0,0,0.05); }
        .nota-display { color: #1E88E5; border: 2px solid #90CAF9; }
        </style>
    """, unsafe_allow_html=True)
    
    st.write("""
        <div class="card-materia">
            <h2 class="comfortaa-bold" style="color:#1E88E5; margin:0px; font-size:24px;">🤖 IFES — 4to A</h2>
            <p class="caveat-cursive" style="color:#546E7A; margin:5px 0px 0px 0px;">Informática y Lógica Tecnológica</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.write('<h3 class="comfortaa-bold" style="color:#1E88E5; margin-top:20px; font-size:18px;">🎛️ Rúbrica del TP Técnico</h3>', unsafe_allow_html=True)
    
    c1 = st.radio("¿Lo resolvió solo? (Autoría)", [3.0, 2.0, 1.0], format_func=lambda x: "3 Pts - Solo / Uso crítico de soporte" if x==3.0 else ("2 Pts - Código o lógica con sospecha de copia" if x==2.0 else "1 Pt - Copia total de IA o compañero"))
    c2 = st.radio("Lógica Propia (Preguntas compuestas)", [3.0, 2.0, 1.0], format_func=lambda x: "3 Pts - Resolvió el problema con criterio propio" if x==3.0 else ("2 Pts - Estructura estándar / Mecánica" if x==2.0 else "1 Pt - Cero lógica, bloque genérico"))
    c3 = st.radio("Lenguaje Técnico e Interpretación", [3.0, 1.5], format_func=lambda x: "3 Pts - Interpreta comandos y usa vocabulario adecuado" if x==3.0 else "1.5 Pts - Copiado robótico sin comprender variables")
    c4 = st.radio("Tiempo y Forma", [3.0, 2.0, 1.0], format_func=lambda x: "3 Pts - Entrega puntual" if x==3.0 else ("2 Pts - Demora leve" if x==2.0 else "1 Pt - Entrega fuera de término"))
    
    nota_tp = round((c1 + c2 + c3 + c4) / 4, 2)
    st.write(f'<p class="caveat-cursive" style="color:#546E7A;">Promedio de TP Técnico: {nota_tp} / 3.0</p>', unsafe_allow_html=True)
    
    st.write('<h3 class="comfortaa-bold" style="color:#1E88E5; margin-top:20px; font-size:18px;">📊 Planilla General Cuaderno</h3>', unsafe_allow_html=True)
    eval_f = st.number_input("Evaluación Final / Parcial / Defensa (Máx. 4.0)", 0.0, 4.0, 4.0, 0.5, key="ev2")
    tareas = st.selectbox("Tareas Diarias", [1.5, 1.0, 0.0], format_func=lambda x: f"Siempre ({x} pts)" if x==1.5 else (f"A medias ({x} pt)" if x==1.0 else f"Casi nunca ({x} pts)"), key="t2")
    part = st.selectbox("Participación en Clase (Intermitentes)", [1.5, 1.0, 0.0], format_func=lambda x: f"Trabaja activo / Consulta dudas reales ({x} pts)" if x==1.5 else (f"A media máquina / Intermitente ({x} pt)" if x==1.0 else f"Desconectado de la actividad ({x} pts)"), key="p2")
    
    nota_final = min(round(eval_f + nota_tp + tareas + part, 2), 10.0)
    st.markdown(f'<div class="nota-display">Nota Cuaderno: {nota_final} / 10</div>', unsafe_allow_html=True)

else:
    st.markdown("""
        <style>
        [data-testid="stAppViewContainer"] { background-color: #FFFFFF !important; }
        .card-materia { background-color: #F8F9FA; border: 2px solid #333333; border-radius: 12px; padding: 20px; text-align: center; }
        .nota-display { color: #333333; border: 2px solid #333333; }
        </style>
    """, unsafe_allow_html=True)
    
    st.write("""
        <div class="card-materia">
            <h2 class="comfortaa-bold" style="color:#333333; margin:0px; font-size:24px;">⚙️ IFES — 2do A</h2>
            <p class="caveat-cursive" style="color:#555555; margin:5px 0px 0px 0px;">Integración Tecnológica y Práctica de Recursos</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.write('<h3 class="comfortaa-bold" style="color:#333333; margin-top:20px; font-size:18px;">🎛️ Rúbrica de Prácticos</h3>', unsafe_allow_html=True)
    
    c1 = st.radio("Apropiación del Texto e Ideas", [3.0, 2.0, 1.0], format_func=lambda x: "3 Pts - Redacción propia acorde al nivel" if x==3.0 else ("2 Pts - Intento estándar" if x==2.0 else "1 Pt - Copia evidente de IA o compañero"))
    c2 = st.radio("Uso Práctico de Herramientas", [3.0, 2.0, 1.0], format_func=lambda x: "3 Pts - Excelente desempeño práctico" if x==3.0 else ("2 Pts - Cumple con lo mínimo indispensable" if x==2.0 else "1 Pt - Mal uso o nula integración"))
    c3 = st.radio("Tiempo y Forma", [3.0, 2.0, 1.0], format_func=lambda x: "3 Pts - Puntual" if x==3.0 else ("2 Pts - Atraso de algunos días" if x==2.0 else "1 Pt - Mucha demora / Fuera de término"))
    
    nota_tp = round((c1 + c2 + c3) / 3, 2)
    st.write(f'<p class="caveat-cursive" style="color:#555555;">Promedio de TP: {nota_tp} / 3.0</p>', unsafe_allow_html=True)
    
    st.write('<h3 class="comfortaa-bold" style="color:#333333; margin-top:20px; font-size:18px;">📊 Planilla General Cuaderno</h3>', unsafe_allow_html=True)
    eval_f = st.number_input("Evaluación Final / Parcial / Defensa (Máx. 4.0)", 0.0, 4.0, 4.0, 0.5, key="ev3")
    tareas = st.selectbox("Tareas Diarias", [1.5, 1.0, 0.0], format_func=lambda x: f"Siempre ({x} pts)" if x==1.5 else (f"A medias ({x} pt)" if x==1.0 else f"Casi nunca ({x} pts)"), key="t3")
    part = st.selectbox("Participación en Clase (Desatentos)", [1.5, 1.0, 0.0], format_func=lambda x: f"Logró prestar atención y aportar ({x} pts)" if x==1.5 else (f"Pasivo / Hay que estar encima para que copie ({x} pt)" if x==1.0 else f"No prestó atención / En la suya ({x} pts)"), key="p3")
    
    nota_final = min(round(eval_f + nota_tp + tareas + part, 2), 10.0)
    st.markdown(f'<div class="nota-display">Nota Cuaderno: {nota_final} / 10</div>', unsafe_allow_html=True)
