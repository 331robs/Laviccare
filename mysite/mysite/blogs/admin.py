from django.contrib import admin

# Register your models here.
from .models import Post


admin.site.site_header="Laviccare Admin"
#admin.site.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','status','created_on','cover','image_title')
    list_filter = ["status"]
    search_fields = ['title','content']
    prepopulated_fields={'slug':('title',)}

admin.site.register(Post,PostAdmin)

