import os
from django.conf import settings

#request.GET.get(key, defaultvalue)同样
def getordefault(request, varname, default):
    if request.GET.get(varname):
        return request.GET.get(varname)
    else:
        return default


filenames = os.listdir(os.path.join(settings.BASE_DIR, "SoraApi/API"))
namelist = []
for i in filenames:
    if i.endswith(".py"):
        namelist.append(os.path.splitext(i)[0])
__all__ = namelist
