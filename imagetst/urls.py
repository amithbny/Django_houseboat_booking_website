from django.urls import path
from .import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('house',views.houseboats,name='houseboat'),
    path('package',views.packages,name='package'),
    path('detail<int:id>',views.package_detail_pg,name='package_detail'),
    path('tariff',views.tariff,name='tariff'),
    path('register',views.regForm,name='register'),
    path('profile',views.profile,name='profile'),
    path('delete/<int:id>',views.delBooking,name='delete'),
    path('update<int:id>',views.updateProfile,name='update'),
    path('booking',views.bookingForm,name='booking'),
    path('login',views.loginPage,name='login'),
    path('logout',views.logOut,name='logout'),
    # path('review<int:id>',views.reviewForm,name='review')
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)