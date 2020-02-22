from django.shortcuts import render
from django.shortcuts import redirect
from. import models


def index(req):
    Goods = models.GoodsInfo.objects.all()
    if req.session.get('is_login', False):
        user = models.user.objects.get(userName=req.session['user_name'])
        return render(req, 'Home/index.html', {"goods": Goods, 'user': user})

    if req.method == "POST":
        username = req.POST.get('username', None)
        password = req.POST.get('password', None)
        message = '用户名和密码不能为空'
        if username and password:
            try:
                user = models.user.objects.get(userName=username)
                if user.password == password:
                    req.session['is_login'] = True
                    req.session['user_id'] = user.userID
                    req.session['user_name'] = user.userName
                    return render(req, 'Home/index.html', {'goods': Goods, 'user': user})
                else:
                    message = '密码错误！'
            except:
                message = '此用户不存在！'
            return render(req, 'Home/index.html', {'goods': Goods, 'message': message})
        return render(req, 'Home/index.html', {'Goods': Goods, 'message': message})
    else:
        return render(req, 'Home/index.html', {"goods": Goods})


def HotGoods(req):
    Goods=models.GoodsInfo.objects.all()
    goods=[]
    length=len(Goods)-1
    for i in range(0,12):
        goods.append(Goods[length])
        length=length-1
    return render(req, 'Home/HotGoods.html',{'goods':goods})


def notice(req):
    notices = models.notice.objects.all()
    return render(req, 'Home/notice.html',{'notices': notices})


def comment(req):
    if req.method =='POST':
        content=req.POST.get('text')
        title='用户评论'
        id=req.session['user_id']
        userID=models.user.objects.get(pk=id)
        models.message.objects.create(title=title,content=content,userID=userID)
    messages = models.message.objects.all()
    return render(req, 'Home/comment.html', {'messages':messages})


def register(req):
    userName = req.POST.get('username')
    name = req.POST.get('name')
    password = req.POST.get('password')
    avatar = req.POST.get('avatar')
    sex = req.POST.get('gender')
    phone = req.POST.get('phone')
    email = req.POST.get('email')
    address = req.POST.get('address')
    models.user.objects.create(userName=userName, avatar=avatar, name=name,
                               sex=sex, password=password, phone=phone, email=email, address=address)
    return render(req, 'Home/register.html')


def goods(req, goodsID):
    goods = models.GoodsInfo.objects.get(pk=goodsID)
    return render(req, 'Home/goods.html', {'goods': goods})


def cart(req):
    if req.method == "POST":
        goodsID = req.POST.get('goodsID')
        goods = models.GoodsInfo.objects.get(pk=goodsID)
        req.session['goodspage'] = req.META.get('HTTP_REFERER', '/')
        count = int(req.POST.get('count'))
        totlePrice = req.session.get('totlePrice', None)
        if not totlePrice:
            req.session['totlePrice'] = count*goods.price
        else:
            totlePrice += count*goods.price
            req.session['totlePrice'] = totlePrice
        item = {'goodsID': goodsID, 'name': goods.name,
                'photo': goods.photo, 'price': goods.price, 'quantity': count}
        cart = req.session.get("cart", None)
        if not cart:
            cart = []
            cart.append(item)
            req.session['cart'] = cart
        else:
            for i in cart:
                if i['goodsID'] == goodsID:
                    i['quantity'] += count
                    return redirect(req.session['goodspage'])
            cart.append(item)
        return redirect(req.session['goodspage'])
    else:
        cart = req.session.get("cart", None)
        totlePrice = req.session.get('totlePrice', None)
        if not cart:
            return render(req, 'Home/cart.html')
        return render(req, 'Home/cart.html', {'cart': cart, 'totlePrice': totlePrice})


def logOut(req):
    req.session['is_login'] = False
    req.session['index'] = req.META.get('HTTP_REFERER', '/')
    return redirect(req.session['index'])

def buy(req):
    cart=req.session.get('cart',None)
    userID=req.session.get('user_id',None)
    totlePrice=req.session.get('totlePrice',None)
    is_login=req.session.get('is_login',False)
    if is_login:
        user=models.user.objects.get(pk=userID)
        return render(req,"Home/buy.html",{'cart':cart,'user':user,'totlePrice':totlePrice})
    else:
        message='请先返回首页登录'
        return render(req,'Home/buy.html',{'message':message})

def search(req):
    bra = req.POST.get('Search')
    brand=models.brand.objects.get(name=bra)
    goods = models.GoodsInfo.objects.filter(brand=brand.brandID)
    return render(req,'Home/search.html',{'goods':goods,'bra':bra})
        