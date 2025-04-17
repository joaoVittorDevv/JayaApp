from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import Transaction
from .serializers import TransactionInputSerializer, TransactionSerializer
from .utils import get_conversion_rate
from django.shortcuts import get_object_or_404
from jayaapp.users.models import User
from decimal import Decimal


class CurrencyConversionView(APIView):
    """
    Endpoint to handle currency conversion.
    Expected JSON input:
    {
        "user_id": "123",
        "origin_currency": "BRL",
        "origin_value": 100,
        "destination_currency": "USD"
    }
    """

    def post(self, request):

        input_serializer = TransactionInputSerializer(data=request.data)
        if input_serializer.is_valid():
            validated_data = input_serializer.validated_data
            user_id = validated_data["user_id"]
            origin_currency = validated_data["origin_currency"]
            origin_value = validated_data["origin_value"]
            destination_currency = validated_data["destination_currency"]

            try:

                conversion_rate = get_conversion_rate(
                    origin_currency, destination_currency
                )

            except Exception as e:
                return Response(
                    {"error": f"Failed to retrieve conversion rate with error: {e}"},
                    status=status.HTTP_503_SERVICE_UNAVAILABLE,
                )

            destination_value = origin_value * Decimal(str(conversion_rate))

            user = get_object_or_404(User, pk=user_id)

            transaction = Transaction.objects.create(
                user=user,
                origin_currency=origin_currency,
                origin_value=origin_value,
                destination_currency=destination_currency,
                conversion_rate=conversion_rate,
                destination_value=destination_value,
            )

            output_serializer = TransactionSerializer(transaction)
            return Response(output_serializer.data, status=status.HTTP_201_CREATED)

        return Response(input_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TransactionListView(generics.ListAPIView):
    """
    Endpoint to list all transactions for a given user.
    """

    serializer_class = TransactionSerializer

    def get_queryset(self):
        token_obj = get_object_or_404(Token, key=self.request.auth.key)

        user = get_object_or_404(User, pk=token_obj.user_id)

        if user:
            return Transaction.objects.filter(user_id=user)
        return Transaction.objects.none()
