from django.http import JsonResponse
from django.shortcuts import render
from AnswerApp.answer_build.BuildAnswer import answer
from AnswerApp.input_analyse.input_analyse import QuestionAnalyse
# 该类进行形成答案
from django.contrib.auth import authenticate, login
question_analyse = QuestionAnalyse()


def do_login(request):
    print(request.POST)
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            print(user)
            login(request=request, user=user)
            return JsonResponse({"code": 200})
        else:
            return JsonResponse({"status": 'fail'})
    # 返回一个无效帐户的错误
    else:
        return JsonResponse({"status": 'fail'})


# 思路 ,通过神经网络的意图识别，得到意图分类，然后去图数据库查询


def question_controller(request):
    # try:
    question = request.POST.get('txt_question')
    print(request.POST)
    # 回答一个问题经过4部分
    # 1. 先判断输入的问题

    answer_type, intention = question_analyse.analyse(question)
    print(answer_type)
    print(intention)

    answers, domains = answer(question, answer_type, intention)

    list1 = ['', '']  # 当前阶段不
    response = JsonResponse({"status": 'successful', 'data': answers, 'list': list1})
    return response  # type: JsonResponse


# # 记录
# basic_util.write_text_ap
# end(FilePath.root_dir_answer_record + r"\question_collection.txt", intention + '<\.sp.\>' + question)
# # 记录
# basic_util.write_text_apend(FilePath.root_dir_answer_record + r"\answer_record_detail.txt",
#                       date_util.get_current_y_m_d_h_m_s() + " " + str(data))

# except Exception as e:
#     print(e)
#     return JsonResponse({"status": 'successful', 'data': {'answer': "不知道你在说什么"}, 'list': []})


def show_index(request):
    return render(request, 'index.html')
