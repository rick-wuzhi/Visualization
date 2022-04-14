import pandas as pd
import json


def data_province(path):
    data_for = pd.read_csv(path,encoding="gbk")
    top_30 = data_for.sort_values(by=['累计确诊'], ascending=False)[:10].reset_index(drop=True)
    top_30['累计确诊'] = top_30['累计确诊']/1000000
    top_30['治愈'] = top_30['治愈']/1000000
    top_30['死亡'] = top_30['死亡']/10000
    top_30['治愈率'] = top_30['治愈']*1000000/(top_30['累计确诊']*1000000-top_30['死亡']*10000)*100
    return top_30

def data_china(path):
    data = pd.read_csv(path,encoding='gbk')
    p = data[['地区', '新增']]
    qi = data[['地区','累计']]
    dataset = []
    for i in range(len(p)):
        dataset.append({'name':p.loc[i,'地区'],'value':int(p.loc[i,'新增'])})
    zizhiqu = ['内蒙古','广西','西藏','宁夏','新疆']
    zhixiashi = ['北京','天津','上海','重庆']
    tebiexing = ['香港','澳门']
    pro = []
    zizhi = []
    zhixia = []
    tebie = []
    for i in range(len(qi)):
        name = qi.loc[i,'地区']
        value = int(qi.loc[i,'累计'])
        if name in zizhiqu:
            zizhi.append({'name':name,'value':value})
        elif name in zhixiashi:
            zhixia.append({'name':name,'value':value})
        elif name in tebiexing:
            tebie.append({'name':name,'value':value})
        else:
            pro.append({'name':name,'value':value})
    qibao= [{'name':'省份','data':pro},{'name':'自治区','data':zizhi},{'name':'直辖市','data':zhixia},{'name':'特别行政区','data':tebie}]
    return dataset,qibao


def data_hist(data_provinces):
    data_p = data_provinces['地区']
    data_c = data_provinces['累计确诊']
    data_r = data_provinces['治愈']
    data_d = data_provinces['死亡']
    data_zhi = data_provinces['治愈率']
    Xaix = []
    datas_1 = []
    datas_2 = []
    datas_3 = []
    datas_4 = []
    for j in range(len(data_provinces)):
        Xaix.append(data_p[j])
        datas_1.append(data_c[j])
        datas_2.append(data_r[j])
        datas_3.append(data_d[j])
        datas_4.append(data_zhi[j])
    return Xaix,datas_1,datas_2,datas_3,datas_4

if __name__ == "__main__":
    path = "../data_save/新冠肺炎疫情最新动态（国外）.csv"
    data_jiu = data_province(path)
    print(data_jiu)
    # a = data_jiu[data_jiu['Province']=='Zhejiang'][['Confirmed','Date']].groupby(['Date']).sum()['Confirmed']
    # for i in a:
    #     x.append(int(i))
    # print(x)