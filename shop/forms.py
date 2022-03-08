from django import forms
from PIL import Image
from shop.models import Product

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'image'
        ]

    
    def clean_image(self):
        image = self.cleaned_data['image']
        output_size = (210, 380)
        if any(dim > 360 for dim in image.image.size):
            i = Image.open(image.file)
            fmt = i.format.lower()
            i.thumbnail(output_size)

            image.file = type(image.file)()
            i.save(image.file, fmt)
        
        return image