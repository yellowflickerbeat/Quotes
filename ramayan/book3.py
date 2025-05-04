import requests
from bs4 import BeautifulSoup

total_chapters = 75
all_tat_texts = []

for i in range(1, total_chapters + 1):
    url = f"https://valmikiramayan.net/utf8/aranya/sarga{i}/aranyasans{i}.htm"
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")
        tat_paragraphs = soup.find_all("p", class_="tat")

        chapter_texts = [p.get_text(strip=True) for p in tat_paragraphs]
        all_tat_texts.append({
            "chapter": i,
            "texts": chapter_texts
        })

        print(f"✅ Chapter {i} - Extracted {len(chapter_texts)} verses.")

    except requests.RequestException as e:
        print(f"❌ Failed to fetch Chapter {i}: {e}")

# Save output to file
with open("valmiki_ramayan_aranya_kanda.txt", "w", encoding="utf-8") as f:
    for chapter in all_tat_texts:
        f.write(f"--- Chapter {chapter['chapter']} ---\n")
        for verse in chapter["texts"]:
            f.write(verse + "\n")
        f.write("\n")

print("✅ Finished extracting all 75 chapters.")
