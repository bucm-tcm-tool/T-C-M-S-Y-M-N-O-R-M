from urllib.request import urlopen
from urllib.parse import quote, unquote
# 由于学院内部需求，如果访问量过大，会切换为RNN网络，以减小压力。 每日10~12点维护
def TCMSymNorm(original_terms):
    normal_url = '维护中...'
    converted_term = []
    original_terms = [quote(x) for x in original_terms]
    if len(original_terms) > 0:
        original_terms = ','.join(original_terms)
    else:
        original_terms = '未识别到症状'

    request_info = normal_url + original_terms

    response = urlopen(request_info)
    print(response)
    get_noraml_info = response.read()

    get_noraml_info = eval(str(get_noraml_info, 'utf-8'))

    for converted in get_noraml_info:
        original_term = unquote(converted['input'])
        if converted.get('result', -1) != -1:
            normalization_term = unquote(converted['result'])

        else:
            normalization_term = '未识别到'

        converted_term.append(
            {'Origin': original_term, 'Normalization': normalization_term})
    # print((end_time-start_time).seconds)y
    return converted_term

text = ['彻夜不眠', '小溲黄']
result = TCMSymNorm(text)

print(result)
