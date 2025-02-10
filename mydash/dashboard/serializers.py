from rest_framework import serializers
from dashboard.models import Artist, Track, CountryChart

# 🎵 아티스트 직렬화
class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ["id", "spotify_id", "name", "genres", "popularity", "followers", "image_url"]

# 🎵 트랙(노래) 직렬화
class TrackSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer()  # 아티스트 정보를 포함

    class Meta:
        model = Track
        fields = ["id", "spotify_id", "title", "artist", "album", "popularity", "duration_ms", "preview_url", "image_url"]

# 🌍 국가별 차트 직렬화
class CountryChartSerializer(serializers.ModelSerializer):
    track = TrackSerializer()  # 트랙 정보를 포함

    class Meta:
        model = CountryChart
        fields = ["id", "country", "track", "rank", "chart_date"]
