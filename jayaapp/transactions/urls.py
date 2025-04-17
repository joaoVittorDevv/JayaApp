from django.urls import path
from .views import CurrencyConversionView, TransactionListView

app_name = "transactions"

urlpatterns = [
    path("conversion/", CurrencyConversionView.as_view(), name="conversion"),
    path("list/", TransactionListView.as_view(), name="list"),
]
