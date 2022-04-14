from flask import Flask
from flask import render_template
from data_deal import deal
import utils

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/time')
def get_time():
    return utils.get_time()

@app.route('/tss')
def hhh():
    path_1 = "data_save/新冠肺炎疫情最新动态（国外）.csv"
    path_2 = "data_save/新冠肺炎疫情最新动态（国内）.csv"
    data_jiu = deal.data_province(path_1)
    # pie_data = deal.data_pie(data_jiu)
    Xaix,datas_1,datas_2,datas_3,datas_4 = deal.data_hist(data_jiu)
    datamap,qibao = deal.data_china(path_2)
    # dt = deal.data_date(path)
    # name_mix,total_mix = deal.data_mix(data_jiu)
    # n_r = int(data_jiu['Recovered'].sum()/1000000)
    # n_c = int(data_jiu['Confirmed'].sum()/1000000)
    # path_2 = 'data_save/疫情鼓励语句.txt'
    # url = 'data_save/1.png'
    # to_url = 'static/img/cloud.jpg'
    # cc.ciyun(path_2,url,to_url)
    return render_template('page.html', x=Xaix, d_1=datas_1, d_2=datas_2, d_3=datas_3,d_4=datas_4,datamap=datamap,qibao=qibao)

@app.route('/ajax',methods=["post","get"])
def h():
    return "10"

@app.route('/tm/')
def he():
    return render_template("indexx.html")

if __name__ == '__main__':
    app.run()
