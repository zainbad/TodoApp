# from django.db.models.signals import post_save
# from django.contrib.auth.models import User

# from .models import User_Profile

# def customer_profile(sender, instance, created, **kwargs):
# 	if created:
		
# 		User_Profile.objects.create(
# 			user=instance,
# 			name=instance.username,
# 			)
# 		print('Profile created!')

# post_save.connect(customer_profile, sender=User)