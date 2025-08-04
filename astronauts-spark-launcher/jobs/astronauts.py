import requests

def main():
    response = requests.get("http://api.open-notify.org/astros.json")
    data = response.json()

    print("👨‍🚀 Astronautas no espaço agora:")
    for person in data["people"]:
        print(f"- {person['name']} ({person['craft']})")

if __name__ == "__main__":
    main()