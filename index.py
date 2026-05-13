import streamlit as st
import os

st.set_page_config(
    page_title="Di NO a las Drogas | CECYTEM",
    page_icon="🚫",
    layout="wide",
    initial_sidebar_state="collapsed",   
)

css_path = os.path.join(os.path.dirname(__file__), "styles.css")
if os.path.exists(css_path):
    with open(css_path, "r", encoding="utf-8") as f:
        css = f.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
else:
    st.warning("⚠️ No se encontró styles.css — ejecuta desde la carpeta del proyecto.")


DROGAS = [
    {"nombre": "🍺 Alcohol", "riesgo": "Alto",
     "desc": "Aunque es legal, el alcohol es una droga depresora. Daña el hígado, el cerebro y el sistema nervioso. Es la sustancia de mayor abuso entre jóvenes."},
    {"nombre": "🚬 Tabaco / Nicotina", "riesgo": "Alto",
     "desc": "La nicotina genera dependencia rápida. Causa enfermedades respiratorias, cardiovasculares y es el principal factor de cáncer de pulmón."},
    {"nombre": "🌿 Marihuana (Cannabis)", "riesgo": "Medio-Alto",
     "desc": "Afecta la memoria, concentración y desarrollo cerebral en jóvenes. El uso crónico aumenta el riesgo de psicosis y ansiedad."},
    {"nombre": "⚡ Cocaína", "riesgo": "Muy Alto",
     "desc": "Estimulante extremadamente adictivo. Puede provocar infartos, derrames cerebrales, psicosis y muerte incluso en la primera dosis."},
    {"nombre": "💊 Anfetaminas / Metanfetamina", "riesgo": "Muy Alto",
     "desc": "Causan deterioro cerebral severo, psicosis, pérdida de peso extrema y envejecimiento acelerado. Altamente adictivas."},
    {"nombre": "💉 Heroína / Opioides", "riesgo": "Extremo",
     "desc": "Los opioides producen la dependencia más intensa. Riesgo de sobredosis fatal en cada consumo. Devastan la vida social y familiar."},
]

SENALES_ALERTA = [
    ("🔴", "Cambios drásticos en el comportamiento o personalidad"),
    ("🔴", "Aislamiento de amigos y familia"),
    ("🟠", "Descuido del higiene personal"),
    ("🟠", "Rendimiento escolar que cae repentinamente"),
    ("🟡", "Ojos rojos, pupilas muy grandes o muy pequeñas"),
    ("🟡", "Pérdida o aumento brusco de apetito"),
    ("🔴", "Solicitar dinero frecuentemente sin explicación"),
    ("🟠", "Cambios extremos de estado de ánimo"),
    ("🟡", "Dormir demasiado o padecer insomnio"),
    ("🔴", "Encontrar parafernalia: jeringas, papel de aluminio, pipas"),
]

QUIZ_PREGUNTAS = [
    {
        "pregunta": "¿A qué edad el cerebro termina de desarrollarse por completo?",
        "opciones": ["16 años", "18 años", "25 años", "30 años"],
        "correcta": 2,
        "explicacion": "El cerebro humano no termina de madurar hasta aproximadamente los 25 años. Las drogas durante este período causan daños más graves y duraderos.",
    },
    {
        "pregunta": "¿Cuál es la droga legal más consumida entre adolescentes en México?",
        "opciones": ["Marihuana", "Alcohol", "Tabaco", "Tranquilizantes"],
        "correcta": 1,
        "explicacion": "El alcohol es la sustancia más consumida por adolescentes mexicanos, a pesar de que su venta a menores es ilegal.",
    },
    {
        "pregunta": "¿Qué significa que una droga sea 'adictiva'?",
        "opciones": [
            "Que se puede dejar de usar cuando se quiera",
            "Que el cerebro la necesita para funcionar 'normal'",
            "Que solo es dañina con dosis altas",
            "Que mejora el rendimiento",
        ],
        "correcta": 1,
        "explicacion": "La adicción es un trastorno cerebral donde el cerebro se reorganiza para 'necesitar' la sustancia, haciendo muy difícil dejarla sin ayuda.",
    },
    {
        "pregunta": "¿Cuál de estas opciones NO es una forma de decir NO a las drogas?",
        "opciones": [
            "Cambiar de tema",
            "Decir 'no, gracias' con seguridad",
            "Ceder para no parecer 'aburrido'",
            "Alejarse de la situación",
        ],
        "correcta": 2,
        "explicacion": "Ceder para encajar es exactamente lo que debemos evitar. La verdadera amistad respeta tus decisiones. Quien te presiona no es tu amigo/a.",
    },
]

PAGINAS = [
    ("🏠", "Inicio"),
    ("📊", "¿Qué son?"),
    ("⚠️", "Alertas"),
    ("💪", "Di NO"),
    ("🧠", "Quiz"),
    ("🆘", "Pedir ayuda"),
]

if "pagina" not in st.session_state:
    st.session_state.pagina = "Inicio"

st.markdown(
    """
    <div class="navbar">
        <div class="navbar-brand">
            <div class="navbar-logo">🏫</div>
            <div class="navbar-title">
                <span class="navbar-escuela">CECYTEM</span>
                <span class="navbar-subtitulo">Prevención de adicciones</span>
            </div>
        </div>
        <div class="navbar-emergency">
            📞 <strong>800 911 2000</strong>&nbsp; Línea de la Vida · 24/7
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

gap_l, *nav_cols, gap_r = st.columns([0.5] + [1] * len(PAGINAS) + [0.5])

for col, (icono, nombre) in zip(nav_cols, PAGINAS):
    with col:
        activo = st.session_state.pagina == nombre
        if st.button(
            f"{icono} {nombre}",
            key=f"nav_{nombre}",
            use_container_width=True,
            type="primary" if activo else "secondary",
        ):
            st.session_state.pagina = nombre
            st.rerun()

st.markdown("<hr style='margin:0.5rem 0 1.5rem 0; border-color:rgba(233,69,96,0.3);'>", unsafe_allow_html=True)

pagina = st.session_state.pagina

if pagina == "Inicio":
    st.markdown(
        """
        <div class="hero-section">
            <p style="font-size:3rem; margin:0;">🚫</p>
            <h1 class="hero-titulo">JUNTOS CONTRA LAS ADICCIONES</h1>
            <p class="hero-subtitulo">Información · Prevención · Esperanza</p>
            <p style="color:#a0a0b0; font-size:0.9rem; margin-top:1rem;">
                Proyecto escolar de concientización · Conoce, previene y actúa
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### 📊 La realidad en números")
    col1, col2, col3, col4 = st.columns(4)
    stats = [
        ("1 de cada 5", "jóvenes prueba alguna droga antes de los 18 años"),
        ("72%", "de los casos de adicción inician en la adolescencia"),
        ("+500,000", "personas en México buscan tratamiento cada año"),
        ("80%", "de recuperaciones exitosas con apoyo temprano"),
    ]
    for col, (num, label) in zip([col1, col2, col3, col4], stats):
        with col:
            st.markdown(
                f"""
                <div class="stat-card">
                    <div class="stat-numero">{num}</div>
                    <div class="stat-label">{label}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("<br>", unsafe_allow_html=True)
    col_a, col_b = st.columns([2, 1])
    with col_a:
        st.markdown(
            """
            <div class="seccion-card">
                <div class="seccion-titulo">¿POR QUÉ IMPORTA?</div>
                <p style="color:#eaeaea; line-height:1.8; font-size:1rem;">
                    Las adicciones no son una debilidad moral — son una enfermedad del cerebro.
                    El consumo de drogas durante la adolescencia puede alterar permanentemente
                    el desarrollo cerebral, afectar las relaciones, el rendimiento escolar y la salud física.
                </p>
                <p style="color:#a0a0b0; line-height:1.8; font-size:0.95rem;">
                    La mejor arma contra las drogas es la <strong style="color:#f5a623;">información</strong>.
                    Conocer los riesgos reales te da el poder de tomar decisiones informadas.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col_b:
        st.markdown(
            """
            <div class="esperanza-card">
                <div class="esperanza-titulo">¿SABÍAS QUE...?</div>
                <p style="color:#eaeaea; font-size:0.9rem; margin:1rem 0;">
                    El cerebro tiene una capacidad increíble de recuperarse cuando
                    se le da la oportunidad. Con apoyo, millones de personas han superado las adicciones.
                </p>
                <p style="color:#27ae60; font-weight:700;">¡Siempre hay esperanza! 💚</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

elif pagina == "¿Qué son?":
    st.markdown(
        """
        <div class="hero-section">
            <h1 class="hero-titulo">¿QUÉ SON LAS DROGAS?</h1>
            <p class="hero-subtitulo">Conoce las sustancias y sus efectos reales</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="seccion-card">
            <div class="seccion-titulo">DEFINICIÓN</div>
            <p style="color:#eaeaea; line-height:1.8;">
                Una <strong style="color:#f5a623;">droga</strong> es cualquier sustancia que al
                introducirse en el organismo altera el funcionamiento del sistema nervioso central
                y puede generar dependencia.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### 💊 Sustancias más comunes y sus riesgos")
    for droga in DROGAS:
        color_riesgo = {
            "Alto": "#f5a623", "Medio-Alto": "#e67e22",
            "Muy Alto": "#e94560", "Extremo": "#c0392b",
        }.get(droga["riesgo"], "#e94560")
        st.markdown(
            f"""
            <div class="droga-card">
                <div class="droga-nombre">
                    {droga['nombre']}
                    <span style="float:right; font-size:0.75rem; color:{color_riesgo};
                                 background:rgba(0,0,0,0.3); padding:2px 8px; border-radius:12px;">
                        Riesgo: {droga['riesgo']}
                    </span>
                </div>
                <div class="droga-desc">{droga['desc']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <div class="linea-ayuda" style="margin-top:1.5rem;">
            <p style="color:#eaeaea; margin:0;">⚠️ Recuerda: no existe una droga "segura". Todas tienen consecuencias.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

elif pagina == "Alertas":
    st.markdown(
        """
        <div class="hero-section">
            <h1 class="hero-titulo">SEÑALES DE ALERTA</h1>
            <p class="hero-subtitulo">Cómo identificar si alguien podría tener un problema</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="seccion-card"><div class="seccion-titulo">🔍 SEÑALES EN CONDUCTA</div>', unsafe_allow_html=True)
        for icono, texto in SENALES_ALERTA[:5]:
            st.markdown(f'<div class="alerta-item"><span class="alerta-icon">{icono}</span><span class="alerta-texto">{texto}</span></div>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="seccion-card"><div class="seccion-titulo">🔍 SEÑALES FÍSICAS</div>', unsafe_allow_html=True)
        for icono, texto in SENALES_ALERTA[5:]:
            st.markdown(f'<div class="alerta-item"><span class="alerta-icon">{icono}</span><span class="alerta-texto">{texto}</span></div>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="seccion-card">
            <div class="seccion-titulo">¿QUÉ HAGO SI IDENTIFICO ESTAS SEÑALES?</div>
            <p style="color:#eaeaea; line-height:1.8;">
                <strong style="color:#f5a623;">1. No juzgues.</strong> Acércate con empatía y sin críticas.<br>
                <strong style="color:#f5a623;">2. Habla en privado.</strong> Busca un momento tranquilo para conversar.<br>
                <strong style="color:#f5a623;">3. Escucha activamente.</strong> Deja que la persona se exprese.<br>
                <strong style="color:#f5a623;">4. Busca ayuda de un adulto de confianza.</strong> Maestro, familiar, orientador.<br>
                <strong style="color:#f5a623;">5. Llama a la línea de ayuda:</strong> <strong style="color:#e94560;">800 911 2000</strong>
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

elif pagina == "Di NO":
    st.markdown(
        """
        <div class="hero-section">
            <h1 class="hero-titulo">EL PODER DE DECIR NO</h1>
            <p class="hero-subtitulo">Estrategias para resistir la presión de grupo</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    estrategias = [
        ("🗣️", "SÉ DIRECTO/A", "Un simple 'No, gracias' es suficiente. No necesitas dar explicaciones. Practica decirlo con seguridad y mirando a los ojos."),
        ("🔄", "CAMBIA EL TEMA", "Si la situación se pone incómoda, desvía la conversación. 'Mejor vamos a hacer X...' puede funcionar perfectamente."),
        ("🚶", "ALÉJATE", "Si la presión continúa, retírate. Tener el valor de alejarte es una señal de madurez, no de cobardía."),
        ("👥", "BUSCA ALIADOS", "Tener amigos que compartan tus valores hace todo más fácil. Júntate con quienes te apoyen en tus decisiones."),
        ("🧠", "RECUERDA TUS METAS", "Piensa en tus sueños, tu familia, tu salud. ¿Vale la pena arriesgar todo eso?"),
        ("📱", "USA UNA EXCUSA", "'Mis papás me van a llamar', 'Tengo que madrugar'. No hay vergüenza en usarlas."),
    ]

    col1, col2 = st.columns(2)
    for i, (icono, titulo, desc) in enumerate(estrategias):
        with col1 if i % 2 == 0 else col2:
            st.markdown(
                f"""
                <div class="droga-card" style="border-left-color:#27ae60;">
                    <div class="droga-nombre" style="color:#27ae60;">{icono} {titulo}</div>
                    <div class="droga-desc">{desc}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown(
        """
        <div class="esperanza-card" style="margin-top:1.5rem;">
            <div class="esperanza-titulo">💬 FRASES QUE FUNCIONAN</div>
            <p style="color:#eaeaea; font-style:italic; line-height:2.2; margin-top:1rem;">
                "No es lo mío, gracias." &nbsp;·&nbsp; "Estoy bien así." &nbsp;·&nbsp;
                "No me late." &nbsp;·&nbsp; "Paso, gracias." &nbsp;·&nbsp;
                "Tengo que manejar." &nbsp;·&nbsp; "Estoy en tratamiento."
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

elif pagina == "Quiz":
    st.markdown(
        """
        <div class="hero-section">
            <h1 class="hero-titulo">QUIZ DE CONOCIMIENTOS</h1>
            <p class="hero-subtitulo">¿Cuánto sabes sobre las drogas y la prevención?</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if "respuestas" not in st.session_state:
        st.session_state.respuestas = {}
    if "mostrar_resultado" not in st.session_state:
        st.session_state.mostrar_resultado = False

    if not st.session_state.mostrar_resultado:
        for i, q in enumerate(QUIZ_PREGUNTAS):
            st.markdown(
                f"""
                <div class="seccion-card">
                    <div class="seccion-titulo">PREGUNTA {i+1} DE {len(QUIZ_PREGUNTAS)}</div>
                    <p style="color:#eaeaea; font-size:1.05rem; font-weight:700; margin-bottom:1rem;">{q['pregunta']}</p>
                """,
                unsafe_allow_html=True,
            )
            seleccion = st.radio(f"q{i}", q["opciones"], key=f"q_{i}", label_visibility="collapsed")
            st.session_state.respuestas[i] = q["opciones"].index(seleccion)
            st.markdown("</div>", unsafe_allow_html=True)

        if st.button("✅ Ver mis resultados", use_container_width=True):
            st.session_state.mostrar_resultado = True
            st.rerun()
    else:
        correctas = sum(1 for i, q in enumerate(QUIZ_PREGUNTAS) if st.session_state.respuestas.get(i) == q["correcta"])
        total = len(QUIZ_PREGUNTAS)
        pct = (correctas / total) * 100
        emoji_resultado = "🏆" if pct == 100 else "💪" if pct >= 75 else "📚" if pct >= 50 else "💡"

        st.markdown(
            f"""
            <div class="esperanza-card">
                <div class="esperanza-titulo">{emoji_resultado} RESULTADO FINAL</div>
                <p style="font-size:3rem; font-family:'Bebas Neue'; color:#e94560; margin:0.5rem 0;">{correctas} / {total}</p>
                <p style="color:#eaeaea;">
                    {"¡Excelente! Tienes un gran conocimiento sobre prevención." if pct == 100
                     else "¡Muy bien! Sigue aprendiendo para estar aún más preparado/a." if pct >= 75
                     else "Bien, pero te recomendamos repasar las secciones." if pct >= 50
                     else "¡No te rindas! Recorre la página para aprender más."}
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("### 📝 Revisión de respuestas")
        for i, q in enumerate(QUIZ_PREGUNTAS):
            tu_resp = st.session_state.respuestas.get(i)
            es_correcta = tu_resp == q["correcta"]
            clase = "respuesta-correcta" if es_correcta else "respuesta-incorrecta"
            icono = "✅" if es_correcta else "❌"
            st.markdown(
                f"""
                <div class="{clase}" style="margin-bottom:1rem;">
                    <strong>{icono} Pregunta {i+1}:</strong> {q['pregunta']}<br>
                    <span style="font-size:0.9rem; opacity:0.8;">
                        Tu respuesta: <em>{q['opciones'][tu_resp]}</em><br>
                        {"" if es_correcta else f"Correcta: <em>{q['opciones'][q['correcta']]}</em><br>"}
                        📖 {q['explicacion']}
                    </span>
                </div>
                """,
                unsafe_allow_html=True,
            )

        if st.button("🔄 Intentar de nuevo", use_container_width=True):
            st.session_state.mostrar_resultado = False
            st.session_state.respuestas = {}
            st.rerun()

elif pagina == "Pedir ayuda":
    st.markdown(
        """
        <div class="hero-section">
            <h1 class="hero-titulo">PEDIR AYUDA ES VALIENTE</h1>
            <p class="hero-subtitulo">Recursos de apoyo · Siempre hay una salida</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div class="linea-ayuda" style="margin-bottom:1.5rem;">
                <p style="color:#a0a0b0; font-size:0.85rem; margin:0;">LÍNEA DE LA VIDA · GRATUITA · 24/7</p>
                <div class="linea-numero">800 911 2000</div>
                <p style="color:#eaeaea; font-size:0.9rem; margin:0.5rem 0 0 0;">
                    Atención a adicciones, crisis emocionales y salud mental
                </p>
            </div>
            <div class="seccion-card">
                <div class="seccion-titulo">📍 DÓNDE BUSCAR AYUDA</div>
                <div class="droga-card" style="border-left-color:#27ae60;">
                    <div class="droga-nombre" style="color:#27ae60;">🏥 Centro de Integración Juvenil (CIJ)</div>
                    <div class="droga-desc">Atención especializada en adicciones para jóvenes. Hay centros en todo México. Visita cij.gob.mx</div>
                </div>
                <div class="droga-card" style="border-left-color:#27ae60;">
                    <div class="droga-nombre" style="color:#27ae60;">🏫 Orientación Escolar</div>
                    <div class="droga-desc">Tu escuela tiene psicólogos y orientadores. Puedes hablar con ellos de forma confidencial.</div>
                </div>
                <div class="droga-card" style="border-left-color:#27ae60;">
                    <div class="droga-nombre" style="color:#27ae60;">👨‍👩‍👧 Confianza Familiar</div>
                    <div class="droga-desc">Un familiar de confianza puede ser el primer paso. No estás solo/a.</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown('<div class="seccion-card"><div class="seccion-titulo">✉️ BUZÓN ANÓNIMO</div>', unsafe_allow_html=True)
        st.markdown("<p style='color:#a0a0b0; font-size:0.9rem;'>¿Quieres compartir algo o pedir orientación? Tu mensaje es anónimo.</p>", unsafe_allow_html=True)
        situacion = st.selectbox(
            "¿Sobre qué quieres saber más?",
            ["Selecciona una opción...", "Tengo dudas sobre el consumo de drogas",
             "Creo que un amigo/a tiene un problema", "Yo mismo/a quisiera ayuda",
             "Quiero saber cómo hablar con mis padres", "Otro tema"],
        )
        mensaje = st.text_area("Tu mensaje (opcional):", placeholder="Escribe aquí tu pregunta o situación...", height=120)
        if st.button("📨 Enviar mensaje", use_container_width=True):
            if situacion != "Selecciona una opción...":
                st.success("✅ Mensaje recibido. Un orientador revisará tu consulta. Recuerda: pedir ayuda es el paso más importante.")
            else:
                st.warning("Por favor selecciona una opción antes de enviar.")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown(
            """
            <div class="esperanza-card" style="margin-top:1rem;">
                <div class="esperanza-titulo">💚 RECUERDA</div>
                <p style="color:#eaeaea; line-height:1.8; font-size:0.95rem;">
                    Pedir ayuda <strong>no es debilidad</strong>.<br>
                    Las adicciones son una enfermedad, no una elección.<br>
                    Con apoyo profesional, <strong>la recuperación es posible</strong>.<br><br>
                    Mereces una vida plena y libre. 🌟
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown(
    """
    <div class="footer-section">
        🏫 CECYTEM · Proyecto escolar de concientización ·
        Información basada en fuentes de salud pública ·
        <strong style="color:#e94560;">Línea de la Vida: 800 911 2000</strong>
        <br><br>
        <span style="font-size:0.75rem;">
            Para personalizar esta página edita el archivo <code>styles.css</code>
        </span>
    </div>
    """,
    unsafe_allow_html=True,
)