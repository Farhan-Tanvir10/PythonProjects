import requests, json, os, time

while True:
    time.sleep(1)
    os.system("cls")
    result = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})

    joke = result.json()
    # print(json.dumps(joke, indent=2))y

    jk = joke["joke"]
    id = joke["id"]

    print(jk)
    again = input("Want to go again> ")
    if again[0] != "y":
        break
