from django.shortcuts import render, get_object_or_404
from yaml import serialize
from .models import Recitations, Reader
from .serializers import ReaderSerializer, RecitationsSerializer
import csv
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class ReaderList(generics.ListAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer

class ReaderDetail(generics.RetrieveAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer


# class RecitationsList(generics.ListAPIView):
#     queryset = Recitations.objects.all()
#     serializer_class = RecitationsSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['reader']


# class RecitationsDetail(generics.RetrieveAPIView):
#     queryset = Recitations.objects.all()
#     serializer_class = RecitationsSerializer




# def reader_name(request):
#     queryset = Reader.objects.all()

#     if queryset.exists() == False:
#         Reader.objects.bulk_create(
#             [
#                 Reader(name='Abdullah Awad al-Juhani'), 
#                 Reader(name='Abdullah Basfar'), 
#                 Reader(name='Abdur-Rahman as-Sudais'), 
#                 Reader(name='Ali Abdur-Rahman al-Huthaify'), 
#                 Reader(name='AbdulMuhsin al-Qasim'), 
#                 Reader(name='AbdulBari ath-Thubaity'), 
#                 Reader(name='Ahmed ibn Ali al-Ajmy'), 
#                 Reader(name='AbdulAzeez al-Ahmad'), 
#                 Reader(name='AbdulBaset AbdulSamad [Murattal]'), 
#                 Reader(name='AbdulWadud Haneef'), 
#                 Reader(name='Aziz Alili'), 
#                 Reader(name='AbdulBaset AbdulSamad [Mujawwad]'), 
#                 Reader(name="Al-Hussayni Al-'Azazy (with Children)"), 
#                 Reader(name='Abdur-Razaq bin Abtan al-Dulaimi [Mujawwad]'), 
#                 Reader(name='Abdullah Khayat'), 
#                 Reader(name='Adel Kalbani'), 
#                 Reader(name='AbdulKareem Al Hazmi'), 
#                 Reader(name="Abdul-Mun'im Abdul-Mubdi'"), 
#                 Reader(name='Abdur-Rashid Sufi'), 
#                 Reader(name='Ahmad al-Huthaify'), 
#                 Reader(name='Abu Bakr al-Shatri [Taraweeh]'), 
#                 Reader(name='Abdullah Matroud'), 
#                 Reader(name='AbdulWadood Haneef'), 
#                 Reader(name='Ahmad Nauina'), 
#                 Reader(name='Akram Al-Alaqmi'), 
#                 Reader(name='Ali Hajjaj Alsouasi'), 
#                 Reader(name='Asim Abdul Aleem'), 
#                 Reader(name='Abdallah Abdal'), 
#                 Reader(name='Abdullah Ali Jabir'), 
#                 Reader(name='Bandar Baleela'), 
#                 Reader(name='Dr. Shawqy Hamed [Murattal]'), 
#                 Reader(name='Fares Abbad'), 
#                 Reader(name='Fatih Seferagic'), 
#                 Reader(name='Hani ar-Rifai'), 
#                 Reader(name='Hamad Sinan'), 
#                 Reader(name='Hatem Farid'), 
#                 Reader(name='Ibrahim Al-Jibrin'), 
#                 Reader(name='Imad Zuhair Hafez'), 
#                 Reader(name='Ibrahim Al Akhdar'), 
#                 Reader(name='Idrees Abkar'), 
#                 Reader(name='Khalid al-Qahtani'), 
#                 Reader(name='Khalid Al Ghamdi'), 
#                 Reader(name='Khalifah Taniji'), 
#                 Reader(name='Mishari Rashid al-`Afasy'), 
#                 Reader(name='Muhammad Siddiq al-Minshawi'), 
#                 Reader(name='Muhammad Jibreel'), 
#                 Reader(name='Muhammad al-Mehysni'), 
#                 Reader(name='Muhammad Siddiq al-Minshawi [Mujawwad]'), 
#                 Reader(name='Muhammad al-Luhaidan'), 
#                 Reader(name='Muhammad Abdul-Kareem'), 
#                 Reader(name='Mustafa al-`Azawi'), 
#                 Reader(name='Muhammad Hassan'), 
#                 Reader(name='Mostafa Ismaeel'), 
#                 Reader(name='Muhammad Sulaiman Patel'), 
#                 Reader(name='Mohammad Al-Tablawi'), 
#                 Reader(name='Mohammad Ismaeel Al-Muqaddim'), 
#                 Reader(name='Muhammad Ayyoob [Taraweeh]'), 
#                 Reader(name='Masjid Quba Taraweeh 1434'), 
#                 Reader(name='Muhammad Khaleel'), 
#                 Reader(name='Mahmoud Khaleel Al-Husary'), 
#                 Reader(name='Mahmood Ali Al-Bana'), 
#                 Reader(name='Maher al-Muaiqly'), 
#                 Reader(name='Nabil ar-Rifai'), 
#                 Reader(name='Nasser Al Qatami'), 
#                 Reader(name='Sa`ud ash-Shuraym'), 
#                 Reader(name='Saad al-Ghamdi'), 
#                 Reader(name='Sahl Yasin'), 
#                 Reader(name='Salah Bukhatir'), 
#                 Reader(name='Sudais and Shuraym'), 
#                 Reader(name='Saleh al Taleb'), 
#                 Reader(name='Salah al-Budair'), 
#                 Reader(name='Sadaqat `Ali'), 
#                 Reader(name='Salah Al-Hashim'), 
#                 Reader(name="Tawfeeq ibn Sa`id as-Sawa'igh"), 
#                 Reader(name='Wadee Hammadi Al Yamani'), 
#                 Reader(name='Yasser ad-Dussary'),
#             ]
#             )
#     return render(request, template_name='quran.html')