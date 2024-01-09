from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ec/', views.ec, name='ec'),
    path('ec/ecaiis/', views.ecaiis, name='ecaiis'),
    path('ec/eccvr/', views.eccvr, name='eccvr'),
    path('molding/', views.molding, name='molding'),
    path('pyscript_test/', views.pyscript_test, name='pyscript_test'),
    path('pyscript_test/display/', views.display, name='display'),
    path('pyscript_test/py_repl/', views.py_repl, name='py_repl'),
    path('pyscript_test/element/', views.element, name='element'),
    path('pyscript_test/get_event/', views.get_event, name='get_event'),
    path('pyscript_test/split_module/', views.split_module, name='split_module'),
    path('post/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<int:pk>/remove/',views.post_remove, name='post_remove'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('javascript_test/', views.javascript_test, name='javascript_test'),
    path('javascript_test/tutorial/', views.tutorial, name='tutorial'),
    path('javascript_test/number_guess/', views.number_guess, name='number_guess')
    ]