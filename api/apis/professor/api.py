from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from api.apis.professor.forms import ProfessorGetForm, ProfessorRateForm
from api.db_models.comment import Comment
from api.db_models.professor import Professor


class ProfessorViewSet(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = ''

    def get(self, request, *args, **kwargs):
        form = ProfessorGetForm(request.GET)
        form.is_valid()
        if not form.errors:
            professor_id = form.cleaned_data.get('professor_id')
            professor = Professor.objects.filter(id=professor_id).first()
            if professor_id:
                comments = Comment.objects.filter(professor_id=professor_id)
                if self.request.user.user_type == 'student':
                    comment_check = comments.filter(student_id=request.user.student.id).first()
                else:
                    comment_check = None

                context = dict(professor=professor, comments=comments,
                               comment_check=comment_check)
            else:
                pass
                # TODO professor does not exist
            return render(request, template_name='professor_page.html', context=context)

        return HttpResponseRedirect('/login/')

    def post(self, request, *args, **kwargs):
        # TODO if user_type staff return false
        form = ProfessorRateForm(request.POST)
        professor_id = request.GET.get('professor_id')
        form.is_valid()
        if not form.errors:
            cleaned_data = form.cleaned_data
            professor = Professor.objects.filter(id=professor_id).first()
            rate_count = professor.total_rate_count + 1

            kindness_rate = professor.kindness_rate
            kindness_rate = (kindness_rate * (rate_count - 1) + cleaned_data.get('kindness_rate')) / rate_count
            professor.kindness_rate = kindness_rate

            hot_rate = professor.hot_rate
            hot_rate = (hot_rate * (rate_count - 1) + cleaned_data.get('hot_rate')) / rate_count
            professor.hot_rate = hot_rate

            response_rate = professor.response_rate
            response_rate = (response_rate * (rate_count - 1) + cleaned_data.get('response_rate')) / rate_count
            professor.response_rate = response_rate

            teach_rate = professor.teach_rate
            teach_rate = (teach_rate * (rate_count - 1) + cleaned_data.get('teach_rate')) / rate_count
            professor.teach_rate = teach_rate

            approach_rate = professor.approach_rate
            approach_rate = (approach_rate * (rate_count - 1) + cleaned_data.get('approach_rate')) / rate_count
            professor.approach_rate = approach_rate

            salary_estimation = professor.salary_estimation
            professor.salary_estimation = (salary_estimation * (rate_count - 1) + cleaned_data.get(
                'salary_estimation')) / rate_count

            total_rate = professor.total_rate
            professor.total_rate = (total_rate * (rate_count - 1) + (
                    kindness_rate + hot_rate + response_rate + teach_rate + approach_rate) / 5) / rate_count

            professor.total_rate_count = rate_count

            professor.save()

            comment_data = cleaned_data.get('comment')
            comment = Comment.objects.create(comment=comment_data, professor_id=professor_id,
                                             student_id=request.user.student.id)
            comment.save()
            return HttpResponseRedirect(f'/professor/?professor_id={professor_id}')
