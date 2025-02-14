from django.contrib import admin
from .models import Apply, Contact, Subscribe, Scripts, Sessions, Broadcasts, Syllabus, Trainer




admin.site.site_header = "Data Science Academy Admin Panel"
admin.site.site_title = "DSA"
admin.site.index_title = "Xos Geldiniz!"
admin.site.register(Apply)
admin.site.register(Contact)
admin.site.register(Subscribe)
admin.site.register(Scripts)
admin.site.register(Sessions)
admin.site.register(Broadcasts)
admin.site.register(Syllabus)
admin.site.register(Trainer)