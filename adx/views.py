from Person.models import PersonInformation
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'adx/login.html'
#    context_object_name = 'latest_person_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return []
