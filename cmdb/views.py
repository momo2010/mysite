from django.shortcuts import render
from django.shortcuts import HttpResponse
from cmdb import models



# Create your views here.
def index(request):
    # request.POST
    # request.GET
    # return HttpResponse("Hello World!")
    if request.method == "POST":
        usersname = request.POST.get("username",None)
        password = request.POST.get("password",None)
        # 添加到数据库中
        models.UserInfo.objects.create(user=usersname,pwd=password)
    user_list = models.UserInfo.objects.all();
    return render(request,"index.html",{'data':user_list})
# 分页函数
#def page(request,index):
#    page = index
#    return render(request,"page.html",{'data':page})
    # return HttpResponse("page: 第%s页" % page)

def page(request, page, number):
    p = page
    n = number
    # return HttpResponse("page: 第%s页 第%s条" %(p, n))
    return render(request,"page.html",{'page':p,'number':n})