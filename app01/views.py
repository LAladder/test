from django.shortcuts import render, redirect
from django.http import HttpResponse
from app01.models import User, Press, Book, Author
import os
from django.conf import settings


# Create your views here.
def login1(request):
    # print(request.GET)
    # print('-' * 120)
    error_msg = ''
    # 需要判断
    if request.method == "POST":
        # 如果是第二次来   表示填完了 要给我发数据了           -->POST
        num = request.POST.get("num")
        pwd = request.POST.get("pwd")
        print(num, pwd)
        # if num == '123456' and pwd == '123456':
        # 从数据库查询有没有这个用户
        ret = User.objects.filter(num=num,pwd=pwd)
        if ret:
            # 登录成功
            # return redirect('http://www.xiaohuar.com')
            return redirect('/index1/')
        else:
            # 登录失败
            # 提示用户名或密码错误
            error_msg = '账号密码错误'

    # 如果你是第一次来   是跟我要一个登陆页面用来填写数据    --> GET
    return render(request, 'login1.html',{'error_msg':error_msg})


def index1(request):

    return render(request,'index1.html')


# 出版社列表处理函数
def press_list(request):

    # 去数据库查所有的出版社
    ret = Press.objects.all().order_by('id')
    print(ret)
    # print(ret[0])
    # print(ret[0].name)
    # 在页面上展示出来
    return render(request,'press_list.html',{'ret':ret})
    # return HttpResponse('ok')


# 添加出版社的处理函数
def add_press(request):
    if request.method == "POST":
        # 表示用户填写完了，要给我发数据
        # 1. 取到用户填写的出版社数据
        press_name = request.POST.get('name')
        # 2. 将数据添加到数据库中
        Press.objects.create(name = press_name)
        # 3. 挑战到出版社列表页面
        return redirect('/press_list/')
    # 返回一个添加页面，让用户在上面填写新的出版社信息
    return render(request,'add_press.html')


# 删除出版社处理函数
def delete_press(request):
    # 获取要删除的出版社ID
    delete_id = request.GET.get('id')
    print(delete_id)
    # 根据id区数据库删除对应的数据行
    Press.objects.filter(id=delete_id).delete()
    # 让用户再去访一下出版社列表
    return redirect('/press_list/')


# 编辑出版社处理函数
def edit_press(request):
    if request.method == 'POST':
        # 1.用户修改完出版社数据给我发过来
        edit_id = request.POST.get('id')
        new_name = request.POST.get('name')  # 拿到form表单提交的值
        # 2.去数据库修改对应的数据
        # 2.1 先找对应的数据
        edit_press_obj = Press.objects.get(id=edit_id)
        # 2.2 修改出版社的名称
        edit_press_obj.name = new_name    # 这一步只发生在ORM实例对象层面
        # 2.3 将修改同步到数据库
        edit_press_obj.save()
        # 3.让用户再去访问出版社列表
        return redirect('/press_list/')

    # 1.获取要编辑的出版社的id
    edit_id = request.GET.get('id')
    # 2.获取该出版社的信息
    # ret = Press.objects.filter(id=edit_id)[0]  # -->[Press obj]
    # print(ret)
    # get 就是获取一个
    ret = Press.objects.get(id=edit_id)   # --> Press obj,get()有且只能找到一个对象，否则就报错
    print(ret)
    # 3.在页面上展示出来
    # 打开edit_press.html
    # 用你传的参数去替换THML页面的特殊符号
    # 将替换后的HTML内容返回给浏览器
    return render(request,'edit_press.html',{'press_obj':ret})


# 书籍展示处理函数
def books(request):
    # 1. 查询所有的数据数据
    data = Book.objects.all()
    # 取到第一本书对象
    first_book = data[0]
    print(first_book)
    # 取到对象的title属性
    print(first_book.title)
    # 取到对象的press属性
    # 即 ORM中的foreignkey 通过外键直接取到和我这本书关联的出版社名称
    print(first_book.press)
    # 取到和我这本书关联的出版社的名字
    print(first_book.press.name)
    # 取到和我这本书关联的出版社id
    print(first_book.press_id)
    # 连表查询到出版社id
    print(first_book.press.id)
    # 2. 在页面上展示出来

    # 3. 返回完整的HTML页面
    return render(request, 'book_list.html', {'data': data})


# 添加书籍的处理函数
def add_book(request):
    if request.method == "POST":
        print(request.POST)
        # 1. 取到用户填写的数据
        book_title = request.POST.get('book_title')
        print(book_title)
        press_id = request.POST.get('press_id')
        print(press_id)
        # 2. 创建新的数据记录
        # 基于对象的创建
        # press_obj = Press.objects.get(id=press_id)
        # Book.objects.create(title=book_title,press=press_obj)
        # 基于外键id的创建
        Book.objects.create(title=book_title,press_id=press_id)
        # 3. 跳转到书籍列表页
        return redirect('/book_list/')
    # 1. 返回一个页面，让用户填写书籍信息
    # 因为书籍信息需要关联出版社
    # 所以在添加书籍页面要把存在的出版社展示出来  让用户选择
    press_data = Press.objects.all()
    return render(request,'add_book.html',{'press_list':press_data})


# 删除书籍的处理函数
def delete_book(request):
    # 1. 从url中取到要删除的书籍的id值
    delete_book_id = request.GET.get('id')
    # 2. 根据id值去数据库找到相对应的数据   删除掉
    Book.objects.filter(id=delete_book_id).delete()
    # 3. 跳转到书籍列表页面
    # redirect 实际做的事
    # 给浏览器返回一个特殊的响应（命令）
    # 这个特殊的命令就是让浏览器在发一次请求，访问我指定的url
    return render(request,'delete_success.html')

    # return redirect('/book_list/')


# 编辑书籍的处理函数
def edit_book(request):
    # 1. 从URL中获取要编辑的书籍的id值
    edit_book_id = request.GET.get('id')
    print('------------------------------------------------------')
    print(edit_book_id)
    # 2. 根据id值找到要编辑的书籍对象
    edit_book_obj = Book.objects.get(id=edit_book_id)
    print(edit_book_obj)
    if request.method == "POST":
        # 1. 取到用户修改后的书籍名称和出版社信息
        new_title = request.POST.get('book_title')
        new_press_id  = request.POST.get('press_id')
        # 3. 修改书籍相应信息
        edit_book_obj.title = new_title
        edit_book_obj.press_id = new_press_id
        # 4. 保存到数据库
        edit_book_obj.save()
        # 5. 跳转到书籍列表页
        return redirect('/book_list/')

    # 2.2 把所有的出版社查询出来
    press_data = Press.objects.all()
    # 3. 在页面上显示出当前书籍的信息，等待被编辑
    return render(
        request,
        'edit_book.html',
        {'book_obj':edit_book_obj,'press_list':press_data}
    )


# 书籍列表的处理函函数
def author_list(request):
    # 1. 去数据库查询到所有的作者
    author_data = Author.objects.all()
    for author in author_data:
        print(author)
        # 取到每个作者出版的书籍
        # print(author.books)  # 是一个ORM提供的桥梁(工具)，帮我找对应关系
        print(author.books.all())
    # 2. 在页面上展示出来
    return render(request,'author_list.html',{'author_list':author_data})


# 添加作者信息
def add_author(request):
    if request.method == "POST":
        # 1. 取到用户填写的信息
        new_author_name = request.POST.get('author_name')
        # 这个只能取到一个值
        book_ids = request.POST.get('books')
        book_ids = request.POST.getlist('books')
        # print(new_author_name)
        # print(book_ids)
        # 2. 添加到数据库中
        # 2.1 创建新的作者
        author_obj = Author.objects.create(name=new_author_name)
        # 2.2 创建作者和书的对应的关系
        author_obj.books.add(*book_ids)  # 参数是一个一个单独的值
        # author_obj.books.set(book_ids)  # 参数是书籍id值的列表
        # 3. 跳转到作者列表页
        return redirect('/author_list/')
    # 1. 返回一个页面给用户   填写作者信息
    # 2. 获取所有的书籍信息
    book_data = Book.objects.all()
    return render(request,'add_author.html',{'book_list':book_data})


# 删除作者
def delete_author(request):
    # 1. 取到要删除的作者的id
    delete_author_id = request.GET.get('id')
    print(delete_author_id)
    # 2. 同步id找到数据库  并删除
    Author.objects.filter(id=delete_author_id).delete()
    # 3. 让用户再去访问作者列表页面
    return redirect('/author_list/')


# 编辑作者的处理函数
def edit_author(request):
    # 1. 取到要编辑的作者的id值
    edit_author_id = request.GET.get('id')
    # 2. 找到要编辑的作者对象
    edit_author_obj = Author.objects.get(id=edit_author_id)
    if request.method == "POST":
        # 3. 拿到编辑之后的数据
        new_author_name = request.POST.get('author_name')
        # 作者不一定只有一本书  获取书籍信息列表
        new_book_ids = request.POST.getlist('book_ids')
        # 4. 去数据库修改
        # 4.1 修改作者表
        edit_author_obj.name = new_author_name
        edit_author_obj.save()
        # 4.2 修改作者这书的关系表   重新设置为新取得的值
        edit_author_obj.books.set(new_book_ids)
        # 5. 引导用户跳转到作者列表页面
        return redirect('/author_list/')
    # 2.2 找到所有的书籍对象
    book_data = Book.objects.all()
    print(book_data)
    # 3. 返回一个页面
    return render(request,'edit_author.html',{'author':edit_author_obj,'book_list':book_data})


# 上传文件
def upload(request):
    if request.method == "POST":
        # 1 取到用户发送的数据
        print(request.POST)
        # 文件相关  类似于字典形式
        print(request.FILES)

        file_obj = request.FILES.get('file_name')
        print(file_obj.name)
        # 判断是否存在
        file_name = file_obj.name
        if os.path.exists(os.path.join(settings.BASE_DIR,file_obj.name)):
            # 如果存在同名的文件
            name, suffix = file_name.split('.')
            name += '2'
            file_name = name + '.' + suffix
        # 从上传文件对象里  一点一点读取数据  写到本地
        # wb 以二进制写的方式打开
        with open(file_name,'wb') as f:
            # 从上传文件对象里  一点一点 读取数据
            for chunk in file_obj.chunks():
                f.write(chunk)
    # 第一次GET请求来  应该给用户返回一个页面  让用户选择文件
    return render(request,'upload.html')