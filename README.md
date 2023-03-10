# django-orm-watching-storage

Сервис для отслеживание посещений хранилища, их длительности и выявление подозрительных посетителей, по картам доступа.

На главной странице доступен список всех активных карт доступа. По нажатию на имя пользователя будет доступен список его посещений хранилища.
На странице /storage_information будет список пользователей которые находятся в хранилище в данный момент. Так-же для каждого посещения доступна проверка на подозрительность. 
Если пользователь находился/находится в хранилище более часа в столбце "Подозрителен?" будет значение True, если визит не является подозрительным будет выведено значение False.

## установка

Для запуска вам потребуется `python3` и менеджер пакетов `pip`. Установите библиотеки из файла `requirements.txt` c помощью команды:

```
pip install -r requirements.txt
```
## main.py

Скрипт запуска сервера. Для начала работы используйте команду:

```
python .\main.py
```

В консоли будет выведена информация о запуске сервера:

```
System check identified no issues (0 silenced).
January 01, 2023 - 20:34:21
Django version 3.2.16, using settings 'project.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CTRL-BREAK.
```
Если сервер не доступен по ууказанному адресу используйте:  http://127.0.0.1:8000/

## datacenter

### active_passcards_view.py

Скрипт для выявления и отображения активных карт доступа и информации о владельцах.

### passcard_info_view.py

Скрипт для поиска и отображения информации о предыдущих визитах пользователя в хранилище.

### storage_information_view.py

Скрипт для поиска и отображения пользователей которые в данный момент находятся в хранилище.

### additional_scripts.py

Доподнительные функции которые используются описанными ранее скриптами для вычисления длительности нахождения пользователя в хранилище,
проверке на подозрительность и выводе данных в читаемом виде.

### models.py

Модели для взаиводействия с базой данных.

### templates

Папка с шаблона отображаемых страниц.

## project

Папка с файлами конфигурации сервера.