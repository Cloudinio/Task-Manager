Привет! Есть два способа запустить проект: через докер или локально

ДОКЕР:
1)создайте .env и добавьте строки из .env.example
2)Сгенерируйте свой secret_key: откройте терминал и введите строку
<python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())">,
затем скопируйте вывод и вставьте вместо ENTER YOUR SECRET KEY
3)соберите образ докера командой <docker compose build>
4)соберите проект командой <docker compose up>
5)создание суперпользователя командой <docker compose run web python manage.py createsuperuser>

ЛОКАЛЬНО:
1)создайте .env и добавьте строки из .env.example
2)Сгенерируйте свой secret_key: откройте терминал и введите строку
<python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())">,
затем скопируйте вывод и вставьте вместо ENTER YOUR SECRET KEY
3)Сделайте свое виртуальное окружение
4)выполните миграции <python manage.py migrate>
5)создайте суперпользователя <python manage.py createsuperuser>
6)запуск сервера <python manage.py runserver>