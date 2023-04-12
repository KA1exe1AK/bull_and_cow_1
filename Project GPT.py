# import requests
# from bs4 import BeautifulSoup
#
# # список социальных сетей
# social_networks = [
#     {
#         'name': 'VK',
#         'search_url': 'https://vk.com/search?c%5Bname%5D=1&c%5Bage_from%5D=&c%5Bage_to%5D=&c%5Bcity%5D=&c%5Bcountry%5D=1&c%5Bcompany%5D=0&c%5Bposition%5D=0&c%5Bsex%5D=&c%5Bnickname%5D=&c%5Bphoto%5D=0&c%5Bsection%5D=people&c%5Bq%5D='
#     },
#     {
#         'name': 'Instagram',
#         'search_url': 'https://www.instagram.com/web/search/topsearch/?query='
#     },
#     {
#         'name': 'Telegram',
#         'search_url': 'https://t.me/s/'
#     }
# ]
#
#
# # функция для отправки запроса и получения ответа
# def get_response(url):
#     response = requests.get(url)
#     return response.text
#
#
# # функция для анализа ответа и поиска совпадений
# def search_social_profiles(html, full_name, age, social_network):
#     soup = BeautifulSoup(html, 'html.parser')
#
#     # проверяем наличие профайла на VK
#     if social_network['name'] == 'VK':
#         vk_profile = soup.find('div', {'class': 'people_row'})
#         if vk_profile and full_name in vk_profile.get('data-name'):
#             print("Найден профиль на VK:", vk_profile.find('a').get('href'))
#
#     # проверяем наличие профайла на Instagram
#     elif social_network['name'] == 'Instagram':
#         instagram_data = soup.json()
#         for user in instagram_data['users']:
#             if full_name in user['user']['full_name']:
#                 print("Найден профиль на Instagram:", f"https://www.instagram.com/{user['user']['username']}/")
#
#     # проверяем наличие профайла на Telegram
#     elif social_network['name'] == 'Telegram':
#         tg_profile = soup.find('div', {'class': 'tgme_page_photo_image'})
#         if tg_profile and full_name in soup.find('div', {'class': 'tgme_page_title'}).text:
#             print("Найден профиль на Telegram:",
#                   social_network['search_url'] + tg_profile.find('img').get('src').split('/')[-1].split('_')[0])
#
#
# # получаем личные данные пользователя
# full_name = input("Введите свое полное имя: ")
# age = input("Введите свой возраст: ")
#
# # формируем запросы к социальным сетям
# for social_network in social_networks:
#     url = social_network['search_url'] + full_name
#     html = get_response(url)
#     search_social_profiles(html, full_name, age, social_network)

import numpy as np
import pandas as pd
import tensorflow as tf

# Загружаем датасет
data = pd.read_csv('weather_data.csv')

# Разбиваем данные на обучающую и тестовую выборки
train_data = data.sample(frac=0.8,random_state=200)
test_data = data.drop(train_data.index)

# Устанавливаем значения для нашей нейронной сети
n_inputs = 4
n_hidden1 = 4
n_outputs = 1
learning_rate = 0.01

# Создаем placeholder-ы для наших входных и выходных данных
X = tf.placeholder(tf.float32, shape=(None, n_inputs), name="X")
y = tf.placeholder(tf.float32, shape=(None), name="y")

# Создаем слои нашей нейросети
hidden1 = tf.layers.dense(X, n_hidden1, name="hidden1", activation=tf.nn.relu)
output = tf.layers.dense(hidden1, n_outputs, name="output")

# Определяем функцию потерь и выбираем оптимизатор
loss = tf.reduce_mean(tf.square(output - y))
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate)
training_op = optimizer.minimize(loss)

# Запускаем сессию TensorFlow
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)

    # Тренируем нейросеть
    for epoch in range(1000):
        sess.run(training_op, feed_dict={X: train_data[['temperature', 'humidity', 'pressure', 'wind_speed']], y: train_data['weather']})

    # Прогнозируем погодные условия
    predicted_weather = sess.run(output, feed_dict={X: test_data[['temperature', 'humidity', 'pressure', 'wind_speed']]})

    # Выводим результаты
    print(predicted_weather)