from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [                                                                     
             path('web_page6/', views.web_page6),
path('web_page1/', views.web_page1),
 path('web_page2/', views.web_page2),
                                
path('user_content/',views.news ),

path('web_page3/', views.web_page3),

path('web_page4/', views.web_page4),
path('web_page5/', views.web_page5),                  
 path('show_content/', views.show_news),
path('learn/', views.learn),
 path('show_news/', views.show_news),
 path('page0/', views.page0, name='page0'),
                                path('page2/', views.page2, name='page2'),

                path('page3/', views.page3, name='page3'),
                path('page4/', views.page4, name='page4'),

                path('page5/', views.page5, name='page5'),
 path('home/', views.home, name='home'),
            path('books/',views.books, name='books' ),

    path('books/add/', views.add_book, name='add_book'),
    path('books/show/', views.show_books, name='show_books'),
    path('purchase/<int:book_id>/', views.purchase_book, name='purchase_book'),
    path('purchase/details/', views.show_purchase_details, name='show_purchase_details'),
    path('purchased/', views.show_purchased_books, name='show_purchased_books'),
    # path('', views.register, name='register'),
    # path('accounts/login/', views.user_login, name='login'),
    path('books/purchase/details/all/', views.show_all_purchase_details, name='show_all_purchase_details'),
path('purchase/detail/<int:purchase_detail_id>/delete/', views.delete_purchase_detail, name='delete_purchase_detail'),
 path('admi/login/', views.admin_login, name='admin_login'),
path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
                path('admin_learn/', views.admin_learn, name='admin_learn'),

 ]


from django.conf import settings
from django.conf.urls.static import static



# # # Add the following line to serve media files in development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Add the following line to serve media files in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)