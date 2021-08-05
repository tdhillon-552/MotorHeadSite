import json
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string

from weasyprint import HTML

from .models import Stats


def statsprint(request):
    start_date = request.session.get('pass_start_date_stats')
    end_date = request.session.get('pass_end_date_stats')
    searched_motor = json.loads(request.session.get('pass_searched_motor_stats'))

    search_query = Stats.objects.filter(date__range=[start_date, end_date], user=searched_motor)

    search_results = {
        'start_date': start_date,
        'end_date': end_date,
        'searched_motor': User.objects.filter(pk=searched_motor)[0],
        'court': sum(total.court for total in search_query),
        'personal': sum(total.personal for total in search_query),
        'training': sum(total.training for total in search_query),
        'equipment': sum(total.equipment for total in search_query),
        'meetings': sum(total.meetings for total in search_query),
        'accident': sum(total.accident for total in search_query),
        'crime': sum(total.crime for total in search_query),
        'patrol_coverage': sum(total.patrol_coverage for total in search_query),
        'call_out': sum(total.call_out for total in search_query),
        'other': sum(total.other for total in search_query),
        'enforcement_stops': sum(total.enforcement_stops for total in search_query),
        'citations': sum(total.citations for total in search_query),
        'mechanicals': sum(total.mechanicals for total in search_query),
        'OTS_Cites': sum(total.OTS_Cites for total in search_query),
        'complaint_areas': sum(total.complaint_areas for total in search_query),
        'accident_reports': sum(total.accident_reports for total in search_query),
        'accident_sups': sum(total.accident_sups for total in search_query),
        'arrests': sum(total.arrests for total in search_query),
        'NAT': sum(total.NAT for total in search_query),

    }

    html_string = render_to_string('MotorHeadApp/statsprint.html', {

        'search_results': search_results
    })

    html = HTML(string=html_string)
    html.write_pdf(target='/tmp/mypdf.pdf')

    fs = FileSystemStorage('/tmp')
    with fs.open('mypdf.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="advStats.pdf"'
        return response


def totalsprint(request):
    start_date = request.session.get('pass_start_date_totals')
    end_date = request.session.get('pass_end_date_totals')

    search_query = Stats.objects.filter(date__range=[start_date, end_date],)

    search_results = {
        'start_date': start_date,
        'end_date': end_date,
        'court': sum(total.court for total in search_query),
        'personal': sum(total.personal for total in search_query),
        'training': sum(total.training for total in search_query),
        'equipment': sum(total.equipment for total in search_query),
        'meetings': sum(total.meetings for total in search_query),
        'accident': sum(total.accident for total in search_query),
        'crime': sum(total.crime for total in search_query),
        'patrol_coverage': sum(total.patrol_coverage for total in search_query),
        'call_out': sum(total.call_out for total in search_query),
        'other': sum(total.other for total in search_query),
        'enforcement_stops': sum(total.enforcement_stops for total in search_query),
        'citations': sum(total.citations for total in search_query),
        'mechanicals': sum(total.mechanicals for total in search_query),
        'OTS_Cites': sum(total.OTS_Cites for total in search_query),
        'complaint_areas': sum(total.complaint_areas for total in search_query),
        'accident_reports': sum(total.accident_reports for total in search_query),
        'accident_sups': sum(total.accident_sups for total in search_query),
        'arrests': sum(total.arrests for total in search_query),
        'NAT': sum(total.NAT for total in search_query),

    }

    html_string = render_to_string('MotorHeadApp/totalsprint.html', {

        'search_results': search_results
    })

    html = HTML(string=html_string)
    html.write_pdf(target='/tmp/mypdf.pdf')

    fs = FileSystemStorage('/tmp')
    with fs.open('mypdf.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="advStats.pdf"'
        return response
