# dashboard/dash_apps.py
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from django_plotly_dash import DjangoDash
from .models import SpotifyChart  # Spotify 데이터 모델 (임시)

# Dash 애플리케이션 생성
app = DjangoDash('SpotifyDashboard')

# 임시 데이터
data = {
    "track_name": ["Song A", "Song B", "Song C", "Song D", "Song E"],
    "streams": [50000, 42000, 39000, 37000, 35000],
    "rank": [1, 2, 3, 4, 5]
}
df = pd.DataFrame(data)

# 레이아웃 구성
app.layout = html.Div([
    html.H1("Spotify Dashboard", style={'textAlign': 'center', 'color': '#1DB954'}),
    
    dcc.Dropdown(
        id='country-dropdown',
        options=[
            {'label': 'South Korea', 'value': 'KR'},
            {'label': 'USA', 'value': 'US'},
            {'label': 'Japan', 'value': 'JP'}
        ],
        value='KR',
        style={'width': '50%', 'margin': 'auto'}
    ),

    dcc.Graph(
        id='weekly-chart',
        figure=px.bar(df, x='track_name', y='streams', title='Weekly Top Songs')
    ),

    dcc.Graph(
        id='artist-trend',
        figure=px.line(df, x='rank', y='streams', title='Artist Rank Trend')
    )
])
