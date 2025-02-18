import requests

def check_username(username):
    url = f"https://www.instagram.com/{username}/"
    response = requests.get(url)
    
    if response.status_code == 404:
        print(f"{username} is available!")
        with open("av.txt", "a") as file:
            file.write(username + "\n")
    else:
        print(f"{username} is taken.")

if __name__ == "__main__":
    with open("us.txt", "r") as file:
        usernames = file.read().splitlines()
    
    for user in usernames:
        check_username(user)
