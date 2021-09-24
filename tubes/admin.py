from django.contrib import admin

from  .models import Tube, TubeBatch, TubeBatchPosition

admin.site.register(Tube)
admin.site.register(TubeBatch)
admin.site.register(TubeBatchPosition)