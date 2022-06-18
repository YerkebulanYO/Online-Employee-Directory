# Онлайн каталог сотрудников

Чтобы скачать файл необходимо скопировать эту команду и вывести в терминал:

``` git clone https://github.com/YerkebulanYO/Online-Employee-Directory.git ```

После скачивании переходим в папку Online-Employee-Directory в терминале

И после этого выводим эту команду в терминал:

``` python manage.py runserver ```

или

``` python3 manage.py runserver ```

Убедитесь что вы до этого скачали python и django.

После этого переходим в http://127.0.0.1:8000

И придется немного подождать. Загружается 50.0000 сотрудников. 

После загрузки сайта у вас будет аккаунт. Вы можете выйти из аккаунта нажав на кнопку 'Logout'.

# Выполненные пункты

## Пункт 1. 
Информация о каждом сотруднике должна храниться в базе данных и содержать следующие данные:
○ ФИО;
○ Должность;
○ Дата приема на работу;
○ Размер заработной платы;

## Решение. 
Иерархия сотрудников состоит из 5 уровней. Intern, Junior, Middle, Senior, President. У каждого есть ФИО - full_name, должность - Position, дата приема на работу - employment_date, размер заработной платы - salary.

## Пункт 2.  

● У каждого сотрудника есть 1 начальник;

## Решение.
У каждого сотрудника есть начальник выше его уровня. Начальника нету у сотрудников с позицией President

## Пункт 3.

● База данных должна содержать не менее 50 000 сотрудников и 5 уровней иерархий.

## Решение.

В миграции хранится 51.000 сотрудников.

## Пункт 4.

Добавьте возможность поиска сотрудников по любому полю.

## Решение.

Вы можете произвести поиск сотрудников а так же комбинировать условия.

## Пункт 5.

Добавьте возможность сортировать.

## Решение.

Вы можете сортировать нажав на верхний заголовок. А так же сортировать в обратном порядке.

## Пункт 6.

Осуществите аутентификацию пользователя для зарегистрированных пользователей.

## Решение

Вы можете зарегистрироваться в и пройти аутентифицкаию. А чтобы выйти из аккаунта нажав на кнопку Logout

## Пункт 7.

Сделайте функционал разработанный в задачах 3, 4 и 5 доступный только для
зарегистрированных пользователей.

## Решение

Функционал добавлен. Если пользователь не зарегистрирован то он не может посмотреть список. 

## Пункт 8.

В разделе доступном только для зарегистрированных пользователей,
реализуйте остальные CRUD операции для записей сотрудников. Пожалуйста заметьте, что все поля касающиеся пользователей должны быть редактируемыми, включая начальника каждого сотрудника.

## Решение.

CRUD добавлен.  Вы можете добавить, посмотреть содержимое, удалить, изменить данные о сотрудниках а так же менять начальника. 

