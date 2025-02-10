from django.urls import path
from dashboard.views import (
    CountryChartListView,
    CountryChartByCountryView,
    TrackListView,
    TrackDetailView,
    ArtistListView,
    ArtistDetailView
)

urlpatterns = [
    path("api/charts/", CountryChartListView.as_view(), name="all_charts"),  # 모든 국가 차트
    path("api/charts/<str:country>/", CountryChartByCountryView.as_view(), name="charts_by_country"),  # 특정 국가 차트
    path("api/tracks/", TrackListView.as_view(), name="track_list"),  # 모든 트랙
    path("api/tracks/<str:spotify_id>/", TrackDetailView.as_view(), name="track_detail"),  # 특정 트랙
    path("api/artists/", ArtistListView.as_view(), name="artist_list"),  # 모든 아티스트
    path("api/artists/<str:spotify_id>/", ArtistDetailView.as_view(), name="artist_detail"),  # 특정 아티스트
]
