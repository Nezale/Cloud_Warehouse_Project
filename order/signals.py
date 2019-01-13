import django.dispatch

orderOrdered = django.dispatch.Signal(providing_args=["meal", "component"])
