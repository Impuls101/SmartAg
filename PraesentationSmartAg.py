import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime

import base64
from pathlib import Path

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Smarte und resiliente Landwirtschaft mit Edge AI",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM STYLING ---
st.markdown("""
<style>
    .title {
        font-size: 2.8rem;
        font-weight: 700;
        color: #1b5e20;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        font-size: 1.3rem;
        color: #424242;
        text-align: center;
        margin-bottom: 2.5rem;
    }
    .section {
        font-size: 1.8rem;
        font-weight: 600;
        color: #2e7d32;
        margin-top: 2.5rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #c8e6c9;
    }
    .section-header {
        font-size: 1.5rem;
        color: #2e7d32;
        border-left: 4px solid #66bb6a;
        padding-left: 1rem;
        margin-top: 2rem;
    }
    .highlight {
        background-color: #f5f9f5;
        padding: 1.2rem;
        border-radius: 8px;
        border-left: 4px solid #4caf50;
        margin: 1.5rem 0;
    }
    .box {
        background: white;
        padding: 1.2rem;
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        margin: 1rem 0;
    }
    .metric-row {
        display: flex;
        justify-content: space-around;
        flex-wrap: wrap;
        gap: 1rem;
        margin: 2rem 0;
    }
    .metric {
        flex: 1;
        min-width: 200px;
        text-align: center;
        padding: 1rem;
        background: #f1f8e9;
        border-radius: 8px;
        border: 1px solid #dcedc8;
    }
    .highlight-box {
        background-color: #f1f8e9;
        padding: 1.5rem;
        border-radius: 10px;
        border: 1px solid #c8e6c9;
        margin: 1rem 0;
    }
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
        transition: transform 0.2s;
    }
    .metric-card:hover {
        transform: translateY(-5px);
    }
    .pros-cons {
        display: flex;
        justify-content: space-between;
        gap: 2rem;
        margin-top: 2rem;
    }
    .pros, .cons {
        flex: 1;
        padding: 1.5rem;
        border-radius: 10px;
    }
    .pros {
        background-color: #e8f5e8;
        border: 2px solid #81c784;
    }
    .cons {
        background-color: #ffebee;
        border: 2px solid #ef9a9a;
    }
    .footer {
        text-align: center;
        margin: 0 !important;          
        padding: 0.5rem 0 !important;  
        color: #757575;
        font-size: 0.9rem;
        border-top: 1px solid #e0e0e0;
        width: 100%;
        box-sizing: border-box;        /* Verhindert Überlappungen */
    }
    .disclaimer {
        font-size: 0.85rem;
        color: #616161;
        margin: 0 !important;          /* Kein Margin */
        padding: 0 !important;
        font-style: italic;
    }
    /* Verhindert unnoetigen Leerraum beim Drucken */
    @media print {
        
        .main .block-container {
            padding-top: 0.rem !important;
            padding-bottom: 0 !important;
            margin-bottom: 0 !important;  
            max-width: 100% !important;
        }

        .stDeployButton, header, footer, #MainMenu {
            display: none !important;
        }

        .footer {
            display: block !important; 
            position: fixed; 
            bottom: 0;
            width: 100%;
            margin-top: 3rem !important; 
            margin-bottom: 0rem !important;  
            padding: 0rem 0 !important;
            page-break-inside: avoid; 
            page-break-after: avoid;  
        }
        
        .disclaimer {
            margin-bottom: 0 !important;
        }
    }

</style>
""", unsafe_allow_html=True)

# --- HEADER ---

st.markdown('<div class="title"><a href="https://smartelandwirtschaft.streamlit.app/" style="color: inherit; text-decoration: none;">🌾Smarte und resiliente Landwirtschaft mit Edge AI</a></div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Ein Projekt zur intelligenten Nahrungsmittelüberwachung durch KI-Kamerasysteme – lokal, unabhängig und zukunftsfähig.'
' </div>', unsafe_allow_html=True)

# --- PROBLEM STATEMENT ---
st.markdown('<div class="section"> Hintergrund & Motivation</div>', unsafe_allow_html=True)

# Funktion zum Laden des Bildes als Base64
def get_base64_image(image_path):
    try:
        img_bytes = Path(image_path).read_bytes()
        encoded = base64.b64encode(img_bytes).decode()
        return f"data:image/png;base64,{encoded}"
    except:
        return ""

# Bild laden
bg_image = get_base64_image("smartgreenhouse.png")
bg_image2 = get_base64_image("DryPlants.jpeg")

st.markdown(f"""
<style>
    .table-container {{
        display: flex;
        gap: 40px;
    }}
    .column {{
        flex: 1;
    }}
    ul {{
        margin: 0;
        padding-left: 20px;
    }}
    .highlight li {{
        font-size: 1.25rem;
        margin-bottom: 0.75rem;
        line-height: 1.4;
    }}
    .column-with-bg {{
        background-image: url('{bg_image}');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        position: relative;
        border-radius: 10px;
        overflow: hidden;
        padding: 1.2rem 1.2rem 0.6rem 1.2rem;
        border-radius: 8px;
        border-left: 4px solid #4caf50;
        margin: 1.5rem 0;
    }}
    .column-with-bg::before {{
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: rgba(245, 249, 245, 0.75); /* Semi-transparent overlay */
        z-index: 1;
    }}
    .column-content {{
        position: relative;
        z-index: 2;
        padding: 5px;
    }}
    .column-with-bg2 {{
        background-image: url('{bg_image2}');
        background-size: cover;
        background-position: bottom;
        background-repeat: no-repeat;
        position: relative;
        border-radius: 10px;
        overflow: hidden;
        padding: 1.2rem 1.2rem 0rem 1.2rem;;
        border-radius: 8px;
        border-left: 4px solid #4caf50;
        margin: 1.5rem 0;
    }}
    .column-with-bg2::before {{
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: rgba(245, 249, 245, 0.85); /* Semi-transparent overlay */
        z-index: 1;
    }}
</style>

<div class="table-container">
    <div class="column">
        <div class="column-with-bg2">
            <div class="column-content">
            <h4 style="text-align: center;">🧭  Ausgangszustand</h4>
            <p><strong><span style="font-size: 1.25rem;">Die Landwirtschaft steht zunehmend unter Druck – ausgelöst durch:</span></strong></p>
            <ul><span style="font-size: 1.25rem;">
              <li>Klimawandel</li>
              <li>Ressourcenknappheit (z. B. Wasser)</li>
              <li>Preisvolatilitäten und Marktschwankungen</li>
              <li>Geopolitische Spannungen</li>
              <li>Störungen in Lieferketten</li>
              <li>Stromausfälle und Energieengpässe</li>
              <li>Unterbrechungen in der Kommunikationsinfrastruktur (Internet/Mobilfunk)</li>
              <li>Zunehmende Bedrohung durch Cyberangriffe</li>
            </ul>
            <p><span style="font-size: 1.25rem;">Gleichzeitig steigt die weltweite Nachfrage nach Nahrungsmitteln – bei wachsendem Anspruch an Nachhaltigkeit und Umweltschutz.</span></p>
        </div>
        </div>
    </div>
    <div class="column">
        <div class="column-with-bg">
            <div class="column-content">
                <h4 style="text-align: center;">❔ Leitfragen</h4>
                <ul>
                <li style="font-size: 1.35rem; color: darkgreen;"><strong>Wie kann kritische Infrastruktur wie die Nahrungsmittelversorgung präziser, resilienter und effizienter überwacht werden?</strong></li>
                <li style="font-size: 1.35rem; color: darkgreen;"><strong>Wie kann man gleichzeitig konkrete Handlungsempfehlungen ableiten, die zu nachhaltigem Nutzen (ökologisch, ökonomisch, gesellschaftlich) führen?</strong></li>
                </ul>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# --- SOLUTION APPROACH ---
st.markdown('<div class="section">Ein Lösungsansatz</div>', unsafe_allow_html=True)

st.markdown("""""")

# --- TABS ---
tab1, tab2= st.tabs(["🛠️ Technologie", "⚙️ Ablauf"]) #, "🛠️ Technologie 2", "⚙️ Ablauf 2"])


# --- TAB 1: TECHNOLOGIE ---
with tab1:
    st.markdown('<div class="section-header">Lokales Netzwerk mit Edge AI & LoRaWAN/WiFi - optional mit Internetanbindung und energieautark</div>', unsafe_allow_html=True)
    
    import base64
    
    with open("TechnologieAufbauErweitert3.png", "rb") as f:
        img_data = base64.b64encode(f.read()).decode()
    
    st.markdown(f"""
        <div style="display: flex; justify-content: center; align-items: center; flex-direction: column;">
            <img src="data:image/png;base64,{img_data}" 
                 style="max-width: 1300px; width: 100%; height: auto;">
            <p style="text-align: center; color: gray; margin-top: 10px;">
                Beispielhafter technischer Aufbau
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""""")


    cols = st.columns(3)

    with cols[0]:
        st.markdown("""
        <div style="background-color:#f0f0f0; padding:10px; border-radius:5px;">
            <h4>📡 Sensorsystem</h4>
        </div>
        <div style="background-color:#EDF3DB; color:black; padding:10px; border-radius:5px; margin-top:10px; font-size: 1.25rem;">
        <ul>
            <li><b>AI-Kamera</b> mit integriertem LoRa-Transceiver  oder integriertem WiFi</li>
            <li><b>Lokale KI-Verarbeitung (Edge AI)</b> auf der Kamera mittels integrierter Tools wie TensorFlow Lite Micro oder PyTorch</li>
            <li><b>Datenübertragung</b> zu definierten Zeiten über energieeffizientes LoRaWAN (bis 10 km Reichweite) oder WiFi (hohe Bandbreite)</li>
            <li><b>Stromversorgung</b> via Batterie (LoRaWAN-basierte Kamera) oder via Netzstrom (WiFi-basierte Kamera)</li>
        </ul>
        </div>
        <div style="background-color:#B61C7B; color:white; padding:10px; border-radius:5px; margin-top:10px; font-size: 1.25rem;">
            <ul>
                <li>Optional: Solarbetrieb bei WiFi-Kameras für Energieautarkie*</li>
            </ul>   
        </div>
        <br>
        <i>* Solarbetrieb ist bei LoRaWAN-basierten Kameras nicht nötig.</i><br>
        <i>** Hierzu ist eine separate SIM-Karte nötig.</i>
        """, unsafe_allow_html=True)

    # Einsatzbereiche: Überwachung von Pflanzenwachstum, Erkennung von Schädlingen/Krankheiten, Bodenfeuchteanalyse, Reifegradbestimmung
    #<li>Zusätzliche Erprobung des Einsatzes von <b>verteiltem KI-Training (Federated Learning)</b> zur kontinuierlichen Verbesserung der Modelle möglich</li>

    with cols[1]:
        st.markdown("""
        <div style="background-color:#f0f0f0; padding:10px; border-radius:5px;">
            <h4>🖥️ Gateway & Server</h4>
        </div>
        <div style="background-color:#EDF3DB; color:black; padding:10px; border-radius:5px; margin-top:10px; font-size: 1.25rem;">
            <ul>
                <li>Ein einzelnes Gerät auf Basis des Raspberry Pi, das <b>sowohl als Gateway als auch als zentraler Server</b> dient.</li>
                <li>Gateway beinhaltet <b>LoRa-Transceiver, WLAN-Modul, LTE-Modul und SSD-Speicher</b></li>
                <li>Vorinstalliertes Linux mit Docker ermöglicht <b>einfache Konfiguration und Containerisierung</b></li>
                <li>Software: ChirpStack (Network Server für LoRaWAN), MQTT Broker (Datenvermittlung), PostgreSQL (Datenbank), Grafana (Visualisierung)</li>
                <li><b>Stromversorgung</b> via Netzstrom/Power over Ethernet (PoE)</li>
            </ul>
        </div>
        <div style="background-color:#C8E3FB; color:black; padding:10px; border-radius:5px; margin-top:10px; font-size: 1.25rem;">
            <ul>
                <li>Optional: Internetanbindung über integriertes LTE-Modul** oder über mobilen LTE-Stick**</li>
            </ul>
        </div>
        <div style="background-color:#B61C7B; color:white; padding:10px; border-radius:5px; margin-top:10px; font-size: 1.25rem;">
            <ul>
                <li>Optional: Solarbetrieb des Gateways/Servers für Energieautarkie</li>
            </ul>
        </div>

        """, unsafe_allow_html=True)

    # Vorteile dieses Setups: Einfache Installation, da ein Gerät; keine komplexe Netzwerkkommunikation zw. Gateway und Server; geringere Latenz; weniger potenzielle Netzwerkprobleme/-ausfälle

    with cols[2]:
        st.markdown("""
        <div style="background-color:#f0f0f0; padding:10px; border-radius:5px;">
            <h4>📱 Zugriff & Nutzung</h4>
        </div>
        <div style="background-color:#EDF3DB; color:black; padding:10px; border-radius:5px; margin-top:10px; font-size: 1.25rem;">
            <ul>
                <li><b>Lokales WLAN</b> vom Gateway/Server bereitgestellt</li>
                <li>Gateway/Server fungiert als <b>zentraler Zugangspunkt</b></li>
                    <ul>
                    <li>Bei Netzstrombetrieb: Permanenter Zugriff auf Gateway/Server über das <b>lokale WLAN</b> per Smartphone, Tablet oder Laptop</li>
                    <li>Bei Solarbetrieb: Aktivierung des Gateways/Servers (Sleepy Server) bei Bedarf über <b>Wake-on-WLAN</b> per Smartphone, Tablet oder Laptop</li>
                    </ul>
                <li>Bereitstellung einer <b>Datenvisualisierung (Dashboard)</b>, welche Pflanzenzustände nach Art, Ort und im Zeitverlauf anzeigt</li>
                <li><b>Benachrichtigungen</b> und Alarme möglich</li>
                <li><b>Keine Cloud- oder Internetverbindung</b> erforderlich</li>
            </ul>
        </div>
        <div style="background-color:#C8E3FB; color:black; padding:10px; border-radius:5px; margin-top:10px; font-size: 1.25rem;">
            <ul>
                <li>Optional: Fernzugriff per Smartphone, Tablet oder Laptop mittels Internet (z.B. via lokalem WLAN-Router oder LTE-Modul**)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        # <li><b>Maßnahmen</b> können direkt vor Ort abgeleitet und umgesetzt werden (z. B. Bewässerung, Warnung, Dokumentation).</li>


with tab2:
    st.markdown(
        """
        <div class="section-header">Ablaufplan</div>
        <div class="highlight-box">
            <ol style="font-size:1.5rem; line-height:2;">
                <li><b>AI-Kamera</b> beobachtet Pflanzen in definierten Zeitabständen</li>
                <li><b>TinyML-Modell</b> erkennt Fruchtanzahl und Pflanzenzustand (z. B. Reifegrad) direkt und lokal auf dem Edge-Gerät</li>
                <li><b>Datenübertragung</b> erfolgt zu definierten Zeitpunkten an das lokale Gateway-/Serversystem</li>
                <li><b>Gateway/Server</b> empfängt, speichert und visualisiert die Daten lokal</li>
                <li><b>Zugriff</b> auf die Visualisierung erfolgt per Smartphone, Tablet oder Laptop über das lokale WLAN (bzw. optional über LTE)</li>
                <li><b>Handlungsempfehlungen</b> können direkt vor Ort abgeleitet werden (z. B. Bewässern, Toppen, Ausdünnen, Auslichten, Ernten).</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""<br><br><br><br><br><br>""", unsafe_allow_html=True)


st.markdown("""<br><br>""", unsafe_allow_html=True)
# --- KEY BENEFITS/CHALLENGES ---
st.markdown('<div class="section">Abwägungen im Überblick</div>', unsafe_allow_html=True)
st.markdown("""""")

vorteile = [
    ("Wirtschaftlichkeit", "Senkung der Betriebskosten, Steigerung der Produktivität und Erträge", "💰"),
    ("Nachhaltigkeit", "Umweltschonend & verbesserter Ressourceneinsatz", "🌱"),
    ("Autarkiegrad und Resilienz", "offline-fähig & anbieterunabhängig & potenziell stromnetzunabhängig & einsetzbar in abgelegenen Regionen", "📡"),
    ("Kosteneffizienz und Energiesparsamkeit", "geringe Initialkosten & niedrige laufende Kosten & geringer Stromverbrauch der LoRaWAN-basierten Kameras", "💡"),
    ("Schnelligkeit", "zeitnahe Daten 24/7 und Entscheidungen möglich", "⏱️"),
    ("Datenhoheit", "lokale KI (Edge AI) & lokale Datenspeicherung", "🔒"),
    ("Erweiterbarkeit", "modularer Aufbau & ergänzende Sensoren (z. B. Multisensor für Bodendaten) möglich & für kleine und große Betriebe geeignet", "🧩"),
    ("Lebensmittelsicherheit", "sicherere Lebensmittel durch genaues, nachvollziehbares Monitoring", "🥗"),
    ("Nachvollziehbarkeit", "Datengetriebene, transparente Entscheidungen möglich", "📚"),
    ("Planbarkeit", "frühere und genauere Erntevorhersage sowie Einkaufbedarfs- und Umsatzprognosen", "🔮"),
    ("Reproduzierbarkeit", "verfügbare, marktzugängliche Hardware & Open Source", "🔄"),
]

herausforderungen = [
    ("Skalierung", "Flächendeckende Erfassung ist beschränkt durch die Anzahl der Kameras, ", "📏"),
    ("KI-Modellgüte und -Kalibrierung", "Bilder und ML-Modelle müssen für geringe Rechenkapazität komprimiert werden & Modellanpassungen für unterschiedl. Anwendungsfälle (z. B. Früchte, Installationsorte) nötig", "🧠"),
    #("Hardware", "Integration & Kommunikation der Komponenten (Sensorik, Gateway/Server, Zugriffsgeräte)", "🔗"),
    #("Sensorzuverlässigkeit", "Kälte-/Wetterfestigkeit sind zu klären", "❄️"),
    ("Datenqualität", "Störungen oder Ausfälle können zu Datenlücken führen", "📉"),
    ("Echtzeitfähigkeit", "Pflanzenbeobachtung nur zu definierten Zeiten, um Energieverbrauch zu minimieren", "⏳"),
    ("Wartung", "Batteriewechsel und ggfs. Updates vor Ort nötig", "🛠️"),
    ("Akzeptanz", "Einweisung für Visualisierungen erforderlich & Annahme der Technik in Arbeitsprozesse", "👨‍🌾"),
    ("Opt. Energieautarkie", "Energieverbrauch, Konfiguration von Sleepy Server, Solarmodulinstallation", "🔋"),
]

# Layout: Zwei große Spalten nebeneinander
col_vorteile, col_herausforderungen = st.columns(2)

with col_vorteile:
    st.markdown(
        '<div style="background-color:#e8f5e9; border-radius:12px; padding:0.5rem 1rem 0rem 1rem; margin-bottom:0.5rem;">'
        '<h4 style="color:#2e7d32; margin-top:0;">✅ Nutzenpotenziale</h4>',
        unsafe_allow_html=True
    )
    for label, value, icon in vorteile:
        st.markdown(
            f"""
            <div style="display:flex;align-items:center;padding:0.5rem 0;">
                <div style="font-size:1.5rem;width:2.5rem;text-align:center;">{icon}</div>
                <div>
                    <span style="font-weight:600;">{label}:</span>
                    <span style="margin-left:0.5rem;">{value}</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    st.markdown('</div>', unsafe_allow_html=True)

with col_herausforderungen:
    st.markdown(
        '<div style="background-color:#ffebee; border-radius:12px; padding:0.5rem 1rem 0rem 1rem; margin-bottom:0.5rem;">'
        '<h4 style="color:#b71c1c; margin-top:0;">⚠️ Herausforderungen</h4>',
        unsafe_allow_html=True
    )
    for label, value, icon in herausforderungen:
        st.markdown(
            f"""
            <div style="display:flex;align-items:center;padding:0.5rem 0;">
                <div style="font-size:1.5rem;width:2.5rem;text-align:center;">{icon}</div>
                <div>
                    <span style="font-weight:600;">{label}:</span>
                    <span style="margin-left:0.5rem;">{value}</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    st.markdown('</div>', unsafe_allow_html=True)


# --- ONE SCENARIO ---
st.markdown('<div class="section">Ein konkretes Anwendungsszenario</div>', unsafe_allow_html=True)

st.markdown("""                
<ul style="font-size:1.25rem;">
    <li>Ort: Gewächshaus</li>
    <li>Früchte: Tomaten, Paprika oder Gurken</li>
    <li>Hardware: 1-3 KI-Kameras & 1 Gateway/Server vor Ort</li>
</ul>
""", unsafe_allow_html=True)


# st.divider()

# # --- DIRECT BENEFITS ---
st.markdown('<div class="section">Unmittelbare Vorteile</div>', unsafe_allow_html=True)

st.markdown("""                
<ul style="font-size:1.25rem;">
    <li>1. Erprobung von KI: Was kann aktuell KI auf Edge-Geräten leisten und was nicht?</li>
    <li>2. Projekt unterstützt den Aufbau/die Verbesserung einer KI-Strategie: Wie könnte KI zukünftig im Betrieb eingesetzt werden (Robotik, Drohnen)?</li>
    <li>3. Teilhabe an KI-Forschung als Werbung für eigenen Betrieb</li>
    <li>4. Zugang zu innovativer Technologie sowie und Netzwerkaufbau zu Hochschulen</li>
</ul>
""", unsafe_allow_html=True)


# st.divider()


with open("Smarte und resiliente Landwirtschaft.pdf", "rb") as f:
    pdf_bytes = f.read()

pdf_base64 = base64.b64encode(pdf_bytes).decode('utf-8')

st.markdown(f"""
<div class="footer">
    Smarte und resiliente Landwirtschaft via Edge AI - Präsentation für potenzielle Projektpartner im Rahmen von <a href="https://innowest-brandenburg.de/">InNoWest</a> | 
    <a href="data:application/pdf;base64,{pdf_base64}" 
       download="Smarte und resiliente Landwirtschaft.pdf"
       style="text-decoration: none; color: #4CAF50; font-weight: 400;">
       als PDF herunterladen
    </a><br>
    © 2026 | Technische Hochschule Brandenburg | Kontakt: <a href="mailto: eren.misirli@th-brandenburg.de">eren.misirli@th-brandenburg.de</a>
</div>
""", unsafe_allow_html=True)
