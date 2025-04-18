from django.shortcuts import render
import random
# Create your views here.
def salary_form(request):
    return render(request, 'salaryapp/form.html')

def salary_result(request):
    if request.method == 'POST':
        name = request.POST['name']
        gross = float(request.POST['gross'])
        tax = float(request.POST['tax'])
        bonus = float(request.POST['bonus'])

        net_salary = gross - (gross * tax / 100) + (gross * bonus / 100)

        return render(request, 'salaryapp/result.html', {
            'name': name,
            'net_salary': round(net_salary, 2)
        })

    return render(request, 'salaryapp/form.html')

def jumble_word(request):
    original_word = ''
    jumbled_word = ''

    if request.method == 'POST':
        original_word = request.POST['word']
        jumbled_word = ''.join(random.sample(original_word, len(original_word)))

    return render(request, 'salaryapp/jumble.html', {
        'original_word': original_word,
        'jumbled_word': jumbled_word
    })