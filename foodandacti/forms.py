from django.forms import ModelForm
from .models import *

class SetgoalForm(ModelForm):
    class Meta:
        model=setgoals
        fields='__all__'


class ActivityForm(ModelForm):
    class Meta:
        model=activitysecdule
        fields = '__all__'
        exclude=('user',)

class UseridForm(ModelForm):
    class Meta:
        model=activitysecdule
        fields = '__all__'

#
# class ArticleForm(ModelForm):
#     class Meta: