from rest_framework import serializers
from .models import OurTeam,Rezident,Space,Faq, Blog,Jihoz


class JihozSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jihoz
        fields = [
            'id',
            'total_uz',
            'total_en',
            'total_ru',
            'image'
        ]

class SpaceSerializer(serializers.ModelSerializer):
    jihozlar = JihozSerializer(many=True)
    class Meta:
        model = Space
        fields = [
            'id', 
            'space_uz', 
            'space_en', 
            'space_ru', 
            'page_slug', 
            'image',
            'jihozlar']


class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = [
            'id', 
            'title_uz', 
            'title_en', 
            'title_ru', 
            'text_uz', 
            'text_en', 
            'text_ru'
            ]
    
    def create(self, validated_data):
        return Faq.objects.create(**validated_data)

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = [
            'id',
            'image_cover',
            'date',
            'title_uz',
            'title_en',
            'title_ru',
            'page_slug',
            'main_title_uz',
            'main_title_en',
            'main_title_ru',
            'text_first_uz',
            'text_first_en',
            'text_first_ru',
            'text_second_uz',
            'text_second_en',
            'text_second_ru',
            'image_first',
            'image_second'
        ]
    
    def create(self, validated_data):
        return Blog.objects.create(**validated_data)

class OurTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurTeam
        fields = [
            'id',
            'name_uz',
            'name_en',
            'name_ru',
            'image',
            'job_uz',
            'job_en',
            'job_ru',
            'description_uz',
            'description_en',
            'description_ru',
        ]

    def create(self, validated_data):
        return OurTeam.objects.create(**validated_data)

class RezidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rezident
        fields = [
            'id',
            'name_uz',
            'name_en',
            'name_ru',
            'job_uz',
            'job_en',
            'job_ru',
            'description_uz',
            'description_en',
            'description_ru',
        ]

    def create(self, validated_data):
        return Rezident.objects.create(**validated_data)






