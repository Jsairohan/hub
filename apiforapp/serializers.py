# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from beforelogin.models import User
from healthandrecords.models import evaluation_form,Risk_sore
from foodandacti.models import Userinfosummary
from apiforapp.models import glucos,oximeter,Temperature,Bpmmeter,Weightmeter,Spirometery,pocapi,totalcholestrol,Hdlmmeter,\
    Himobloginmeter,Hbacmeter,Ldlmeter,Totalcolestrolmeter,Triglecyridesmeter,Urinemeter,Ecgmeter,EcgNIGmeter
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status
import urllib,os
from uuid import uuid4
from PIL import Image
from rest_framework import serializers
from healthandrecords.models import CheckParams
from pyPdf import PdfFileWriter, PdfFileReader
import StringIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from usermanagement.models import Patient

class UserResgistrationserializer(serializers.Serializer):
    email = serializers.EmailField()
    patient_code = serializers.IntegerField()
    name = serializers.CharField(max_length=150)

    # def create(self, validated_data):




class Patientevaluvationserializer(serializers.ModelSerializer):
    class Meta:
        model = evaluation_form
        fields = '__all__'
        exculde=("bmr","bp_systolic","bp_diastolic",)

class Patientriskserializer(serializers.ModelSerializer):
    class Meta:
        model = Risk_sore
        fields = '__all__'


class Patientuserinfoserializer(serializers.ModelSerializer):
    class Meta:
        model = Userinfosummary
        fields = '__all__'
        exculde=("name","email","PhoneNo","age","Gender","MaritalStatus","EmployedStatus","HousingStatus",)

class glucosserializer(serializers.ModelSerializer):
    class Meta:
        model = glucos
        fields = '__all__'
        exculde=("bpvalue",)
class cholestrolserializer(serializers.ModelSerializer):
    class Meta:
        model = totalcholestrol
        fields = '__all__'

class oximeterserializer(serializers.ModelSerializer):
    class Meta:
        model = oximeter
        fields = '__all__'
    # def create(self, validated_data):
    #     validated_data["spo"]=validated_data["spo2"]
    #     return oximeter(**validated_data)


class Temperatureserializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = '__all__'


class Bpmmeterserializer(serializers.ModelSerializer):
    class Meta:
        model = Bpmmeter
        fields = '__all__'



class Weightmeterserializer(serializers.ModelSerializer):
    class Meta:
        model = Weightmeter
        fields = '__all__'

class Spirometeryserializer(serializers.ModelSerializer):
    class Meta:
        model = Spirometery
        fields = '__all__'


class Hdlmmeterserializer(serializers.ModelSerializer):
    class Meta:
        model = Hdlmmeter
        fields = '__all__'
		
		
class Himobloginmeterserializer(serializers.ModelSerializer):
    class Meta:
        model = Himobloginmeter
        fields = '__all__'


class Hbacmeterserializer(serializers.ModelSerializer):
    class Meta:
        model = Hbacmeter
        fields = '__all__'



class Ldlmeterserializer(serializers.ModelSerializer):
    class Meta:
        model = Ldlmeter
        fields = '__all__'

class Totalcolestrolmeterserializer(serializers.ModelSerializer):
    class Meta:
        model = Totalcolestrolmeter
        fields = '__all__'


class Triglecyridesmeterserializer(serializers.ModelSerializer):
    class Meta:
        model = Triglecyridesmeter
        fields = '__all__'
		
		
class Urinemetermeterserializer(serializers.ModelSerializer):
    class Meta:
        model = Urinemeter
        fields = '__all__'


class ECGserializer(serializers.ModelSerializer):
    class Meta:
        model = Ecgmeter
        fields = '__all__'
        exculde=("pdf_file",)
    def create(self, validated_data):
        ecg_url = validated_data['ECG_File']
        print validated_data['ECG_File'], "ECG_File"
        loc = urllib.urlretrieve(ecg_url)
        print loc
        index_pos = (loc[0].rfind("\\")) + 1
        index_lpos = (loc[0].rfind('.'))
        print index_pos, index_lpos
        name = loc[0][index_pos:index_lpos]

        filename = loc[0] # file path
        im = Image.open(filename)
        if im.mode == "RGBA":
            im = im.convert("RGB")

        new_filename = "documents/{}.pdf".format('ECG'+str(uuid4().clock_seq_low)) # file path where you have to save
        print new_filename
        if not os.path.exists(new_filename):

            im.save(new_filename, "PDF", resolution=100.0)
        validated_data['pdf_file'] = new_filename
        return Ecgmeter.objects.create(**validated_data)


class ECGNigserializer(serializers.ModelSerializer):
    class Meta:
        model = EcgNIGmeter
        fields = '__all__'

    def create(self, validated_data):
        ecg_url = validated_data['ECG_File']
        print validated_data['ECG_File']
        loc = urllib.urlretrieve(ecg_url)

        filename = loc[0] # file path

        #im = Image.open("C:\\Users\\user\\Desktop\\1560436833.jpeg"
        im = Image.open(filename)
        if im.mode == "RGBA":
            im = im.convert("RGB")


        new_filename = "documents/ECG12lead/{}.pdf".format('ECG12'+str(uuid4().clock_seq_low)) #file path where you have to save

        print new_filename,'newfile name'

        if not os.path.exists(new_filename):
            im.save(new_filename, "PDF",resolution=100.0)
        validated_data['pdf_file'] = new_filename
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        print BASE_DIR,'hgjhsgdj'
        fil_for_canvas = os.path.join(BASE_DIR,new_filename)
        fil_for_canvas_str = str(fil_for_canvas)
        with open(fil_for_canvas_str,"r") as f:

            id = validated_data["patient_code"]
            user = Patient.objects.filter(patient_code=id).last()
            # print user.first_name
            packet = StringIO.StringIO()
            # create a new PDF with Reportlab
            can = canvas.Canvas(packet, pagesize=letter)
            can.setFont("Times-Roman", 30)
            # can.setFillColorRGB(1,0,1)
            can.setFontSize(30)
            can.drawString(30, 30, "Cygen summary 12 lead ecg")
            # can.drawRightString(2180,100,  "name:dinesh")
            can.drawCentredString(1300, 30, "{0}/{1}".format(user.pro.first_name+' '+user.pro.middle_name+' '+user.pro.last_name,user.pro.gender))
            # can.drawCentredString(3000, 2100, "patient code: AMPHL-00-0001")
            can.save()

            # move to the beginning of the StringIO buffer
            packet.seek(0)
            new_pdf = PdfFileReader(packet)
            # read your existing PDF
            existing_pdf = PdfFileReader(file(fil_for_canvas_str, "rb"))
            print existing_pdf,'hhhhhhhhhhh'
            output = PdfFileWriter()
            print output
            # add the "watermark" (which is the new pdf) on the existing page
            page = existing_pdf.getPage(0)
            page.mergePage(new_pdf.getPage(0))
            output.addPage(page)
            # finally, write "output" to a real file
            outputStream = file(fil_for_canvas_str, "ab")
            print outputStream,'hhhhhh'
            output.write(outputStream)
            outputStream.close()


        return EcgNIGmeter.objects.create(**validated_data)




class Evaluationserializer(serializers.ModelSerializer):
    class Meta:
        model = evaluation_form
        fields = '__all__'

class Checkserializer(serializers.ModelSerializer):
    class Meta:
        model = CheckParams
        fields = '__all__'
        # exculde=("bmi_param",)
class userserializer(serializers.ModelSerializer):
    class Meta:
        model =User
        fields='__all__'

