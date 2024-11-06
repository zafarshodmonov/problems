from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Problem
from django.template.loader import render_to_string
import pdfkit  # PDF yaratish uchun

def problem_list(request):
    problems = Problem.objects.all()
    return render(request, 'problems/problem_list.html', {'problems': problems})

def problem_detail(request, pk):
    problem = get_object_or_404(Problem, pk=pk)
    return render(request, 'problems/problem_detail.html', {'problem': problem})

def download_problem_pdf(request, pk):
    problem = get_object_or_404(Problem, pk=pk)
    html = render_to_string('problems/problem_pdf.html', {'problem': problem})
    pdf = pdfkit.from_string(html, False)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{problem.title}.pdf"'
    return response
