import requests
import os

# Spotify API 인증 (Access Token 가져오기)
def get_spotify_token():
    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret
    }
    
    response = requests.post(url, headers=headers, data=data)
    response_json = response.json()
    
    return response_json.get("access_token")

token = get_spotify_token()
print(token)

# 특정 국가의 차트 데이터 가져오기
def get_top_tracks_by_country(country="KR", limit=10):
    token = get_spotify_token()
    
    url = f"https://api.spotify.com/v1/playlists/37i9dQZEVXbK{country}ZpWD7X"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Error fetching data: {response.json()}")
        return []
    
    playlist_data = response.json()
    
    tracks = []
    for idx, item in enumerate(playlist_data.get("tracks", {}).get("items", []), start=1):
        track_info = item["track"]
        artist_info = track_info["artists"][0]
        
        tracks.append({
            "spotify_id": track_info["id"],
            "title": track_info["name"],
            "artist_id": artist_info["id"],
            "artist_name": artist_info["name"],
            "album": track_info["album"]["name"],
            "popularity": track_info["popularity"],
            "image_url": track_info["album"]["images"][0]["url"] if track_info["album"]["images"] else None,
            "rank": idx,
        })
    
    return tracks
