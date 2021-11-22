from rest_framework import serializers
from .models import FastTextModel, DownloadModel, DataForTrain


class TrainModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = FastTextModel
        fields = ('file', )


class ShowModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = FastTextModel
        fields = ('name', )

class DownloadedModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = DownloadModel
        fields = ('file', )

class DataModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataForTrain
        fields = ('__all__', )