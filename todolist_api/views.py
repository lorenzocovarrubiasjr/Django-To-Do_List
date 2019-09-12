from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import date
from todolist_api.models import TodoItem, TodoList
import os
import json

def re(request):
    if request.method == "POST":
        post_dict = request.POST.dict()
        print(post_dict)
        choice = post_dict['choice']
        list_id = post_dict['list_id']
        print("THIS IS YOUR LIST ID:    ",list_id)
        if str(choice) == "1":
            return redirect('/todolist/' + str(list_id) + '/incomplete', permanent=True)
        elif str(choice) == "2":
            return redirect('/todolist/' + str(list_id) + '/complete', permanent=True)
        elif str(choice) == "3":
            return redirect('/todolist/' + str(list_id), permanent=True)
        elif str(choice) == "4":
            pass
        elif str(choice) == "5":
            pass
        else:
            pass

def index(request):
    return render(request, 'todolist/home.html')

def welcome(request):
    if request.method == "POST":
        post_dict = request.POST.dict()
        loaded_id = post_dict['list_id']
        loaded_list = TodoList.objects.get(id=loaded_id)
        t = date.today()
        day = date.strftime(t, '%d')
        month = date.strftime(t, '%b')
        year = t.year
        title = "Your To Do List for %s %s %s" % (month, day, year)
        context = {}
        context["title"] = title
        context["list"] = loaded_list
        return render(request, 'todolist/welcome.html', context)    
    else:
        return JsonResponse({"Error": "You didn't make it!"})

def about(request):
    return HttpResponse("This calculator is currently under development")

def all_todolists(request):
    lists = TodoList.objects.all()
    data = list(lists.values())
    print(data)
    return JsonResponse({"lists: ": data})

def find_list_by_id(request, id):
    list_id = str(id)
    loaded_list = TodoList.objects.get(id=list_id)
    loaded_list_items = loaded_list.todoitem_set.only('done','content')
    context = {}
    context["list"] = loaded_list
    context["items"] = [item for item in loaded_list_items]
    return render(request, 'todolist/list.html', context)

def incomplete_items(request, id):
    list_id = str(id)
    loaded_list = TodoList.objects.get(id=list_id)
    items = loaded_list.todoitem_set.only('done','content').filter(done=False)
    items_list = [item for item in items]
    context = {}
    context['items'] = items_list
    return render(request, 'todolist/incomplete_items.html', context)

def complete_items(request, id):
    list_id = str(id)
    loaded_list = TodoList.objects.get(id=list_id)
    items = loaded_list.todoitem_set.only('done','content').filter(done=True)
    items_list = [item for item in items]
    context = {}
    context['items'] = items_list
    return render(request, 'todolist/complete_items.html', context)



@csrf_exempt
def new_todolist(request):
    #try:
    list_name = request.POST["list_name"]
    list_desc = request.POST["list_desc"]
    new_list = TodoList(name=list_name, description=list_desc)
    new_list.save()
    return JsonResponse({"New Lists: ": new_list.to_d()})
    #except:
     #   return JsonResponse({"error": "You need to POST a list with name and description to use this API endpoint."}) 
    


@csrf_exempt
def add_item(request, id):
    list_id = str(id)
    loaded_list = TodoList.objects.get(id=list_id)
    item_content = request.POST['content']
    item_done = request.POST['done']
    new_item = TodoItem(todo_list=loaded_list, content= item_content, done = item_done)
    new_item.save()
    return JsonResponse({"Added Item": (new_item.to_d()["content"], new_item.to_d()['done']), "To List": loaded_list.to_d()})

def all_todoitems(request):
    lists = TodoItem.objects.all()
    data = list(lists.values())
    print(data)
    return JsonResponse({"lists: ": data})

@csrf_exempt
def toggle_item(request, id):
    item_id = str(id)
    loaded_item = TodoItem.objects.get(id=item_id)
    print("LOADED ITEEEEEM:        ",loaded_item)
    print("LOADED ITEM WITH TO D:      ",loaded_item.to_d())
    if loaded_item.done == False:
        loaded_item.done = True
        loaded_item.save()
    elif loaded_item.done == True:
        loaded_item.done = False
        loaded_item.save()
    return JsonResponse({"Item": (loaded_item.to_d()["content"], loaded_item.to_d()['done'])})

#/3
def all_items(request):
    items = TodoItem.all()
    print(items)
    item_array_for_string = []
    for item in items:
        arg = "Title: " + item.title
        item_array_for_string.append(arg)
    return HttpResponse("""<h3>All Items</h3> 
                        <ul>
                            <li> %s </li>
                        </ul>""" %item_array_for_string )
    

def create_item(request):
    return HttpResponse("<h3>Create a New Item</h3>")

def delete_item(request):
    return HttpResponse("<h3>Delete Item</h3>")

def quit(request):
    return HttpResponse("<h3>Quit</h3>")
# Create your views here.
