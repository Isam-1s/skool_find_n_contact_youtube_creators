from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import requests
from config import YOUTUBE_API_KEY, SCRAPER_API_KEY
from youtube_api import YouTubeDataManager

youtube_manager = YouTubeDataManager(youtube_api_key=YOUTUBE_API_KEY, scraper_api_key=SCRAPER_API_KEY)

class YouTubeDataManager :
    def __init__(self, youtube_api_key, scraper_api_key):
        self.youtube_api_key = youtube_api_key
        self.scraper_api_key = scraper_api_key
        self.youtube_service = self.build_youtube_service()
        self.using_scraper = False

    def build_youtube_service(self):
        return build("youtube", "v3", developerKey=self.youtube_api_key)
    
    def switch_to_scraper_api(self):
        print("YouTube rate limite reached. Now using API Scraper...")
        self.using_scraper = True

    def search_creators(self, query, max_results=10):
        if self.using_scraper:
            return self.search_creators_with_scraper(query, max_results)
        else:
            return self.search_creators_with_youtube(query, max_results)
        
    def search_creators_with_youtube(self, query, max_results=10):
        try:
            request = self.youtube_service.serach().list(
                q = query,
                part = "snippet",
                type = "channel",
                maxResults = max_results
            )
            response = request.execute()
            return response.get("items", [])
        except HttpError as e:
            if e.resp.status == 403:
                self.switch_to_scraper_api()
                return self.search_creators_with_scraper(query, max_results)
        else:
            raise

    def search_creators_with_scraper(self, query, max_results=10):
        pass
