from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserData
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


def index(request):
    return render(request, "auction_app/index.html")


def contact(request):
    return render(request, "auction_app/contact.html")


class LoginApi(APIView):

    def post(self, request):
        data = request.data
        print("data is : ", data)
        username = data.get("username", "")
        password = data.get("password", "")
        user = authenticate(username=username, password=password)
        if user:
            print("user authenticated")
            data = {"user_id": user.id, "username": user.username, "user_type": user.user_type}
            return Response({"result": 1, "msg": "User authenticated!", "user_data": data})
        else:
            print("user credential doesn't exists")
            return Response({"result": 0, "msg": "Please check your credentials!"})


class RegistrationApi(APIView):
    def post(self, request):
        data = request.data
        print("data : ", data)
        username = data.get("username", "")
        first_name = data.get("firstname", "")
        last_name = data.get("lastname", "")
        email_address = data.get("email", "")
        password = data.get("password", "")
        mobile = data.get("mobile", "")
        telephone = data.get("telephone", "")
        company_name = data.get("company", "")
        address = data.get("address", "")
        city = data.get("city", "")
        state = data.get("state", "")
        country = data.get("country", "")
        postal_code = data.get("postal", "")
        user_type = data.get("user_type", "")
        user = UserData.objects.filter(username=username)
        if user.exists():
            return Response({"result": 0, "msg": "User Already Exists."
                                                 "Try again with different username."})
        else:
            user_data = UserData.objects.create(user_type=user_type, first_name=first_name, last_name=last_name,
                                    email=email_address, username=username,
                                    password=password, mobile_number=mobile, telephone=telephone,
                                    company_name=company_name, address=address, city=city,
                                    state=state, country=country, postal_code=postal_code)
            user = UserData.objects.last()
            pwd = user.password
            user.set_password(pwd)
            user.save()
            return Response({"result": 1, "msg": "Registration Completed. Try Login!"})


def vendor_page(request):
    print("request : ", request)
    return render(request, 'auction_app/vendor.html')


def bidder_page(request):
    print("request : ", request)
    return render(request, 'auction_app/bidder.html')
