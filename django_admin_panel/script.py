import runpy
import sys
import time

time.sleep(2)  # Ждем на всякий.
# Фейк миграция movies, так как типо ставим на готовую базу.
sys.argv = ['', 'migrate', 'movies', '--fake']
runpy.run_path('./manage.py', run_name='__main__')

# Миграции Django.
sys.argv = ['', 'migrate']
runpy.run_path('./manage.py', run_name='__main__')

# Собираем статику.
sys.argv = ['', 'collectstatic', '--noinput']
runpy.run_path('./manage.py', run_name='__main__')

# Создаем суперпользователя(superuser/password).
runpy.run_path('./scripts/create_superuser.py', run_name='__main__')

# Заливаем данные в PGSQL.
runpy.run_path('./sqlite_to_postgres/load_data.py', run_name='__script__')
