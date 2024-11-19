def solution(rsp):
    rsp_list = {'2':'0', '0':'5', '5':'2'}
    return ''.join(rsp_list[i] for i in rsp)