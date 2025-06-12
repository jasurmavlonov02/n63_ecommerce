from django.db.models.signals import pre_save,post_save,pre_delete,post_delete
from uuid import uuid4
from django.dispatch import receiver
from .models import Product

@receiver(post_save,sender=Product)
def send_message_after_save(sender,instance,created,**kwargs):
    if created:
        instance.code = str(uuid4())
        instance.save()
        print('*****************')
        print(f'{instance.name} is  successfull created')
        print('****************')

    if created is False:
        pass # updated logic
    
    

