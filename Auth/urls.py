from django.contrib import admin
from django.urls import path, include

import accounts

urlpatterns = [
    # path('admin/', admin.site.urls),

    path('accounts/', include('accounts.urls')),
]
