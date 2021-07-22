from django.views         import View
from django.http.response import JsonResponse

from products.models      import Product
from orders.models        import Bidding
from utils                import authorization

class BiddingPageView(View):
    @authorization
    def get(self, request, product_id):
        try:
            user = request.user

            if not Product.objects.filter(id=product_id).exists():
                return JsonResponse({'message': 'PRODUCT_NOT_FOUND'}, status=404)

            product = Product.objects.get(id=product_id)

            current_buying_price  = product.current_buying_price
            current_selling_price = product.current_selling_price
            
            selling_bid, buying_bid = None, None
        
            if Bidding.objects.filter(is_seller=1, product_id=product_id).exists():
                selling_bid = Bidding.objects.filter(is_seller=1, product=product).order_by('price').first()

            if Bidding.objects.filter(is_seller=0, product_id=product_id).exists():
                buying_bid = Bidding.objects.filter(is_seller=0, product=product).order_by('-price').first()


            results = {
                'product': {
                    'name'                 : product.name, 
                    'author'               : product.author.name, 
                    'image'                : product.productimage_set.first().image_url,
                    'selling_bid_id'       : selling_bid.id if selling_bid else None,
                    'buying_bid_id'        : buying_bid.id if buying_bid else None,
                    'current_buying_price' : current_buying_price,
                    'current_selling_price': current_selling_price
                    },
                'user': {
                    'name'        : user.name, 
                    'address'     : user.address, 
                    'phone_number': user.phone_number,
                    'payment': {
                        'card_company': user.card_company, 
                        'card_number' : user.card_number,
                        'bank_name'   : user.bank_name,
                        'bank_account': user.bank_account
                        }
                    }
            }

            return JsonResponse({'results': results}, status=200)
        
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)