from django.db import models

# 아티스트 정보 저장
class Artist(models.Model):
    spotify_id = models.CharField(max_length=100, unique=True)  # Spotify 아티스트 ID
    name = models.CharField(max_length=255)
    genres = models.TextField(blank=True, null=True)  # 장르 정보
    popularity = models.IntegerField()
    followers = models.IntegerField()
    image_url = models.URLField(blank=True, null=True)  # 프로필 이미지 URL
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# 트랙 정보 저장
class Track(models.Model):
    spotify_id = models.CharField(max_length=100, unique=True)  # Spotify 트랙 ID
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="tracks")  # 아티스트와 연결
    album = models.CharField(max_length=255)
    popularity = models.IntegerField()
    duration_ms = models.IntegerField()  # 노래 길이 (밀리초)
    preview_url = models.URLField(blank=True, null=True)  # 미리 듣기 URL
    image_url = models.URLField(blank=True, null=True)  # 앨범 이미지
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.artist.name}"

# 국가별 차트 데이터 저장
class CountryChart(models.Model):
    country = models.CharField(max_length=50)  # 국가 (KR, US, GB 등)
    track = models.ForeignKey(Track, on_delete=models.CASCADE, related_name="charts")  # 트랙과 연결
    rank = models.IntegerField()  # 차트 순위
    chart_date = models.DateField()  # 차트 발표 날짜
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('country', 'track', 'chart_date')  # 동일한 국가, 동일한 노래, 동일한 날짜 중복 방지

    def __str__(self):
        return f"[{self.country}] {self.rank}. {self.track.title} - {self.track.artist.name} ({self.chart_date})"
