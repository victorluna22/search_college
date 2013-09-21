# -*- coding: utf-8 -*-
from datetime import date
from django import forms
from django.forms.extras.widgets import Select
from models import Relatorio

YEAR_CHOICES = (('', 'Selecione'), ('2005', '2005'), ('2006', '2006'), ('2007', '2007'), ('2008', '2008'),
                ('2009', '2009'), ('2010', '2010'), ('2011', '2011'), ('2012', '2012'),
                ('2013', '2013'))

class RelatorioForm(forms.ModelForm):
    nome = forms.CharField(max_length=255,
                        widget=forms.TextInput(attrs={
                                            'class':'span6',
                                            'placeholder': 'Ex. Seu Nome'}))
    email = forms.EmailField(label=u'E-mail',
                        widget=forms.TextInput(attrs={
                                            'class':'span6',
                                            'placeholder': 'Ex. test@exemplo.com'}))
    universidade = forms.CharField(max_length=255,
                        widget=forms.TextInput(attrs={
                                            'class':'span6',
                                            'placeholder': 'Ex. UFPE'}))
    de = forms.ChoiceField(widget=Select, choices=YEAR_CHOICES)
    ate = forms.ChoiceField(widget=Select, choices=YEAR_CHOICES)

    class Meta:
        model = Relatorio
        exclude = ['status_crowler', 'status_busca', 'status_email']

    # def save(self, commit=True):
    #     return super(RelatorioForm, self).save(commit=commit)


