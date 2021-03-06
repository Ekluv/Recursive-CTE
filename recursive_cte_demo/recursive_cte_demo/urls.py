"""recursive_cte_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from company import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^get-subtree/(?P<employee_id>[\w-]+)/?', views.EmployeeSubtreeApiView.as_view(), name='get_subtree'),
    url(r'^update-parent/(?P<employee_id>[\w-]+)/?', views.EmployeeSubtreeApiView.as_view(), name='update_subtree'),
    url(r'^get-ancestor-tree/(?P<employee_id>[\w-]+)/?', views.EmployeeAncestorTreeApiView.as_view(), name='get_ancestor'),
    url(r'^all/?', views.EmployeeListSubtree.as_view(), name='get_subtree'),
]
