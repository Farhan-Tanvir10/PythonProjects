import requests, json, time

for i in range(10):
    result = requests.get("https://randomuser.me/api/")
    if result.status_code == 200:
        user = result.json()

        name = f"{user["results"][0]["name"]["first"]} {user["results"][0]["name"]["first"]}"


        for person in user["results"]:
            filename = f"""{person["name"]["first"].lower()} {person["name"]["last"].lower()}.jpg"""
            # print(filename)
            picture = requests.get(person["picture"]["large"])
            f = open(filename, "wb")
            f.write(picture.content)
            f.close()
            print(f"Saved {filename}")
            time.sleep(1)