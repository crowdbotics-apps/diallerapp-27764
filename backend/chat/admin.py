from django.contrib import admin
from .models import (
    ForwardedMessage,
    Message,
    ThreadMember,
    MessageAction,
    Thread,
    ThreadAction,
)

admin.site.register(MessageAction)
admin.site.register(ForwardedMessage)
admin.site.register(Message)
admin.site.register(ThreadAction)
admin.site.register(ThreadMember)
admin.site.register(Thread)

# Register your models here.
