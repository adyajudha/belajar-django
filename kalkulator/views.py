from django.shortcuts import render

# Create your views here.

def kalkulator(request, num1, num2, operasi):
    operasi_dict = {
        'tambah': ('Kalkulator Tambah', f"{num1} + {num2} = {num1 + num2}"),
        'kurang': ('Kalkulator Kurang', f"{num1} - {num2} = {num1 - num2}"),
        'kali': ('Kalkulator Perkalian', f"{num1} * {num2} = {num1 * num2}"),
        'bagi': ('Kalkulator Pembagian', f"{num1} / {num2} = {num1 / num2:.2f}"),
    }

    title, result = operasi_dict.get(operasi, ('Operasi Tidak Dikenal', 'Hasil tidak valid'))
    
    context = {
        'title': title,
        'result': result,
    }

    return render(request, 'kalkulator/index.html', context)
