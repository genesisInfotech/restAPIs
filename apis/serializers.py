# -*- coding: utf-8 -*-

from rest_framework import serializers
from .models import Branch, Bank

class BankSerializer(serializers.ModelSerializer):
    bank = serializers.CharField(read_only=True)
    class Meta:
       model = Bank


class BranchSerializer(serializers.ModelSerializer):
    bank_name = serializers.CharField(source='bank.name', read_only=True)
    class Meta:
       model = Branch
       fields = ('id', 'ifsc', 'name', 'bank_name', 'address',
            'city', 'district', 'state')

