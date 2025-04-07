# The Smiths의 인기 노래 목록과 임의의 점수
songs = [
    {"title": "There Is a Light That Never Goes Out", "score": 95},
    {"title": "This Charming Man", "score": 90},
    {"title": "How Soon Is Now?", "score": 88},
    {"title": "Bigmouth Strikes Again", "score": 85},
    {"title": "The Boy with the Thorn in His Side", "score": 82},
    {"title": "Panic", "score": 80},
    {"title": "Heaven Knows I'm Miserable Now", "score": 78},
    {"title": "Ask", "score": 77},
    {"title": "Please, Please, Please, Let Me Get What I Want", "score": 75},
    {"title": "Girlfriend in a Coma", "score": 74}
]

# 인기 점수에 따라 노래 목록 정렬
sorted_songs = sorted(songs, key=lambda x: x["score"], reverse=True)

# 정렬된 노래 목록 출력
print("The Smiths의 인기 노래 순위:")
for idx, song in enumerate(sorted_songs, start=1):
    print(f"{idx}. {song['title']} (Score: {song['score']})")
