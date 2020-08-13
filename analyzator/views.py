import re

from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import TextForm
from .models import Text, Word


def input_text(request):
    if request.method == "POST":
        form = TextForm(request.POST)
        if form.is_valid():
            text_input = request.POST["text"]
            text_input_clear = re.sub(r"[^\w\s]", "", text_input)  # delete punctuation
            text_input_clear = text_input_clear.lower()
            text_input_clear = text_input_clear.split(" ")
            word_count_dict = {}
            for word in set(text_input_clear):
                word_count_dict[word] = text_input_clear.count(word)
            text_obj = Text(text=text_input)  # creation Text object
            text_obj.save()  # save Text object in DB
            words_obj_list = []
            for word, number in word_count_dict.items():
                if number > 5:
                    frequency_word = "high"
                elif number < 3:
                    frequency_word = "low"
                else:
                    frequency_word = "average"
                words_obj_list.append(
                    Word(
                        word=word,
                        amount=number,
                        text=text_obj,
                        frequency=frequency_word,
                    )
                )
            # In SQLite, there is a limit on the number of parameters in an SQL query.
            # We cannot create more than 199 objects
            while len(words_obj_list) > 199:
                Word.objects.bulk_create(words_obj_list[:199])
                words_obj_list = words_obj_list[199:]
            Word.objects.bulk_create(words_obj_list)
            return HttpResponseRedirect("statistic/{}".format(text_obj.id))
    else:
        print("\n GET\n")
        form = TextForm()
    return render(request, "index.html", {"form": form})


def statistic(request, text_id):
    text = Text.objects.get(pk=text_id)
    words = Word.objects.filter(text=text).order_by("-amount")
    print("text: ", text)
    print("20 words: ", words[:20])
    context = {"text": text, "words": words}
    return render(request, "statistic.html", context)
