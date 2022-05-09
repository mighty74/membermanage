from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Test, List, BList
from .forms import DiaryForm, HomeForm
from django import forms
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q

# Create your views here.

class Test(generic.ListView):
    template_name = 'memberapp/test.html'
    model = Test

class Home(generic.ListView):
    template_name = 'memberapp/home.html'
    def get_queryset(self):
        queryset = BList.objects.order_by('-id')
        queryset = queryset.filter(author = self.request.user)
        keyword = self.request.GET.get('keyword')
        if keyword:
            queryset = queryset.filter(
                Q(title__icontains=keyword)
            )
            messages.success(self.request, '「{}」の検索結果'.format(keyword))
        return queryset

def Memberlist(request, id):
    template_name = 'memberapp/memberlist.html'

    def get_queryset(request):
        queryset = List.objects.order_by('-id')
        queryset = queryset.filter(author = request.user)
        queryset = queryset.filter(listpk = id)
        keyword = request.GET.get('keyword')
        if keyword:
            queryset = queryset.filter(
                Q(name__icontains=keyword) | Q(grade__icontains=keyword) |
                Q(group__icontains=keyword) | Q(se__icontains=keyword) 
            )
            messages.success(request, '「{}」の検索結果'.format(keyword))
        return queryset
    a = get_queryset(request)
    return render(request, 'memberapp/memberlist.html', {'object_list': a, 'id': id})
    


def About(request, member_id):
    member_db = get_object_or_404(List, id=member_id)
    return render(request, 'memberapp/about.html', {'member_db': member_db})

def CreateMember(request, id):
    if request.method == 'POST':
        form = DiaryForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.listpk = id
            post.save()
            return redirect('memberlist', id = id)
    else:
        form = DiaryForm()
    return render(request, 'memberapp/create.html', {'form': form, 'id': id})
    success_url = reverse_lazy('memberlist', id = id)

def CreateList(request):
    if request.method == 'POST':
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = HomeForm()
    return render(request, 'memberapp/createlist.html', {'form': form})
    success_url = reverse_lazy('home',)

def DeleteList(request, id):
    template_name = 'memberapp/deletelist.html'
    list = get_object_or_404(BList, pk = id)
    obj = List.objects.all()
    obj = obj.filter(listpk = id)
    if request.method == 'POST':
        list.delete()
        obj.delete()
        return redirect('home')
    return render(request, template_name, {'object': list})


def DeleteMember(request, id):
    template_name = 'memberapp/delete.html'
    obj = get_object_or_404(List, pk = id)
    if request.method == 'POST':
        obj.delete()
        return redirect('memberlist', id = obj.listpk)
    return render(request, template_name, {'object': obj, 'id': obj.listpk})

def UpdateMember(request, id):
    list = get_object_or_404(List, id = id)
    if request.method == 'POST':
        form = DiaryForm(request.POST, instance = list)
        if form.is_valid():
            post = form.save()
            post.author = request.user
            post.listpk = list.listpk
            post.save()
            return redirect('memberlist', id = list.listpk)
    else:
        form = DiaryForm(initial={
            'name': list.name,
            'number': list.number,
            'grade': list.grade,
            'group': list.group,
            'se': list.se,
            'adre': list.adre,
            'content': list.content
            })
    return render(request, 'memberapp/update.html', {'form': form, 'id': list.listpk})
    success_url = reverse_lazy('memberlist', id = list.listpk)
