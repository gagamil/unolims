import factory
from tubes import models


class TubeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Tube

    barcode = factory.Sequence(lambda n: "EXT%06d" % n)


class InternalTubeFactory(TubeFactory):
    barcode = factory.Sequence(lambda n: "INXX%06d" % n)


class TubeBatchFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.TubeBatch

    title = factory.Faker('pystr')
