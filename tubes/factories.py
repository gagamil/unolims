import factory
from . import models


class TubeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Tube

    tube_id = factory.Sequence(lambda n: "AA%06d" % n)


class TubeBatchFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.TubeBatch

    title = factory.Faker('pystr')
