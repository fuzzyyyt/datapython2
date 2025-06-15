import csv

# 1. 락 곡 데이터베이스
song_database = [
    {
        "title": "The Cure - Pictures of You",
        "genre": "Alternative Rock",
        "tags": {"mood": "무기력", "weather": "비", "time": "밤"}
    },
    {
        "title": "Radiohead - Street Spirit (Fade Out)",
        "genre": "Alternative Rock",
        "tags": {"mood": "무기력", "weather": "비", "time": "밤"}
    },
    {
        "title": "U2 - With or Without You",
        "genre": "Rock",
        "tags": {"mood": "무기력", "weather": "비", "time": "밤"}
    },
    {
        "title": "Metallica - Master of Puppets",
        "genre": "Thrash Metal",
        "tags": {"mood": "분노", "weather": "맑음", "time": "오후"}
    },
    {
        "title": "Rage Against the Machine - Killing in the Name",
        "genre": "Rap Metal",
        "tags": {"mood": "분노", "weather": "맑음", "time": "오후"}
    },
    {
        "title": "Nirvana - Territorial Pissings",
        "genre": "Grunge",
        "tags": {"mood": "분노", "weather": "맑음", "time": "오후"}
    },
    {
        "title": "Bon Jovi - You Give Love a Bad Name",
        "genre": "Glam Rock",
        "tags": {"mood": "활기참", "weather": "맑음", "time": "아침"}
    },
    {
        "title": "Van Halen - Jump",
        "genre": "Hard Rock",
        "tags": {"mood": "활기참", "weather": "맑음", "time": "아침"}
    },
    {
        "title": "Queen - Don’t Stop Me Now",
        "genre": "Rock",
        "tags": {"mood": "활기참", "weather": "맑음", "time": "아침"}
    },
    {
        "title": "Pink Floyd - Comfortably Numb",
        "genre": "Progressive Rock",
        "tags": {"mood": "우울", "weather": "흐림", "time": "새벽"}
    },
    {
        "title": "The Smiths - Asleep",
        "genre": "Indie Rock",
        "tags": {"mood": "우울", "weather": "흐림", "time": "새벽"}
    },
    {
        "title": "The Cranberries - Ode to My Family",
        "genre": "Alternative Rock",
        "tags": {"mood": "우울", "weather": "흐림", "time": "새벽"}
    },
    {
        "title": "Journey - Faithfully",
        "genre": "Arena Rock",
        "tags": {"mood": "설렘", "weather": "맑음", "time": "밤"}
    },
    {
        "title": "Scorpions - Wind of Change",
        "genre": "Hard Rock",
        "tags": {"mood": "설렘", "weather": "맑음", "time": "밤"}
    },
    {
        "title": "Extreme - More Than Words",
        "genre": "Soft Rock",
        "tags": {"mood": "설렘", "weather": "맑음", "time": "밤"}
    }
]

# 2. 추천 함수: 점수 기반
def recommend_songs(mood, weather, time):
    scored_songs = []
    for song in song_database:
        score = 0
        if song["tags"]["mood"] == mood:
            score += 1
        if song["tags"]["weather"] == weather:
            score += 1
        if song["tags"]["time"] == time:
            score += 1
        if score > 0:
            scored_songs.append((score, song["title"]))
    scored_songs.sort(reverse=True)
    return [title for score, title in scored_songs[:3]] or ["조건에 맞는 추천이 없습니다."]

# 3. 사용자 입력
def get_user_input():
    print("\n기분 선택: 무기력 / 분노 / 활기참 / 우울 / 설렘")
    mood = input("당신의 기분은? ").strip()
    print("날씨 선택: 맑음 / 흐림 / 비")
    weather = input("현재 날씨는? ").strip()
    print("시간대 선택: 아침 / 오후 / 밤 / 새벽")
    time = input("지금은 어떤 시간대인가요? ").strip()
    return mood, weather, time

# 4. 저장
def save_playlist(songs):
    filename = input("저장할 파일 이름을 입력하세요 (예: playlist.csv): ")
    with open(filename, mode='w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["추천 플레이리스트"])
        for song in songs:
            writer.writerow([song])
    print(f"{filename}에 저장 완료.")

# 5. 불러오기
def load_playlist():
    filename = input("불러올 파일 이름을 입력하세요: ")
    try:
        with open(filename, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)  # 헤더 스킵
            print("\n저장된 플레이리스트:")
            for row in reader:
                print("- " + row[0])
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")

# 6. 메인 실행
def main():
    mood, weather, time = get_user_input()
    songs = recommend_songs(mood, weather, time)

    print("\n추천된 락 플레이리스트:")
    for s in songs:
        print("- " + s)

    if input("\n저장하시겠습니까? (y/n): ").lower() == 'y':
        save_playlist(songs)

    if input("이전 플레이리스트를 불러올까요? (y/n): ").lower() == 'y':
        load_playlist()

if __name__ == "__main__":
    main()
