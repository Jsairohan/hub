from rest_framework.utils import html, model_meta, representation
from .models import *



def get_querystring_params(data,info):
    dic={}
    # info.pk
    for attr, value in data.items():
        if attr == 'email':
            ik = str(info.pk).split('.')
            key = ik[2] + '__' + attr
            dic[key] =data.get(attr, None)
        if attr != 'email':
            for i in info.relations:
                if info.relations[i].to_many != False:
                    continue
                model = info.relations[i].related_model
                # inforel =model._meta.get_fields()
                inforel = model_meta.get_field_info(model)
                if attr in inforel.fields :
                    attr = str(i)+'__'+str(attr)
                    dic[attr]=value

            if attr in info.fields:
                dic[attr] = value
    print dic
    return dic
