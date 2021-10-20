from serializers.serializer import Serializer


class JsonSerializer(Serializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def serialize(self, obj):
        return dict(obj.fields)
