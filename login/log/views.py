import json
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password
from .models import UserModel

def user_register(request):
    data = json.loads(request.body)
    name = data.get('name')
    email = data.get('email')
    phone_no = data.get('phone_no')
    password = data.get('password')
    
    try:
        if name and email and phone_no and password:
            is_user_present = UserModel.objects.filter(email=email, phone_no=phone_no).exists()
            if not is_user_present:
                UserModel.objects.create(name=name, email=email, phone_no=phone_no, password=password)
                # send_email(name, email)
                return JsonResponse({'message': 'Registration successful!'})
            else:
                return JsonResponse({'message': 'User already present with these credentials!'}, status=403)
        else:
            return JsonResponse({'message': 'Please fill all the fields!'}, status=403)
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=400)


def user_login(request):
    data = json.loads(request.body)
    email = data.get('email')
    password = data.get('password')
    
    try:
        if email and password:
            user = UserModel.objects.filter(email=email).first()
            if user:
                if not check_password(password, user.password):
                    return JsonResponse({'message': 'Password incorrect'}, status=402)
                else:
                    # Generate token and send user details
                    # token = generate_token(user)
                    return JsonResponse({'message': 'You have been successfully logged in!', 'userDetails': user.serialize()}, status=200)
            else:
                return JsonResponse({'message': 'Your email is not registered. Please register to continue!'}, status=403)
        else:
            return JsonResponse({'message': 'Please fill all the fields!'}, status=403)
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=400)

def update_profile(request):
    data = json.loads(request.body)
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    food_to_donate = data.get('items_to_donate')

    try:
        user = request.user
        user.latitude = latitude
        user.longitude = longitude
        user.food_to_donate = food_to_donate
        user.save()
        
        return JsonResponse({'message': 'Profile updated successfully!', 'userDetails': user.serialize()})
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=400)