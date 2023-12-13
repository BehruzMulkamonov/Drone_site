from spravchnik.models import Brand
from rest_framework import  serializers


# class BrandSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Brand
#         fields = '__all__'
class BrandSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField(max_length = 100)

    def create(self, validated_data):

        return Brand.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.name =  validated_data.get('name', instance.name)
        instance.save()
        return instance

        