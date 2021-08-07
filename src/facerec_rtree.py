import face_recognition as fr
import heapq
import numpy as np
from rtree import index
import os, datetime

path = "./data/faces"

def image_indexing(rtree_name, n_images):
  import os
  from rtree import index

  # Image collection folder path
  dirList = os.listdir(path)

  # Rtree index properties
  prop = index.Property()
  prop.dimension = 128 #D
  prop.buffering_capacity = 10 #M
  rtreeIndex = index.Index(rtree_name, properties = prop) #r-tree filename

  # Variables de apoyo
  index = 0
  breakUtility = False
  imagesList = []

  # Iterate over all person folders in collection
  for filePath in dirList:
    folderPath = path + "/" + filePath
    imgList = os.listdir(folderPath)
    
    # Iterate over all images inside folder
    for filename in imgList: 
      imagePath = folderPath + "/" + filename
      img = fr.load_image_file(imagePath)

    # Get encodings for all faces in current image
      faceEncodings = fr.face_encodings(img)

      # Para cada cara en la imagen
      for face in faceEncodings:

        # MAX Images  
        if index == n_images:
          breakUtility = True
          break

        tempCoords = list(face)

        for coord in face:
          tempCoords.append(coord)

        format = {"path": folderPath, "name": filename}

        rtreeIndex.insert(index, tempCoords, format)
        imagesList.append((index, imagePath))

        index = index + 1
        
      if breakUtility:
        break

    if breakUtility:
      break    
  rtreeIndex.close()

  print(str(index) + " images were processed.")

  return rtreeIndex

# -------------------------------------------------------------------------------------------

imagesList = os.listdir(path)

def encode(unencodedQuery):
    image = fr.load_image_file(unencodedQuery)
    return fr.face_encodings(image)[0]


def KNNSequentialIndex(n):
    path = 'src/data'
    dirList = os.listdir(path)

    count = 0
    names = []
    known = []
    raeachedN = False


    for filepath in dirList:

      folderPath = path + '/' + filepath
      imageList = os.listdir(folderPath)

      for imageFile in imageList:
        count += 1
        imagePath = folderPath + '/' + imageFile

        #processing this image
        print(imageFile)

        image = fr.load_image_file(imagePath)
        encodings = fr.face_encodings(image)[0]

        names.append(imageFile)
        known.append(encodings)

        if count == n:
          raeachedN = True
          break

      if raeachedN:
        break
    
    return (known, names)


def SequentialKNN(known, names, query, k):
  distancesList = fr.face_distance(known, query)
  result = []

  for i in range(len(known)):
    result.append((distancesList[i], names[i]))

  heapq.heapify(result)
  return heapq.nsmallest(k, result)


def KNNRtree(k, query, n):
    path = 'index'
    rtree = path + 'rtreeFile' + str(n)

    encodedQuery = encodeRtree(query)

    prop = index.Property()
    prop.dimension = 128
    prop.buffering_capacity = 10
    
    rtreeIndex = index.Rtree(rtree, properties=prop)
    queryList = list(encodedQuery)

    for elem in encodedQuery:
        queryList.append(elem)
    
    return rtreeIndex.nearest(coordinates=queryList, num_results=k, objects='raw')

    
def KNNRtree(k, query, n):
    rtree = 'RtreeIndexFile12000'
    encodedQuery = encode(query)
    prop = index.Property()
    prop.dimension = 128
    prop.buffering_capacity = 10
    rtreeIndex = index.Rtree(rtree, properties=prop)
    queryList = list(encodedQuery)

    for elem in encodedQuery:
        queryList.append(elem)
    return rtreeIndex.nearest(coordinates=queryList, num_results=k, objects='raw')


# rtreeName = 'RtreeIndexFile' + str(NImagenes)
# FacesRtree = image_indexing(rtreeName, NImagenes)

# result = list(KNNRtree(4, './data/saved/adam-sandler-test.jpeg', NImagenes))
# print(result[0]['name'])

# ----TESTS----

N = 100
print(N)
start = datetime.datetime.now()
print(KNNRtree(4, "./data/saved/adam-sandler-test.jpeg", N))
print(datetime.datetime.now() - start)
start = datetime.datetime.now()
print(KNNSequential(4, "./data/saved/adam-sandler-test.jpeg", N))
print(datetime.datetime.now() - start)
N = 200
print(N)
start = datetime.datetime.now()
print(KNNRtree(4, "./data/saved/adam-sandler-test.jpeg", N))
print(datetime.datetime.now() - start)
start = datetime.datetime.now()
print(KNNSequential(4, "./data/saved/adam-sandler-test.jpeg", N))
print(datetime.datetime.now() - start)
N = 400
print(N)
start = datetime.datetime.now()
print(KNNRtree(4, "./data/saved/adam-sandler-test.jpeg", N))
print(datetime.datetime.now() - start)
start = datetime.datetime.now()
print(KNNSequential(4, "./data/saved/adam-sandler-test.jpeg", N))
print(datetime.datetime.now() - start)
N = 800
print(N)
start = datetime.datetime.now()
print(KNNRtree(4, "./data/saved/adam-sandler-test.jpeg", N))
print(datetime.datetime.now() - start)
start = datetime.datetime.now()
print(KNNSequential(4, "./data/saved/adam-sandler-test.jpeg", N))
print(datetime.datetime.now() - start)
N = 1600
print(N)
start = datetime.datetime.now()
print(KNNRtree(4, "./data/saved/adam-sandler-test.jpeg", N))
print(datetime.datetime.now() - start)
start = datetime.datetime.now()
print(KNNSequential(4, "./data/saved/adam-sandler-test.jpeg", N))
print(datetime.datetime.now() - start)
N = 3200
print(N)
start = datetime.datetime.now()
print(KNNRtree(4, "./data/saved/adam-sandler-test.jpeg", N))
print(datetime.datetime.now() - start)
start = datetime.datetime.now()
print(KNNSequential(4, "./data/saved/adam-sandler-test.jpeg", N))
print(datetime.datetime.now() - start)
N = 6400
print(N)
start = datetime.datetime.now()
print(KNNRtree(4, "./data/saved/adam-sandler-test.jpeg", N))
print(datetime.datetime.now() - start)
start = datetime.datetime.now()
print(KNNSequential(4, "./data/saved/adam-sandler-test.jpeg", N))
print(datetime.datetime.now() - start)
N = 12000
print(N)
start = datetime.datetime.now()
print(KNNRtree(4, "./data/saved/adam-sandler-test.jpeg", N))
print(datetime.datetime.now() - start)
start = datetime.datetime.now()
print(KNNSequential(4, "./data/saved/adam-sandler-test.jpeg", N))
print(datetime.datetime.now() - start)


(known, names) = KNNSequentialIndex(N)
test = fr.load_image_file("./data/faces/Abdullah/Abdullah_0002.jpg")
query = fr.face_encodings(test)
SequentialKNN(known, names, test, 4)