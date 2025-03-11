# Phoebe Buffay Chatbot

## Описание
Чат-бот, имитирующий манеру речи персонажа Фиби Буффе из сериала "Друзья". Бот использует Retrieval-Based подход, выбирая наиболее подходящий ответ из заранее подготовленного набора реплик. Для поиска ответов применяются методы TF-IDF и Sentence-BERT.

## Данные
Используются данные из цитат Фиби Буффе (`https://fangj.github.io/friends/season/`). 

Пример данных:
quote  
Wait, does he eat chalk?  
Just, 'cause, I don't want her to go through  
No.

## Инструкция по запуску

### Скачивание данных
python download.py

### Установка зависимостей
pip install -r requirements.txt


### Предварительная обработка данных
python model/preprocess.py


### Обучение модели 
python model/train.py


### Запуск веб-сервиса
uvicorn app.main --reload

yaml или через Docker:
docker build -t phoebebot .
docker run -p 8000:8000 phoebebot

Сделайте POST-запрос:
POST http://localhost:8000/chat/

С JSON-телом:
{
"query": "Hey Phoebe, sing a song?"
}

Запуск через HTML-интерфейс
Откройте файл index.html в браузере.

Введите ваш запрос в текстовое поле и нажмите "Отправить".

Ответ бота отобразится на экране.