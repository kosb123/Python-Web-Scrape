import requests
import os


def ask_user():
    answer = input("Do you want to start over? y/n ")
    return answer


def answer_user(answer):
    answer = answer.lower()
    if answer == 'y':
        IsItDown()
    elif answer == 'n':
        print('k. bye!')
    else:
        print("That's not a valid answer")
        answer_now = ask_user()
        answer_user(answer_now)


def IsItDown():
    os.system('cls')
    print("Welcome to IsItDown.py!\nPlease write a URLs you want to check. (separated by comma)")
    url = input()
    url = url.split(',')

    for get_url in url:
        get_url_lower = get_url.lower().strip()
        if '.com' in get_url_lower:
            if 'http://' in get_url_lower:
                try:
                    r = requests.get(get_url_lower)
                    if r.status_code == 200:
                        print(f"{get_url_lower} is up!")
                    else:
                        print(f"{get_url_lower} is down!")
                except:
                    print(f"{get_url_lower} is down!")
            else:
                get_url_lower = f"http://{get_url_lower}"
                try:
                    r = requests.get(get_url_lower)
                    if r.status_code == 200:
                        print(f"{get_url_lower} is up!")
                    else:
                        print(f"{get_url_lower} is down!")
                except:
                    print(f"{get_url_lower} is down!")
        else:
            print(f"{get_url_lower} is not a valid URL.")
        #r = requests.get(get_url_lower)
        # print(r.status_code)

    answer = ask_user()
    answer_user(answer)


IsItDown()
