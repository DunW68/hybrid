# Для развертывания проекта локально:

  1. Создать папку с виртуальным окружением Virtualenv
  2. В этой папке выполнить команды (с активированным виртуальным окружением):
       <p> 2.1 git clone --branch main https://github.com/DunW68/hybrid.git
       <p>2.2 cd "hybrid"
       <p> 2.3 pip install -r requirements.txt
       <p> 2.4 python manage.py makemigrations
       <p> 2.5 python manage.py migrate
  3. Проект готов к работе!
 <p>На случай проблем с установкой fasttext: https://fasttext.cc/docs/en/support.html


# Описание точек и методов на них:

  Для начала работы с функционалом api нужно получить токен, для этого нужно создать аккаунт:
      <p> POST http://127.0.0.1:8000/api/v1/auth/registration/
           
       Необходимые параметры:
           username
           password1
           password2
       Пример запроса:
        {
            "username":"user",
            "password1":"asdvmn3545#@5",
            "password2":"asdvmn3545#@5"
        }
        
  Если пользователь уже существует, то токен можно взять здесь:
      <p> POST http://127.0.0.1:8000/api/v1/auth/login/
       
        Необходимые параметры:
          username
          password
        Пример запроса:
        {
            "username":"user",
            "password":"asdvmn3545#@5"
        }
        

# Основной функционал api:
  1)	GET http://127.0.0.1:8000/api/v1/train_model/
         <p>Выводит список всех тренированных моделей
         При переобучении модели, она обновляется в базе данных
  2)	POST http://127.0.0.1:8000/api/v1/train_model/
    <p>Загрузка файла для тренировки модели и сохранение этой модели в базе данных
    
             Необходимые параметры:
               file
             Пример запроса:
             {
                 "file":"cooking_train.bin"
             }
          
  3) GET http://127.0.0.1:8000/api/v1/downloaded_models/
    <p>Вывод всех доступных загруженных моделей. 
    Если добавить в запрос ?lang_code="code language" начнется загрузка
    новой модели по двубуквенному коду языка (коды языка можно посмотреть здесь: 
    https://fasttext.cc/docs/en/language-identification.html#list-of-supported-languages)
    
    Пример запроса для загрузки модели:
    http://127.0.0.1:8000/api/v1/downloaded_models?lang_code=ru
    
  4) POST http://127.0.0.1:8000/api/v1/downloaded_models/
    <p>Показывает векторы для каждого слова в предложении (из параметра sentence в выбранной моделе)
    
          Необходимые параметры:
            model
            sentence
          Пример запроса:
          {
              "model":"cc.en.300.bin",
              "sentence":"Привет модель"
          }
        
  5) GET http://127.0.0.1:8000/api/v1/predict/
    <p>Выводит все тренированные модели
  6) POST http://127.0.0.1:8000/api/v1/predict/
    <p>На основе предложения выводит предполагаемую метку
    
          Необходимые параметры:
            model
            sentence
          Пример запроса:
          {
              "model":"cooking_train.bin",
              "sentence":"Why not put knives in the dishwasher?"
          }
   Остальная документация находится здесь:
      http://127.0.0.1:8000/swagger
      или
      http://127.0.0.1:8000/redoc
