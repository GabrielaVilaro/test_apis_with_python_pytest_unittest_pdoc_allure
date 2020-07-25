import datetime


class BaseNasaApi:
    def __init__(self):
        self.Format = "%Y-%m-%d"
        self.BackDay = datetime.date.today() - datetime.timedelta(days=2)
        self.Day = self.BackDay.strftime(self.Format)
        self.api_key = 'RNbDIcUjE81o0zefiEoJ1OaP6FMCBQcCzvUgRvrs'
        self.date = str(datetime.date.today().strftime("%Y-%m-%d"))
        self.hd = 'False'
        self.url = f"https://api.nasa.gov/planetary/apod?api_key={self.api_key}&date={self.Day}&hd={self.hd}"
        self.api_key_two = 'YnzlCuLqw7MXZV1Sn9QJP5jgycwu25Rskj5LAHSK'
        self.url_two = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={self.date}&end_date={self.BackDay}" \
                       f"&api_key={self.api_key_two}"
