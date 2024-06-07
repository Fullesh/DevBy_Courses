## Запуск проекта с использованием Docker

### Шаги по запуску

1. **Клонируйте репозиторий**
    ```bash
    git clone https://github.com/Fullesh/DevBy_Courses.git
    cd DevBy_Courses
    ```

2. **Переименуйте пример файла окружения с .env_example в .env и отредактируйте его**

3. **Постройте и запустите контейнеры Docker**
    ```
    docker-compose build
    docker-compose up
    ```

5. **Создание суперпользователя**
    ```
    docker-compose exec app python manage.py csu
    ```
    *Дополнительно* \
    Данные для входа под аккаунтом администратора: \
    *Логин: admin@service.py* \
    *Пароль: 1* 

### Доступ к приложению
- Приложение будет доступно по адресу: [http://localhost:8000](http://localhost:8000)
- Админ панель Django: [http://localhost:8000/admin](http://localhost:8000/admin)

### Остановка контейнеров
Для остановки контейнеров используйте следующую команду:

```
docker-compose down
```
