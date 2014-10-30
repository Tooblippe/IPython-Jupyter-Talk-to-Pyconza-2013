
import urllib
import json

class DescargaImagen(object):

    figshare_id = None
    nombre_imagen = None

    def __init__(self):
      pass

    def set_figshare_id(self,figshare_id):
      self.figshare_id = figshare_id

    def set_nombre_imagen(self,nombre_imagen):
      self.nombre_imagen = nombre_imagen

    def download(self):
      figshare_url = "http://api.figshare.com/v1/articles/%s" % self.figshare_id
      f = urllib.urlopen(figshare_url)
      info = json.load(f)
      image_url = info['items'][0]['files'][0]['download_url']
      urllib.urlretrieve(image_url, self.nombre_imagen)