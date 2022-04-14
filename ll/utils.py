import time

def get_time():
    times = time.strftime("%Y{}%m{}%d{} %X")
    return times.format("年","月","日")

if __name__=="__main__":
    print(get_time())