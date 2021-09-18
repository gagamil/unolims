import factory
from tubes import models


class TubeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Tube

    tube_id = factory.Sequence(lambda n: "EXT%06d" % n)


class InternalTubeFactory(TubeFactory):
    tube_id = factory.Sequence(lambda n: "INXX%06d" % n)


class TubeBatchFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.TubeBatch

    title = factory.Faker('pystr')
