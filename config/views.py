from django.shortcuts import render, redirect, reverse  
from django.views import View  

class index(View):
    def get(self, request, *args, **kwargs):
        return redirect(reverse('club_management:top_page'))


index_toppage = index.as_view()
