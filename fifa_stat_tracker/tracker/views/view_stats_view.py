from django.views.generic import TemplateView


class ViewStatsView(TemplateView):
    template_name = 'tracker/view_stats.html'