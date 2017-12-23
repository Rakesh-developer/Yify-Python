BASE_API_URL="https://yts.am/api/v2"
from request_response import *
import os
import webbrowser
import urllib

trackers = [

        'udp://open.demonii.com:1337/announce',

        'udp://tracker.openbittorrent.com:80',

        'udp://tracker.coppersurfer.tk:6969',

        'udp://glotorrents.pw:6969/announce',

        'udp://tracker.opentrackr.org:1337/announce',

        'udp://torrent.gresille.org:80/announce',

        'udp://p4p.arenabg.com:1337',

        'udp://tracker.leechers-paradise.org:6969',

        'http://track.one:1234/announce',

        'udp://track.two:80'
        ]
class Yify():
     def __init__(self):
         self.req=Request("",BASE_API_URL)

     def _list_movies(self,args,path=""):
         """base method for all list movie methods. should be used only by this class methods"""
         """args: Dictionary """
         path="/list_movies.json"
         data=args
         #req=Request("",BASE_API_URL)
         result= self.req.call_api("GET",path,data).extract()
         if result['data'].get('movies'):
             return result["data"]["movies"]
         else:
            "No movies Found"
     def listMovies():
         pass
     def moviesByGenre(self,genre):
        data={"genre":genre}
        return self._list_movies(data)

     def MoviesByName(self,name):
         """Method to list movies specified in the parameter"""
         """args: Name"""
         data={"query_term":name}
         return self._list_movies(data)
     def moviesByQuality(self,quality="1080p"):
         """Method to list movies by quality."""
         """args: quality; Default:1080p"""
         """returns: latest movie in specified quality"""
         data={"quality":quality}
         return self._list_movies(data)
     def moviesByRating(self,rating):
        """methods to list movies by rating"""
        """args: Rating; Default: 0"""
        """returns: List of movies based on rating"""
        data={"rating":rating}
        return self._list_movies(data)

     def listUpcoming(self):
         """List latest 4 upcoming movies in YTS"""
         path="/list_upcoming.json"
         return self._list_movies({},path)
     def extractNameId(self,movies_list):
         """Method to extract Movie Id and Name"""
         movieId=dict()
         for movie in movies_list:
             movieId[movie["title"]]=movie["id"]
         return movieId




class Torrent():
    """Class used to download torrents or movies"""
    def __init__(self,torrent):
        self.name=''
        self.url=torrent.get("url")
        self.hash=torrent.get("hash")
        self.quality=torrent.get("quality")
        self.seeds=torrent.get("seeds")
        self.peers=torrent.get("peers")
        self.size=torrent.get("size")
        self.size_bytes=torrent.get("size_bytes")
        self.date_uploaded=torrent.get("date_uploaded")



    def make_magnet(self,tracks=5):
        movie_encode="dn="+self.name
        self.magnet='magnet:?xt=urn:btih:{}&{}'.format(self.hash ,movie_encode)
        for tracker in trackers[tracks]:
            self.magnet=self.magnet+tracker
        return self.magnet
    def downloadTorrent(self):
         webbrowser.open(self.url)
    def download(self,trackers=5):
        """dowloads movie directly using magnet links"""
        os.startfile(self.make_magnet(trackers))


class Movie():
    def __init__(self,movie_id=None):
        self.movieId=movie_id
        self.req=Request("",BASE_API_URL)

    def getDetails(self):
        """Method to get details about the movie"""
        """args: Movie_ID"""
        """returns movie details"""
        path="/movie_details.json"
        data={"movie_id":self.movieId}
        result=self.req.call_api("GET",path,data).extract()
        if result['data'].get('movie'):
             return result["data"]["movie"]
        else:
            return "No movies Found"

    def getReviews(self):
        path="/movie_reviews.json"
        data={"movie_id":self.movieId}
        return self.req.call_api("GET",path,data).extract()
    def suggestions(self):
        path="/movie_suggestions.json"
        data={"movie_id":self.movieId}
        result=self.req.call_api("GET",path,data).extract()
        if result['data'].get('movies'):
             return result["data"]["movies"]
        else:
            "No movies Found"








def test():
    data={'url': 'https://yts.am/torrent/download/6E88B3F25BA49D483D740A652BF013C341BC5373', 'hash': '6E88B3F25BA49D483D740A652BF013C341BC5373', 'quality': '720p', 'seeds': 458, 'peers': 49, 'size': '1.02 GB', 'size_bytes': 1095216660, 'date_uploaded': '2015-11-01 00:18:06', 'date_uploaded_unix': 1446351486}
    x=Torrent(data)
    y=Yify()

    #x.downloadTorrent("C:\\Users\\Rakesh\\Desktop","moviename")
    #print(x.make_magnet())
    x=y.MoviesByName("fifty shades")
    print(y.extractNameId(x))
    m=Movie(6448)
    print(m.getDetails())
test()
