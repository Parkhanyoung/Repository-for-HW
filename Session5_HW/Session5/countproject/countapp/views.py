from django.shortcuts import render

# Create your views here.


def count(request):
    return render(request, 'count.html')


def result(request):
    text = request.POST['text']
    total_length = len(text)
    except_blank = len(text.replace(" ", ""))
    word_length = len(text.split())
    return render(request, 'result.html',
                  {'text': text,
                   'total_length': total_length,
                   'word_length': word_length,
                   'except_blank': except_blank,
                   })
