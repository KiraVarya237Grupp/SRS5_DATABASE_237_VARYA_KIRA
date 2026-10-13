from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Title, WatchEntry, Genre

def entry_detail_view(request, pk):
    entry = get_object_or_404(WatchEntry, pk=pk)
    return render(request, 'partials/entry_detail.html', {'entry': entry})

def index_view(request):
    total_titles = Title.objects.count()
    completed_count = WatchEntry.objects.filter(status='completed').count()
    recent_entries = WatchEntry.objects.select_related('title').order_by('-id')[:5]

    context = {
        'total_titles': total_titles,
        'completed_count': completed_count,
        'recent_entries': recent_entries,
    }
    return render(request, 'index.html', context)


def catalog_view(request):
    entries = WatchEntry.objects.select_related('title').all()
    genres = Genre.objects.all()

    context = {
        'entries': entries,
        'genres': genres,
    }
    return render(request, 'catalog.html', context)


def stats_view(request):
    total_titles = Title.objects.count()
    total_entries = WatchEntry.objects.count()

    completed_count = WatchEntry.objects.filter(status='completed').count()
    in_progress_count = WatchEntry.objects.filter(status='watching').count()
    planned_count = WatchEntry.objects.filter(status='planned').count()

    context = {
        'total_titles': total_titles,
        'total_entries': total_entries,
        'completed_count': completed_count,
        'in_progress_count': in_progress_count,
        'planned_count': planned_count,
    }
    return render(request, 'stats.html', context)


@csrf_exempt
def api_update_status(request, entry_id):
    """API-действие: обновление статуса без перезагрузки"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            new_status = data.get('status')

            entry = get_object_or_404(WatchEntry, id=entry_id)
            entry.status = new_status
            entry.save()

            return JsonResponse({'success': True, 'new_status': entry.get_status_display()})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)
    return JsonResponse({'success': False, 'error': 'Invalid method'}, status=405)


@csrf_exempt
def api_delete_entry(request, entry_id):
    """API-действие: удаление записи без перезагрузки"""
    if request.method == 'POST':
        try:
            entry = get_object_or_404(WatchEntry, id=entry_id)
            entry.delete()
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)
    return JsonResponse({'success': False, 'error': 'Invalid method'}, status=405)
def update_status_view(request, pk):
    """Представление для обновления статуса"""
    pass