from rest_framework import serializers
from transactions.models import Transaction


class TransactionInputSerializer(serializers.Serializer):
    user_id = serializers.CharField(max_length=100)
    origin_currency = serializers.ChoiceField(choices=Transaction.CURRENCY_CHOICES)
    origin_value = serializers.DecimalField(max_digits=14, decimal_places=2)
    destination_currency = serializers.ChoiceField(choices=Transaction.CURRENCY_CHOICES)

    def validate(self, data):
        if data["origin_currency"] == data["destination_currency"]:
            raise serializers.ValidationError(
                "Origin and destination currencies must be different."
            )
        return data


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"
