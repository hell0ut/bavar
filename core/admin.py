from django.contrib import admin
from .models import *
from django import forms

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Image)


class ItemAdminForm(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = Item
        fields = '__all__'

    def save(self, commit=True):
        item = super(ItemAdminForm, self).save(commit=False)

        print(type(self.cleaned_data['image']))
        i = Image(image=self.cleaned_data['image'], item=item)
        i.save()
        if commit:
            item.save()

        return item


class ItemAdmin(admin.ModelAdmin):

    form = ItemAdminForm


admin.site.register(Item, ItemAdmin)





