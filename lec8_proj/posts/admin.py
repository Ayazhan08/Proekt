from django.contrib import admin

# Register your models here.
from .models import Posts
admin.site.register(Posts)

from .models import Categories
admin.site.register(Categories)

from .models import Labs
admin.site.register(Labs)

from .models import Mids
admin.site.register(Mids)

from .models import Registration
admin.site.register(Registration)