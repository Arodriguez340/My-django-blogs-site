from blogs.models import Entry

def lts_entries_processor(request):
    try:
        query_set = lts_entries = Entry.objects.order_by('-date_added') [:10]
        return {
            'lts_entries': query_set
        }
    except ObjectDoesNotExist:
        return None