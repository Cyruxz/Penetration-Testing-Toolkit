import requests

def dir_brute(url, wordlist):
    with open(wordlist) as f:
        for word in f:
            word = word.strip()
            full_url = f"{url}/{word}"
            r = requests.get(full_url)
            if r.status_code == 200:
                print(f"[FOUND] {full_url}")
