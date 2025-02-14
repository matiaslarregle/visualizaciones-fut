

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from mplsoccer import Radar, grid
from matplotlib.font_manager import FontProperties
from mplsoccer import Radar, FontManager, grid
import matplotlib.pyplot as plt

URL1 = ('https://raw.githubusercontent.com/googlefonts/SourceSerifProGFVersion/main/fonts/'
        'SourceSerifPro-Regular.ttf')
serif_regular = FontManager(URL1)
URL2 = ('https://raw.githubusercontent.com/googlefonts/SourceSerifProGFVersion/main/fonts/'
        'SourceSerifPro-ExtraLight.ttf')
serif_extra_light = FontManager(URL2)
URL3 = ('https://raw.githubusercontent.com/google/fonts/main/ofl/rubikmonoone/'
        'RubikMonoOne-Regular.ttf')
rubik_regular = FontManager(URL3)
URL4 = 'https://raw.githubusercontent.com/googlefonts/roboto/main/src/hinted/Roboto-Thin.ttf'
robotto_thin = FontManager(URL4)
URL5 = ('https://raw.githubusercontent.com/google/fonts/main/apache/robotoslab/'
        'RobotoSlab%5Bwght%5D.ttf')
robotto_bold = FontManager(URL5)

# Cargar datos
df_copa_2024 = pd.read_csv('Argentina Copa de la Liga 2024.csv')
df_lpf_2024 = pd.read_csv('Argentina LPF 2024.csv')
df_reserva_2024 = pd.read_csv('Argentina Reserve League 2024.csv')

# Agregar el nombre de la liga al final de cada jugador
df_copa_2024["Player"] = df_copa_2024["Player"] + " (Copa de la Liga)"
df_lpf_2024["Player"] = df_lpf_2024["Player"] + " (LPF)"
df_reserva_2024["Player"] = df_reserva_2024["Player"] + " (Reserva)"

df = pd.concat([df_copa_2024, df_lpf_2024, df_reserva_2024])
df = df.fillna(0)

# Diccionario de mapeo
position_mapping = {
    'CF': 'Delanteros',
    'RB': 'Laterales',
    'RW': 'Extremos',
    'RWF': 'Extremos',
    'LW': 'Extremos',
    'LWF': 'Extremos',
    'LB': 'Laterales',
    'LCB': 'Centrales',
    'RCB': 'Centrales',
    'CB': 'Centrales',
    'LCMF': 'Interiores/mixtos',
    'RCMF': 'Interiores/mixtos',
    'RCMF3': 'Interiores/mixtos',
    'LCMF3': 'Interiores/mixtos',
    'AMF': 'Mediocampistas ofensivos',
    'LAMF': 'Mediocampistas ofensivos',
    'RAMF': 'Mediocampistas ofensivos',
    'DMF': 'Mediocampistas defensivos',
    'LDMF': 'Mediocampistas defensivos',
    'RDMF': 'Mediocampistas defensivos',
    'RWB': 'Laterales',
    'LWB': 'Laterales',
    'GK': 'Arqueros',
    'RB5': 'Laterales',
    'LB5': 'Laterales',
    'LCB3': 'Centrales',
    'RCB3': 'Centrales'
}

# Reemplazar los valores en las columnas correspondientes
df['Primary position'] = df['Primary position'].replace(position_mapping)
df['Secondary position'] = df['Secondary position'].replace(position_mapping)
df['Third position'] = df['Third position'].replace(position_mapping)

# Calcular las frecuencias de cada columna por separado
primary_position_counts = df['Primary position'].value_counts()
secondary_position_counts = df['Secondary position'].value_counts()
third_position_counts = df['Third position'].value_counts()

estadisticas = [
    "Goals",
    "xG",
    "Assists",
    "xA",
    "Duels per 90",
    "Duels won, %",
    "Successful defensive actions per 90",
    "Defensive duels per 90",
    "Defensive duels won, %",
    "Aerial duels per 90",
    "Aerial duels won, %",
    "Sliding tackles per 90",
    "PAdj Sliding tackles",
    "Shots blocked per 90",
    "Interceptions per 90",
    "PAdj Interceptions",
    "Successful attacking actions per 90",
    "Goals per 90",
    "Non-penalty goals",
    "Non-penalty goals per 90",
    "xG per 90",
    "Head goals",
    "Head goals per 90",
    "Shots",
    "Shots per 90",
    "Goal conversion, %",
    "Assists per 90",
    "Crosses per 90",
    "Accurate crosses, %",
    "Crosses to goalie box per 90",
    "Dribbles per 90",
    "Successful dribbles, %",
    "Offensive duels per 90",
    "Offensive duels won, %",
    "Progressive runs per 90",
    "Accelerations per 90",
    "Fouls suffered per 90",
    "Passes per 90",
    "Accurate passes, %",
    "Forward passes per 90",
    "Accurate forward passes, %",
    "Long passes per 90",
    "Accurate long passes, %",
    "xA per 90",
    "Shot assists per 90",
    "Second assists per 90",
    "Smart passes per 90",
    "Accurate smart passes, %",
    "Key passes per 90",
    "Passes to final third per 90",
    "Accurate passes to final third, %",
    "Passes to penalty area per 90",
    "Accurate passes to penalty area, %",
    "Through passes per 90",
    "Accurate through passes, %",
    "Deep completions per 90",
    "Deep completed crosses per 90",
    "Progressive passes per 90",
    "Accurate progressive passes, %",
    "Clean sheets",
    "Save rate, %",
    "Prevented goals",
    "Prevented goals per 90",
    "Exits per 90",
]

estadisticas_traducidas = [
    "Goles",
    "xG (Goles esperados)",
    "Asistencias",
    "xA (Asistencias esperadas)",
    "Duelos por 90",
    "% de duelos ganados",
    "Acciones defensivas exitosas por 90",
    "Duelos defensivos por 90",
    "% de duelos defensivos ganados",
    "Duelos aéreos por 90",
    "% de duelos aéreos ganados",
    "Barridas por 90",
    "Barridas ajustadas por posesión",
    "Tiros bloqueados por 90",
    "Intercepciones por 90",
    "Intercepciones ajustadas por posesión",
    "Acciones ofensivas exitosas por 90",
    "Goles por 90",
    "Goles sin penales",
    "Goles sin penales por 90",
    "xG por 90",
    "Goles de cabeza",
    "Goles de cabeza por 90",
    "Tiros",
    "Tiros por 90",
    "% de conversión de goles",
    "Asistencias por 90",
    "Centros por 90",
    "% de centros precisos",
    "Centros al área chica por 90",
    "Regates por 90",
    "% de regates exitosos",
    "Duelos ofensivos por 90",
    "% de duelos ofensivos ganados",
    "Carreras progresivas por 90",
    "Aceleraciones por 90",
    "Faltas recibidas por 90",
    "Pases por 90",
    "% de Pases precisos",
    "Pases hacia adelante por 90",
    "% de pases hacia adelante precisos",
    "Pases largos por 90",
    "% de pases largos precisos",
    "xA por 90",
    "Asistencias de tiro por 90",
    "Segundas asistencias por 90",
    "Pases inteligentes por 90",
    "% de pases inteligentes precisos",
    "Pases clave por 90",
    "Pases al tercio final por 90",
    "% de pases precisos al tercio final",
    "Pases al área por 90",
    "% de pases precisos al área",
    "Pases entre líneas por 90",
    "% de pases entre líneas precisos",
    "Pases profundos por 90",
    "Centros profundos completados por 90",
    "Pases progresivos por 90",
    "% de pases progresivos precisos",
    "Vallas invictas",
    "% de atajadas",
    "Goles evitados",
    "Goles evitados por 90",
    "Salidas por 90",
]

# Crear un diccionario para traducir los nombres
traducciones = dict(zip(estadisticas, estadisticas_traducidas))

# Renombrar las columnas del DataFrame
df.rename(columns=traducciones, inplace=True)

parametros_radar = [
    "Team within selected timeframe",
    "Player",
    "Age",
    "Goles",
    "xG (Goles esperados)",
    "Asistencias",
    "xA (Asistencias esperadas)",
    "Duelos por 90",
    "% de duelos ganados",
    "Acciones defensivas exitosas por 90",
    "Duelos defensivos por 90",
    "% de duelos defensivos ganados",
    "Duelos aéreos por 90",
    "% de duelos aéreos ganados",
    "Barridas por 90",
    "Barridas ajustadas por posesión",
    "Tiros bloqueados por 90",
    "Intercepciones por 90",
    "Intercepciones ajustadas por posesión",
    "Acciones ofensivas exitosas por 90",
    "Goles por 90",
    "Goles sin penales",
    "Goles sin penales por 90",
    "xG por 90",
    "Goles de cabeza",
    "Goles de cabeza por 90",
    "Tiros",
    "Tiros por 90",
    "% de conversión de goles",
    "Asistencias por 90",
    "Centros por 90",
    "Centros al área chica por 90",
    "Regates por 90",
    "% de regates exitosos",
    "Duelos ofensivos por 90",
    "% de duelos ofensivos ganados",
    "Carreras progresivas por 90",
    "Aceleraciones por 90",
    "Faltas recibidas por 90",
    "Pases por 90",
    "% de Pases precisos",
    "Pases hacia adelante por 90",
    "Pases largos por 90",
    "% de pases largos precisos",
    "xA por 90",
    "Asistencias de tiro por 90",
    "Segundas asistencias por 90",
    "Pases inteligentes por 90",
    "Pases clave por 90",
    "Pases al tercio final por 90",
    "Pases al área por 90",
    "Pases entre líneas por 90",
    "Pases profundos por 90",
    "Centros profundos completados por 90",
    "Pases progresivos por 90",
    "Vallas invictas",
    "% de atajadas",
    "Goles evitados",
    "Goles evitados por 90",
    "Salidas por 90",
]

# Filtrar columnas del DataFrame
dfradar = df[parametros_radar]

# Selección de estadísticas
params = st.sidebar.multiselect(
    "Selecciona las estadísticas", 
    parametros_radar[3:],  # Opciones desde "Goles" en adelante
    default=parametros_radar[3:8]  # Valores preseleccionados
)

# Filtrar jugadores según edad y equipo
mas29 = dfradar[(dfradar['Age'] >= 29) & (dfradar['Team within selected timeframe'].isin(["River Plate Res.", "River Plate"]))]
menos24 = dfradar[(dfradar['Age'] <= 22) & (dfradar['Team within selected timeframe'].isin(["River Plate Res.", "River Plate"]))]

# Selección de jugadores
st.sidebar.title("Comparación de Jugadores")
jugador1 = st.sidebar.selectbox("Selecciona el Jugador 1", menos24['Player'].unique())
jugador2 = st.sidebar.selectbox("Selecciona el Jugador 2", mas29['Player'].unique())

if params:
    values_jugador1 = menos24[menos24['Player'] == jugador1][params].iloc[0].values
    values_jugador2 = mas29[mas29['Player'] == jugador2][params].iloc[0].values

    low = dfradar[params].min().values
    high = dfradar[params].max().values

    radar = Radar(params, low, high,
                  round_int=[False] * len(params),
                  num_rings=4,
                  ring_width=1, center_circle_radius=1)
    
    fig, axs = grid(figheight=14, grid_height=0.915, title_height=0.06, endnote_height=0.025,
                    title_space=0, endnote_space=0, grid_key='radar', axis=False)

    radar.setup_axis(ax=axs['radar'], facecolor='None')
    radar.draw_circles(ax=axs['radar'], facecolor='#28252c', edgecolor='#39353f')
    radar.draw_radar_compare(values_jugador1, values_jugador2, ax=axs['radar'],
                             kwargs_radar={'facecolor': '#fa3434', 'alpha': 0.6},
                             kwargs_compare={'facecolor': '#4b7afa', 'alpha': 0.6})
    radar.draw_range_labels(ax=axs['radar'], fontsize=8, color='#fcfcfc')
    radar.draw_param_labels(ax=axs['radar'], fontsize=10, color='#fcfcfc')

    axs['endnote'].text(0.99, 0.5, "Data from WyScout Credits: @Lanusstats Inspired By: StatsBomb / Rami Moghadam",
                        color='#fcfcfc', fontsize=15, ha='right', va='center')

    axs['title'].text(0.01, 0.65, f'{jugador1}', fontsize=25,
                      ha='left', va='center', color='#fa3434')
    axs['title'].text(0.99, 0.65, f'{jugador2}', fontsize=25,
                      ha='right', va='center', color='#4b7afa')
    axs['title'].text(0.50, 0.65, 'Estadísticas por 90', fontsize=25,
                      ha='center', va='center', color='#ffffff')

    fig.set_facecolor('#121212')
    st.pyplot(fig)
else:
    st.write("Selecciona al menos una estadística para generar el gráfico.")


