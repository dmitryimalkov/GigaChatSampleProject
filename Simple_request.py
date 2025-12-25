from gigachat import GigaChat

# Укажите ключ авторизации, полученный в личном кабинете, в интерфейсе проекта GigaChat API
with GigaChat(credentials="Authorization key", verify_ssl_certs=False) as giga:
    response = giga.chat("2+2")
# Ответ по доступным моделям
    print(response.choices[0].message.content)
    response = giga.get_models()
    print(response)
# Получение токена
    response = giga.get_token()
    print(response)


