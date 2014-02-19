from django.utils import timezone
from haystack import indexes
from apps.jobs.models import Job


class JobIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    submission_email = indexes.CharField(model_attr='submission_email')
    submission_closes = indexes.DateTimeField(model_attr='submission_closes')

    def get_model(self):
        return Job

    def index_queryset(self, using=None):
        now = timezone.now()
        return self.get_model().objects.filter(submission_closes__gt=now)
