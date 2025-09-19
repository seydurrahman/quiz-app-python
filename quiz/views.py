from django.shortcuts import render
from .models import Question, Choice

def quiz(request):
    questions = Question.objects.all().prefetch_related("choices")

    if request.method == "POST":
        score = 0
        for question in questions:
            selected = request.POST.get(str(question.id))
            if selected:  # make sure user answered
                correct = Choice.objects.filter(id=selected, is_correct=True).exists()
                if correct:
                    score += 1

        return render(request, "quiz/score.html", context={
            "total_question": questions.count(),
            "score": score
        })

    return render(request, "quiz/quiz.html", context={"questions": questions})
