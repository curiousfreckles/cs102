import requests
from datetime import datetime
import plotly
from config import config


def get(url, params={}, timeout=5, max_retries=5, backoff_factor=0.3):
    """ Выполнить GET-запрос

    :param url: адрес, на который необходимо выполнить запрос
    :param params: параметры запроса
    :param timeout: максимальное время ожидания ответа от сервера
    :param max_retries: максимальное число повторных запросов
    :param backoff_factor: коэффициент экспоненциального нарастания задержки
    """
    for n in range(max_retries):
        try:
            response = requests.get(query, params=params, timeout=timeout)
            content_type = response.headers.get('Content-Type')
            if not content_type == "application/json; charset=utf-8":
                raise
            return response
        except requests.exceptions.RequestException:
            if n == max_retries - 1:
                raise
            backoff_value = backoff_factor * (2 ** n)
            time.sleep(backoff_value)



def get_friends(user_id, fields=''):
    """ Returns a list of user IDs or detailed\
    information about a user's friends """
    assert isinstance(user_id, int), "user_id must be positive integer"
    assert isinstance(fields, str), "fields must be string"
    assert user_id > 0, "user_id must be positive integer"
    query_params = {
        'access_token': config.get("ACCESS_TOKEN"),
        'user_id': user_id,
        'fields': fields,
        'version': config.get('VERSION')
    }
    url = "{}/friends.get".format(config.get("DOMAIN"))
    response = get(url, params=query_params)

    return response.json()


def age_predict(user_id):
    """ Наивный прогноз возраста по возрасту друзей

    Возраст считается как медиана среди возраста всех друзей пользователя

    :param user_id: идентификатор пользователя
    """
    assert isinstance(user_id, int), "user_id must be positive integer"
    assert user_id > 0, "user_id must be positive integer"
    # PUT YOUR CODE HERE


def messages_get_history(user_id, offset=0, count=200):
    """ Получить историю переписки с указанным пользователем

    :param user_id: идентификатор пользователя, с которым нужно получить историю переписки
    :param offset: смещение в истории переписки
    :param count: число сообщений, которое нужно получить
    """
    assert isinstance(user_id, int), "user_id must be positive integer"
    assert user_id > 0, "user_id must be positive integer"
    assert isinstance(offset, int), "offset must be positive integer"
    assert offset >= 0, "user_id must be positive integer"
    assert count >= 0, "user_id must be positive integer"
    



def count_dates_from_messages(messages):
    """ Получить список дат и их частот

    :param messages: список сообщений
    """
    # PUT YOUR CODE HERE


def plotly_messages_freq(freq_list):
    """ Построение графика с помощью Plot.ly

    :param freq_list: список дат и их частот
    """
    # PUT YOUR CODE HERE


def get_network(users_ids, as_edgelist=True):
    # PUT YOUR CODE HERE


def plot_graph(graph):
    # PUT YOUR CODE HERE

#import matplotlib
#matplotlib.use('Agg')
#import matplotlib.pyplot as plt
#fig = plt.figure()
#ax = fig.add_subplot(111)
#ax.plot([1,2,3])
#fig.savefig('test.png')

if __name__ == '__main__':
    #get.friends