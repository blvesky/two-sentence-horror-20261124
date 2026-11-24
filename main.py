import os

STORY = "Tonight was my turn to read to our daughter, so I opened her bedroom door at eight. She was already asleep, and the voice reading to her did not stop."

def main():
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(STORY)
    os.chmod(path, 0o644)

if __name__ == "__main__":
    main()
