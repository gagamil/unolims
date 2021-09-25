import django.dispatch

# business logic signals [START]

batch_pending_confirmation = django.dispatch.Signal()
batch_just_confirmed = django.dispatch.Signal()

# business logic signals [END]