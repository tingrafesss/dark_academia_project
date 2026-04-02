Django-проект «dark academia» (обновлённая версия)

1. Установите зависимости (в виртуальном окружении):
   pip install django

2. Перейдите в папку проекта:
   cd dark_academia_project

3. Выполните миграции:
   ./venv_python manage.py migrate
   (у вас это была команда вида: ./.venv/bin/python manage.py migrate)

4. Запустите сервер разработки той же командой:
   ./.venv/bin/python manage.py runserver

5. Откройте в браузере:
   http://127.0.0.1:8000/

Страницы:
- /          — главная
- /about/    — о жанре
- /books/    — книги
- /authors/  — авторы
- /news/     — список статей
- /news/reading-start/   — статья про книги для входа в жанр
- /news/adaptations/     — статья про экранизации
- /news/playlist/        — статья про плейлист

Статика:
- CSS: static/css/styles.css  — цвета, шрифты, тени
- JS: static/js/script.js     — бургер-меню, генератор цитат и настроения
- Изображения: static/img/
- Шрифты: static/fonts/

Замените:
- файлы background-cathedral.jpg и background-handwriting.jpg на свои фоны;
- обложки taina-istoria.jpg, devyatyi-dom.jpg, esli-by-my-byli-zlodeyami.jpg, shesterka-atlasa.jpg;
- шрифты DaSerif-*.woff2 в static/fonts и/или правьте @font-face в css.
