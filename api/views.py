from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import FastTextModel, DataForTrain, DownloadModel
from .serializers import TrainModelSerializer


class TrainModelView(APIView):
    serializer_class = TrainModelSerializer
    # вывод всех тренированных моделей

    def get(self, request):
        data = FastTextModel.objects.all()
        response = []
        for obj in data:
            response.append(str(obj.file))
        return Response(response)

    # загрузка файла для тренировки модели и сохранение этой модели в базе данных
    def post(self, request):
        file = request.data['file']
        file_name = str(file)[:-4] + '.bin'
        try:
            exist = FastTextModel.objects.get(file=file_name)
        except Exception:
            exist = None
        if exist:
            # есть в базе
            from fasttext import train_supervised
            model = train_supervised(input=f"{file}", loss='hs', wordNgrams=2, dim=11, bucket=500)
            model.save_model(f"{file_name}")
            exist.file = file_name
            exist.save()
            return Response('model retrained and saved')
        else:
            # нету в базе
            DataForTrain.objects.create(file=file)
            from fasttext import train_supervised
            model = train_supervised(input=f"{file}", loss='hs', wordNgrams=2, dim=11, bucket=500)
            model.save_model(f"{file_name}")
            FastTextModel.objects.create(file=f"{file_name}", name=file_name)
            return Response('model saved')


class DownloadModelView(APIView):
    # вывод всех доступных загруженных моделей+ если добавить в запрос ?lang_code="code language" начнется загрузка
    # новой модели по двубукв. коду языка (коды языка, ссылка: )
    def get(self, request):
        lang_code = request.GET.get('lang_code', None)
        if lang_code:
            import fasttext.util
            try:
                fasttext.util.download_model(lang_code, if_exists='ignore')
                exist = DownloadModel.objects.filter(file=f'cc.{lang_code}.300.bin')
                if not exist:
                    DownloadModel.objects.create(file=f'cc.{lang_code}.300.bin')
            except Exception:
                return Response("Неверно введен двубуквенный код языка")
        data = DownloadModel.objects.all()
        response = []
        for obj in data:
            response.append(str(obj.file))
        return Response(response)

    # Обязательные параметры модель и сентенсе, показывает векторы для каждого слова в предложении (из параметра сент в
    # выбранной моделе)
    def post(self, request):
        try:
            model = request.data['model']
            sentence = request.data['sentence']
            print('1')
            model = DownloadModel.objects.get(file=model).file
            print(model)
            import fasttext
            ft = fasttext.load_model(str(model))
            print(ft)
            data = ft.get_sentence_vector(sentence)
        except Exception:
            return Response('Неверный запрос')
        return Response(data)


class PredictModelView(APIView):
    # вывод всех тренированных моделей
    def get(self, request):
        data = FastTextModel.objects.all()
        response = []
        for obj in data:
            response.append(str(obj.file))
        return Response(response)

    #
    def post(self, request):
        model = request.data['model']
        sentence = request.data['sentence']
        try:
            model = FastTextModel.objects.get(file=model).file
            import fasttext
            model = fasttext.load_model(str(model))
            predict = model.predict(sentence)
            return Response(predict)
        except Exception:
            return Response('Неверный запрос')