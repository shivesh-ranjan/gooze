from django.db import models
from App.util import unique_slug_generator


from django.db.models.signals import pre_save
from django.dispatch import receiver
# Create your models here.
class BlogPost(models.Model):
    slug = models.SlugField(max_length = 250, null = True, blank = True)
    title = models.CharField(max_length = 250)
    text = models.TextField()
    published_at = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ('-published_at', )
    
    def __str__(self):
        return self.title

@receiver(pre_save, sender=BlogPost)
def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
	    instance.slug = unique_slug_generator(instance)
