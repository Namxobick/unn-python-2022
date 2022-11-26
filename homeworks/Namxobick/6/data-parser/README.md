# Необходимо реализовать простой парсер данных.

## 1. На вход подается `csv` список email адресов, вида:

```csv
"Sincere@april.biz","Shanna@melissa.tv","anastasia.net"
```

## 2. Получаем по переданным почтам `id` пользователей с сайта: https://jsonplaceholder.typicode.com/users/

## 3. Для каждого пользователя необходимо скачать всю информацию по его `posts`, `albums` и `todos`, пример:

- https://jsonplaceholder.typicode.com/users/1/posts
- https://jsonplaceholder.typicode.com/users/1/albums
- https://jsonplaceholder.typicode.com/users/1/todos

## 4. В качестве результата необходимо сохранить всю информацию о каждом пользователе в виде `xml` файла вида:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<user>
  <id>1</id>
  <email>Sincere@april.biz</email>

  <posts>
    <post>
      <id>1</id>
      <title>sunt aut facere repellat provident occaecati excepturi optio reprehenderit</title>
      <body>quia et suscipit suscipit recusandae consequuntur expedita et cum reprehenderit molestiae ut ut quas totam nostrum rerum est autem sunt rem eveniet architecto</body>
    </post>
  </posts>

  <albums>
    <album>
      <id>1</id>
      <title>omnis laborum odio</title>
    </album>
  </albums>

  <todos>
    <todo>
      <id>1</id>
      <title>delectus aut autem</title>
      <completed>false</completed>
    </todo>
  </todos>
</user>
```

Если у пользователя нет какой-то части данных, например `posts`, то записываем просто `<posts></posts>`

## 5. Все файлы мы сохраняем в папку `users/${userId}/`, где `${userId}` заменяем на `id` пользователя

## 6. Необходимо логировать:

- количество пользователей для запуска
- переход к парсингу каждого конкретного `email`, пример: `Starts parsing for Sincere@april.biz`
- время выполнения каждого запроса к внешнему источнику данных
- логируем ошибки, если они случаются

# Технические требования:

- используем встроенный модуль `csv` для работы с `csv`
- Используем `poetry` для управления зависимостями
- Используем `loguru` для логирования
- Используем `requests` для выполнения запросов
- Можно выбрать любую библиотеку для работы с `xml`
