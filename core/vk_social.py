import requests
import time

def auth(code):
    request_link = 'https://oauth.vk.com/access_token?client_id=7429099&client_secret=2O8UyOG7nXIHLgF3kZqG&redirect_uri=http://127.0.0.1:8000/final&code={0}'
    request_link = request_link.format(code)
    try:
        r = requests.get(url=request_link)
    except Exception as e:
        error_report = "<h1 style='color:blue'>Сервер ВКонтакте временно недоступен. Повторите попытку позже. </h1>"
        return error_report
    data = r.json()
    print(data)
    access_token = data['access_token']
    user_id = data['user_id']
    request_link = "https://api.vk.com/method/users.get?user_ids={0}&fields=bdate&access_token={1}&v=5.101"
    request_link = request_link.format(user_id, access_token)
    try:
        r = requests.get(url=request_link)
    except Exception as e:
        error_report =  "<h1 style='color:blue'>Сервер ВКонтакте временно недоступен. Повторите попытку позже. </h1>"
        return error_report
    data = r.json()
    first_name = data['response'][0]['first_name']
    last_name = data['response'][0]['last_name']
    greeting_string = '{0} {1}<br>'
    greeting_string = greeting_string.format(first_name, last_name)
    request_link = "https://api.vk.com/method/friends.get?order=random&count=5&access_token={0}&v=5.101 "
    request_link = request_link.format(access_token)
    try:
        r = requests.get(url=request_link)
    except Exception as e:
        error_report = "<h1 style='color:blue'>Сервер ВКонтакте временно недоступен. Повторите попытку позже. </h1>"
        return error_report
    data = r.json()
    array_of_friends_ID = data['response']['items']
    amount_of_friends = len(array_of_friends_ID)
    if amount_of_friends == 0 :
        greeting_string += 'У вас нет друзей'
        return greeting_string
    elif amount_of_friends < 5 :
        greeting_string += 'У вас меньше 5 друзей: <br>'
        for i in range(amount_of_friends):
            user_id = str(array_of_friends_ID[i])
            time.sleep(0.5)
            request_link = "https://api.vk.com/method/users.get?user_ids={0}&fields=bdate&access_token={1}&v=5.101"
            request_link = request_link.format(user_id, access_token)
            try:
                r = requests.get(url=request_link)
            except Exception as e:
                error_report =  "<h1 style='color:blue'>Сервер ВКонтакте временно недоступен. Повторите попытку позже. </h1>"
                return error_report
            data = r.json()
            temp_first_name = data['response'][0]['first_name']
            temp_last_name = data['response'][0]['last_name']
            temp_new_string = '{0} {1} \n'
            temp_new_string = temp_new_string.format(temp_first_name, temp_last_name)
            new_string = '<a href="https://vk.com/id{0}">{1}</a><br> '
            new_string = new_string.format(user_id, temp_new_string)
            greeting_string += new_string
        return greeting_string
    else:
        greeting_string += '5 случайных друзей из вашего списка: <br>'
        for i in range(amount_of_friends):
            user_id =str(array_of_friends_ID[i])
            time.sleep(0.5)
            request_link = "https://api.vk.com/method/users.get?user_ids={0}&fields=bdate&access_token={1}&v=5.101"
            request_link = request_link.format(user_id, access_token)
            try:
                r = requests.get(url=request_link)
            except Exception as e:
                error_report =  "<h1 style='color:blue'>Сервер ВКонтакте временно недоступен. Повторите попытку позже. </h1>"
                return error_report
            data = r.json()
            temp_first_name = data['response'][0]['first_name']
            temp_last_name = data['response'][0]['last_name']
            temp_new_string = '{0} {1} \n'
            temp_new_string = temp_new_string.format(temp_first_name, temp_last_name)
            new_string = '<a href="https://vk.com/id{0}">{1}</a><br> '
            new_string = new_string.format(user_id, temp_new_string)
            greeting_string += new_string
        return greeting_string
