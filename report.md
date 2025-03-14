# Отчет проекта "Phoebe Buffay Chatbot"

## Данные
Используются цитаты Фиби Буффе (`phoebe_quotes.csv`), содержащие реплики из сериала "Друзья". Данные были предварительно очищены и подготовлены для обучения.

## Архитектура
Retrieval-Based бот, использующий два метода поиска:
1. **TF-IDF + Косинусное сходство**: Быстрый метод, основанный на частоте слов.
2. **Sentence-BERT**: Современный метод, учитывающий семантику текста.

## Предобработка данных
- Удаление пустых строк и слишком коротких реплик.
- Токенизация и создание эмбеддингов для Sentence-BERT.
- Разделение данных на обучающую и тестовую выборки.

## Обучение
1. **TF-IDF**: Используется для быстрого поиска похожих реплик.
2. **Sentence-BERT**: Создаются эмбеддинги из цитат Фиби с использованием модели `paraphrase-MiniLM-L6-v2`. Модель быстро инферит и легко развертывается.

## Качество и итерации
- **Baseline**: Начали с простого метода TF-IDF.
- **Улучшение**: Перешли на Sentence-BERT для учета семантики текста.
- **Оценка**: Провели эксперименты и выбрали лучший метод (Sentence-BERT с точностью 90%).

## Итог
Чат-бот успешно отвечает репликами в стиле Фиби Буффе, учитывая ограниченные возможности Retrieval-Based подхода. Для улучшения качества можно расширить базу данных или использовать генеративные модели в будущих итерациях.

## Как запустить проект

### Шаги для запуска:
1. Установите зависимости:
   pip install -r requirements.txt
2. Скачайте данные:
    python download.py
3. Предобработайте данные:
    python model/preprocess.py
4. Обучите модель:
    python model/train.py
5. Запустите веб-сервис:
    uvicorn app.main:app --reload
6. Откройте index.html в браузере для использования HTML-интерфейса.