class Statistics:
    def __init__(self):
        self.total_converts = 0
        self.daily_converts = 0
        self.total_downloads = 0
        self.daily_downloads = 0

    def add_converts(self):
        self.daily_converts += 1

    def add_downloads(self):
        self.daily_downloads += 1

    def clear_daily_stats(self):
        self.daily_converts = 0
        self.daily_downloads = 0

    def update_total_stats(self):
        self.total_converts += self.daily_converts
        self.total_downloads += self.daily_downloads

    def create_statistics_message(self):
        import datetime
        message = f'Report from {datetime.datetime.now()}\n\n' \
                  f'Daily number of converted texts: {self.daily_converts}\n' \
                  f'Total number of converted texts: {self.total_converts}\n\n' \
                  f'Daily wave files downloaded: {self.daily_downloads}\n' \
                  f'Total wave files downloaded: {self.total_downloads}'
        return message
