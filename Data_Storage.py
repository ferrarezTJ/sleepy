import json 

class DataStorage:
  def save(libary):
    with open ('Library.json','w') as file:
      file = json.dump(data,file, indent = 4)

  def load(library):
    with open ('Libray.json','r') as file:
      data = json.load(file)
      return (data)

#Will try to separate Track and Playlist saving and loading

class Track_Storage(DataStorage):
  pass

class Playlist(DataStorage):
  pass
  