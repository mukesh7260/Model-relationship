from rest_framework import serializers
from tryapp.models import *

class ProductColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductColourModel
        fields = "__all__" 


class ProductImageSerialiizer(serializers.ModelSerializer):
    class Meta:
        model = ProductImageModel
        fields = "__all__" 



class ProductMainModelSerializer(serializers.ModelSerializer):
                               
    # color = ProductColorSerializer()    # ono to one relationship model 
    # color = ProductColorSerializer(many=True)         # many to one model relationship ie forignkey modlel   
    color = serializers.SerializerMethodField()

    def get_first_name(self, obj):
        return obj.color.title()


    color = ProductColorSerializer(many=True)                                       
    image =   ProductImageSerialiizer(many=True)      
    class Meta:

        model = ProductMainModel
        fields = ['titles','description','price','unique_code','size','mainchoice','color','image']
    


