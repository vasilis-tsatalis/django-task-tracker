from django.contrib import admin
from todo_app.models import ToDoItem, ToDoList

# Register your models here.

admin.site.register(ToDoItem)
admin.site.register(ToDoList)


# Add Custom labels
admin.site.site_header = 'Administrator Portal'          # default: "Django Administration"
admin.site.index_title = 'Features area'                 # default: "Site administration"
admin.site.site_title = 'Admin Framework'                # default: "Django site admin"
