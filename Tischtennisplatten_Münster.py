import streamlit as st
import plotly.graph_objects as go
import json

# Laden der GeoJSON-Datei
with open('tischtennisplatten_muenster.geojson', 'r', encoding='utf-8') as f:
    geojson_data = json.load(f)

# GeoJSON-Daten extrahieren
features = geojson_data['features']

# Extrahieren der Koordinaten und anderer relevanter Informationen
lats = [feature['geometry']['coordinates'][1] for feature in features]
lons = [feature['geometry']['coordinates'][0] for feature in features]
hover_texts = [
    f"Name: {feature['properties'].get('name', 'Unnamed')}<br>"
    f"Ort: {feature['properties'].get('ort', 'Unknown')}<br>"
    f"OrtID: {feature['properties'].get('ortId', 'Unknown')}<br>"
    f"Material: {feature['properties'].get('material', 'Unknown')}<br>"
    f"Typ: {feature['properties'].get('typ', 'Unknown')}"
    for feature in features
]

# Erstellen der Karte mit Plotly
fig = go.Figure(go.Scattermapbox(
    lat=lats,
    lon=lons,
    mode='markers',
    marker=go.scattermapbox.Marker(size=14),
    text=hover_texts,
    hoverinfo='text'
))

fig.update_layout(
    mapbox=dict(
        style="open-street-map",
        center=dict(lat=51.961563, lon=7.626135),
        zoom=10  # Vergrößerter Zoom-Ausschnitt
    ),
    margin={"r":0,"t":0,"l":0,"b":0}
)

# Darstellung der Karte in Streamlit
st.title("Tischtennisplatten in Münster")
st.plotly_chart(fig, use_container_width=True)
