from django.urls  import path

from orders.views import BiddingPageView

urlpatterns = [
    path('/<int:product_id>', BiddingPageView.as_view()),
]