import requests

def fetch_random_jokes():
    url = "https://api.freeapi.app/api/v1/public/randomjokes/joke/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data: 
        user_data = data["data"]
        Jokes = user_data["content"]
        return Jokes
    else :
        raise Exception("Failed to fetch jokes")
    
def main():
    try:
        Jokes = fetch_random_jokes()
        print(f"Joke : {Jokes}\n")
    except Exception as e:
        print(str(e))
        

if __name__ == "__main__":
    main()