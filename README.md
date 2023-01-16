# Для проверки:
    https://github.com/ZOMini/Auth_sprint_1 - репозиторий
    https://github.com/ZOMini/Auth_sprint_1/invitations - приглашение
    группа 13 - Пирогов Виталий/Игорь Синякин/Малик Гасанов (@malikzevs @ee2 @sinyakinmail - в пачке) 

# Запуск:
  - oauth - update:
    - 1-я проблема локально не подебажить под виндой, так как gunicorn под виндой не пашет, т.е. только в докере/linux
    - 2-я что бы callback-и прилетали от провайдера, нужен открытый порт на роутере(я в роутере прописал NAT) - [router](https://github.com/ZOMini/Auth_sprint_1/blob/main/router.jpg)
    - В общем при регистрации своего приложения/сайта у провайдера(yandex,mail, и т.д.) нужно указывать redirect_uri, в котором твой внешний ip и внешний порт который прокинули выше, иначе тестить не получится, хотя можно тупо воткнуть кабель с инетом в комп и принимать все, но это такое)...
    - Так как начал использовать[authlib](https://docs.authlib.org/en/latest/client/flask.html) то советую начать с одного провайдера(google or twitter) для них есть почти готовые решения и много стороннего материала по настройке authlib, в отличии от того же yandex/vk, там все методом научного тыка.
    - Тестировал тупо в браузере http://____.____.____.____:5000/api/v1/oauth_login?provider=vk  or  http://____.____.____.____:5000/api/v1/oauth_login?provider=yandex - должны прилететь пара старых добрых jwt токенов.
  - docker-compose:
    - docker-compose -f docker-compose-test.yml up --build
    - docker-compose -f docker-compose-prod.yml up --build
    - docker-compose -f docker-compose-dev.yml up --build
  - локально:
    -  останавливаем контейнер flask_auth, из выше запущенных, оставляем redis и bd
    -  в терминале:
    -  pip install -r requirements.txt
    -  из папки /flask_auth: python app.py
    -  http://127.0.0.1:5000/docs/v1/ - Swagger docs
    -  http://127.0.0.1:5000/api/v1/   + ручки
    -  примеры заросов [requests.http](https://github.com/ZOMini/Auth_sprint_1/blob/main/requests.http) - это для [REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) под VSCode - в PyCharm сами решайте как тестить.

# DEV:
  - 13.01.23 начал
    - добавил env TESTS и модифицировал тротлинг декоратор, чтобы тротлинг отключался в тестах.

# Проектная работа 7 спринта

Упростите регистрацию и аутентификацию пользователей в Auth-сервисе, добавив вход через социальные сервисы. Список сервисов выбирайте исходя из целевой аудитории онлайн-кинотеатра — подумайте, какими социальными сервисами они пользуются. Например, использовать [OAuth от Github](https://docs.github.com/en/free-pro-team@latest/developers/apps/authorizing-oauth-apps){target="_blank"} — не самая удачная идея. Ваши пользователи не разработчики и вряд ли имеют аккаунт на Github. А вот добавить Twitter, Facebook, VK, Google, Yandex или Mail будет хорошей идеей.

Вам не нужно делать фронтенд в этой задаче и реализовывать собственный сервер OAuth. Нужно реализовать протокол со стороны потребителя.

Информация по OAuth у разных поставщиков данных: 

- [Twitter](https://developer.twitter.com/en/docs/authentication/overview){target="_blank"},
- [Facebook](https://developers.facebook.com/docs/facebook-login/){target="_blank"},
- [VK](https://vk.com/dev/access_token){target="_blank"},
- [Google](https://developers.google.com/identity/protocols/oauth2){target="_blank"},
- [Yandex](https://yandex.ru/dev/oauth/?turbo=true){target="_blank"},
- [Mail](https://api.mail.ru/docs/guides/oauth/){target="_blank"}.

## Дополнительное задание

Реализуйте возможность открепить аккаунт в соцсети от личного кабинета. 

Решение залейте в репозиторий текущего спринта и отправьте на ревью.
