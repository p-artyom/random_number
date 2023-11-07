# Случайное число

## Описание

Проект представляет из себя сервис генерации случайных чисел. Через _PGAdmin_
была создана хранимая процедура, которая заполняет таблицу текущей датой и
временем в поле _time_ и случайным значением от 0 до 10 в поле _value_.
Настроена задача, выполняющая данную процедуру каждые 5 секунд. Создан
триггер, записывающий время, когда значение было более 9 в отдельную таблицу.
Создано представление данных, которое выводит поминутно агрегированные данные
таблицы чисел. Получить представление можно отправив _GET_ запрос на адрес
`http://127.0.0.1:8000/api/get_aggregated_data/`. Сервис доступен только
авторизованным пользователям. Настроен _CI_ при пуше в ветку _main_.
 
## Технологии

- Python 3.10.12;
- PostgreSQL 14;
- PGAdmin 4;
- Django 4.2.5;
- Django REST framework 3.14.0;
- Gunicorn 21.2.0;
- Nginx 1.22.1.

## Запуск приложения локально в docker-контейнерах

Инструкция написана для компьютера с установленной _ОС Windows_ 10 или 11.

- Установите _Windows Subsystem for Linux_ по инструкции с официального сайта
[Microsoft](https://learn.microsoft.com/ru-ru/windows/wsl/install);

- Зайдите на
[официальный сайт Docker](https://www.docker.com/products/docker-desktop/),
скачайте и установите файл _Docker Desktop_;

- В корне проекта создайте .env файл и заполните следующими данными:

  - в переменной `POSTGRES_DB` должно быть название базы данных;

  - в переменной `POSTGRES_USER` должно быть имя пользователя БД;

  - в переменной `POSTGRES_PASSWORD` должен быть пароль пользователя БД;

  - в переменной `DB_HOST` должен быть адрес, по которому _Django_ будет
  соединяться с базой данных;

  - в переменной `DB_PORT` должен быть порт, по которому _Django_ будет
  обращаться к базе данных;

  - в переменную `SECRET_KEY` укажите секретный ключ для конкретной установки
  _Django_;

  - в переменную `DEBUG` укажите значение режима отладки;

  - в переменную `ALLOWED_HOSTS` укажите список строк, представляющих имена
  хоста/домена, которые может обслуживать это _Django_ приложение;

  - в переменную `PGADMIN_DEFAULT_EMAIL` укажите адрес электронной почты,
  используемый при первоначальной настройке учетной записи администратора в
  _PGAdmin_.

  - в переменную `PGADMIN_DEFAULT_PASSWORD` укажите пароль, используемый при
  первоначальной настройке учетной записи администратора в _PGAdmin_.

- В терминале в папке с `docker-compose.yml` выполните команду:

```text
docker compose up
```

- Перейдите в новом терминале в директорию, где лежит файл
`docker-compose.yml`, и выполните команды:

```text
docker compose exec backend python manage.py migrate
docker compose exec backend python manage.py collectstatic
docker compose exec backend cp -r /app/collected_static/. /backend_static/static/
```

- Панель администратора доступна по адресу `http://127.0.0.1:8000/admin/`;

- На странице `http://127.0.0.1:8000/api/docs/` можно ознакомиться с
документацией проекта;

- Откройте _PGAdmin_ по адресу `http://127.0.0.1:5050/`. Авторизуйтесь данными
из переменных `PGADMIN_DEFAULT_EMAIL` и `PGADMIN_DEFAULT_PASSWORD`. В верхней
панели откройте: _Tools_ -> _Query Tool_;

- Установите _PGAgent_:

```sql
CREATE EXTENSION pgagent;
```

- Перейдите в новом терминале в директорию с файлом `docker-compose.yml` и
выполните команды, где _dbname_ - название базы данных, _user_ - имя
пользователя БД:

```text
docker compose exec -it postgres bash
pgagent hostaddr=127.0.0.1 dbname=postgres user=postgres_user -s pgagent_log.log
```

- В _Query Tool_ выполните следующие запросы:

```sql
CREATE PROCEDURE public.create_random_value()
LANGUAGE 'sql'
AS $BODY$
INSERT INTO public.number_number ("time", value)
VALUES(clock_timestamp(), random()*10);
$BODY$;
ALTER PROCEDURE public.create_random_value()
OWNER TO postgres_user;
```

```sql
DO $$
DECLARE
    jid integer;
    scid integer;
BEGIN
-- Creating a new job
INSERT INTO pgagent.pga_job(
    jobjclid, jobname, jobdesc, jobhostagent, jobenabled
) VALUES (
    1::integer, 'run_create_random_value'::text, ''::text, ''::text, true
) RETURNING jobid INTO jid;

-- Steps
-- Inserting a step (jobid: NULL)
INSERT INTO pgagent.pga_jobstep (
    jstjobid, jstname, jstenabled, jstkind,
    jstconnstr, jstdbname, jstonerror,
    jstcode, jstdesc
) VALUES (
    jid, 'step1'::text, true, 's'::character(1),
    ''::text, 'postgres'::name, 'f'::character(1),
    'CALL public.create_random_value();
    SELECT pg_sleep(5);
    CALL public.create_random_value();
    SELECT pg_sleep(5);
    CALL public.create_random_value();
    SELECT pg_sleep(5);
    CALL public.create_random_value();
    SELECT pg_sleep(5);
    CALL public.create_random_value();
    SELECT pg_sleep(5);
    CALL public.create_random_value();
    SELECT pg_sleep(5);
    CALL public.create_random_value();
    SELECT pg_sleep(5);
    CALL public.create_random_value();
    SELECT pg_sleep(5);
    CALL public.create_random_value();
    SELECT pg_sleep(5);
    CALL public.create_random_value();
    SELECT pg_sleep(5);
    CALL public.create_random_value();
    SELECT pg_sleep(5);
    CALL public.create_random_value();'::text, ''::text
) ;

-- Schedules
-- Inserting a schedule
INSERT INTO pgagent.pga_schedule(
    jscjobid, jscname, jscdesc, jscenabled,
    jscstart, jscend,    jscminutes, jschours, jscweekdays, jscmonthdays, jscmonths
) VALUES (
    jid, 'schedule1'::text, ''::text, true,
    '2023-11-07 00:00:00 +08:00'::timestamp with time zone,
    '2024-11-07 00:00:00 080'::timestamp with time zone,
    -- Minutes
    '{t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,
    t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t}'::bool[]::boolean[],
    -- Hours
    '{t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t}'::bool[]::boolean[],
    -- Week days
    '{t,t,t,t,t,t,t}'::bool[]::boolean[],
    -- Month days
    '{t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t}'::bool[]::boolean[],
    -- Months
    '{t,t,t,t,t,t,t,t,t,t,t,t}'::bool[]::boolean[]
) RETURNING jscid INTO scid;
END
$$;
```

```sql
CREATE FUNCTION public.value_more_nine()
RETURNS trigger
LANGUAGE 'plpgsql'
COST null
VOLATILE NOT LEAKPROOF
AS $BODY$
BEGIN
IF NEW.value > 9 THEN
INSERT INTO public.number_numbermorenine("time", "value_more_nine")
VALUES(localtimestamp, NEW.value);
END IF;
RETURN NEW;
END;
$BODY$;

ALTER FUNCTION public.value_more_nine()
OWNER TO postgres_user;

COMMENT ON FUNCTION public.value_more_nine()
IS 'null';
```

```sql
CREATE OR REPLACE TRIGGER number_value_more_nine
BEFORE INSERT
ON public.number_number
FOR EACH ROW
EXECUTE FUNCTION public.value_more_nine();
```

```sql
CREATE VIEW public.minute_by_minute_aggregated_data AS
SELECT date_trunc('minute'::text, number_number."time") AS time_minute,
AVG(number_number.value) AS avg_value
FROM number_number
GROUP BY (date_trunc('year'::text, number_number."time")),
(date_trunc('month'::text, number_number."time")),
(date_trunc('day'::text, number_number."time")),
(date_trunc('hour'::text, number_number."time")),
(date_trunc('minute'::text, number_number."time"))
ORDER BY (date_trunc('year'::text, number_number."time")),
(date_trunc('month'::text, number_number."time")),
(date_trunc('day'::text, number_number."time")),
(date_trunc('hour'::text, number_number."time")),
(date_trunc('minute'::text, number_number."time"));

ALTER TABLE public.minute_by_minute_aggregated_data
OWNER TO postgres_user; 
```

-  Отправьте _GET_ запрос на адрес
`http://127.0.0.1:8000/api/get_aggregated_data/` для получения данных
представления.

## Автор

Пилипенко Артем
