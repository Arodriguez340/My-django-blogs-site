from blogs.models import Entry

def lts_entries_processor(request):
    query_set = Entry.objects.order_by('-date_added') [:5]
    
    return {
        'lts_entries': query_set
        }