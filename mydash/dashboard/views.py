from rest_framework import generics
from dashboard.models import Artist, Track, CountryChart
from dashboard.serializers import ArtistSerializer, TrackSerializer, CountryChartSerializer

# 🌍 모든 국가별 차트 데이터 가져오기
class CountryChartListView(generics.ListAPIView):
    queryset = CountryChart.objects.all().order_by("country", "rank")
    serializer_class = CountryChartSerializer

# 🌍 특정 국가의 차트 데이터 가져오기
class CountryChartByCountryView(generics.ListAPIView):
    serializer_class = CountryChartSerializer

    def get_queryset(self):
        country = self.kwargs["country"]
        return CountryChart.objects.filter(country=country).order_by("rank")

# 🎵 모든 트랙 목록 가져오기
class TrackListView(generics.ListAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

# 🎵 특정 트랙의 상세 정보 가져오기
class TrackDetailView(generics.RetrieveAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    lookup_field = "spotify_id"  # Spotify ID 기준으로 조회

# 🎤 모든 아티스트 목록 가져오기
class ArtistListView(generics.ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

# 🎤 특정 아티스트의 상세 정보 가져오기
class ArtistDetailView(generics.RetrieveAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    lookup_field = "spotify_id"
