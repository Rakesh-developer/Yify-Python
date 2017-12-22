BASE_API_URL="https://yts.am/api/v2"
from request_response import *
import os
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
         ""

     def _list_movies(self,args):
         """base method for all list movie methods"""
         """args: Dictionary """
         path="/list_movies.json"
         data=args
         req=Request("",BASE_API_URL)
         return req.call_api("GET",path,data)
     def moviesByGenre(self,genre):
        data={"genre":genre}
        return self._list_movies(data)
     def listMovies(self,name):
        data={"query_term":name}
        return self._list_movies(data)



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
    def downloadTorrent(self , path : str = os.path.expanduser('~/Downloads/') , fileName = '' ):
        if not fileName:
            fileName=self.name+'.torrent'
        else:
            fileName=fileName.strip('.torrent')+'.torrent'
            urlopen=urllib.request.URLopener()
            urlopen.addheader=[('user-agent','Mozilla/5.0')]
            urlopen.retrieve(self.url,path+fileName)
    def download(self,trackers=5):
        os.startfile(self.make_magnet(trackers))

def test():
    data={'url': 'https://yts.am/torrent/download/6E88B3F25BA49D483D740A652BF013C341BC5373', 'hash': '6E88B3F25BA49D483D740A652BF013C341BC5373', 'quality': '720p', 'seeds': 458, 'peers': 49, 'size': '1.02 GB', 'size_bytes': 1095216660, 'date_uploaded': '2015-11-01 00:18:06', 'date_uploaded_unix': 1446351486}
    x=Torrent(data)
    #x.downloadTorrent("C:\\Users\\Rakesh\\Desktop","moviename")
    #print(x.make_magnet())
    x.download()

test()
