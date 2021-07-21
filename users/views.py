import re, json, bcrypt, jwt

from django.views import View
from django.http  import JsonResponse

from users.models import User

REGEX = {
    'email'    : '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
    'password' : '^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%#?&])[A-Za-z\d@$!%*#?&]{8,16}$'
}

class SignupView(View):
    def post(self, request):
        try:
            data         = json.loads(request.body)
            email        = data['email']
            password     = data['password']
            phone_number = data['phone_number']
            name         = data['name']

            if not re.match(REGEX['email'], email) or not re.match(REGEX['password'], password):
                return JsonResponse({'error':'INVALID_ERROR'}, status=400)
            
            if User.objects.filter(email=email).exists() or User.objects.filter(phone_number=phone_number).exists():
                return JsonResponse({'message':'DUPLICATE'},status=409)
            
            encoded_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

            User.objects.create(
                email        = email,
                password     = encoded_password.decode('utf-8'),
                phone_number = phone_number,
                name         = name
            )
            return JsonResponse({'message':'SUCCESS'}, status=201)
        
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'},status=400)