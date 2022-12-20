from django.db import models


class ProductMainModel(models.Model):
    choice = (('10','10'),('20','20'),('30','30'))
    quality = (('low','low'),('high','hgih'),('medium','medium'))
    titles = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    unique_code = models.IntegerField()
    size = models.CharField(max_length = 200, choices=choice)
    mainchoice = models.CharField(max_length = 100,choices=quality) 

# class ProductColourModel(models.Model):
#     product = models.OneToOneField(ProductMainModel,on_delete=models.CASCADE,related_name='color')
#     color_choice = (('red','red'),('green','green'),('blue','blue'),('black','black'))
#     chice_color = models.CharField(max_length = 200, choices=color_choice)
    

# class ProductColourModel(models.Model):
#     product = models.ForeignKey(ProductMainModel,on_delete=models.CASCADE,related_name='color')
#     color_choice = (('red','red'),('green','green'),('blue','blue'),('black','black'))
#     chice_color = models.CharField(max_length = 200, choices=color_choice)


class ProductColourModel(models.Model):
    product = models.ManyToManyField(ProductMainModel,related_name='color')
    color_choice = (('red','red'),('green','green'),('blue','blue'),('black','black'))
    chice_color = models.CharField(max_length = 200, choices=color_choice)

class ProductImageModel(models.Model):
    product = models.ForeignKey(ProductMainModel,on_delete=models.CASCADE,related_name='image')
    image = models.ImageField()
