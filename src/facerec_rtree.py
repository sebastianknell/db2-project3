import face_recognition as fr
import heapq
import numpy as np
from rtree import index
import os

def image_indexing(rtree_name, n_images):
  import os
  from rtree import index

  # Image collection folder path
  path = "./data/faces"
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
    folderPath = path + '/' + filePath
    imgList = os.listdir(folderPath)
    
    # Iterate over all images inside folder
    for file in imgList: 
      imagePath = folderPath + "/" + file
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

        format = {"path": folderPath, "name": file}

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

path = 'src/Test'
imagesList = os.listdir(path)

def encode(unencodedQuery):
    path = 'src/data'
    image = fr.load_image_file(path + '/' + unencodedQuery)
    return fr.face_encodings(image)[0]

def encodeRtree(unencoded):
    path = 'src/data'
    image = fr.load_image_file(path + '/' + unencoded)
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

def convert(box):
  return box[:int(len(box)/ 2)]

def rangeSearch(range, query):
  rtree = "indexrtreeFile12000"
  prop = index.Property()
  prop.dimension
  prop.buffering_capacity = 10
  rtreeIndex = index.Rtree(rtree, properties=prop)

  box = [x - range for x in query] + [x + range for x in query]

  return [
    item.id for item in rtreeIndex.intersection(box, objects='raw')
    if np.linalg.norm(convert(item.bbox) - query) <= range
  ]
  


# result = KNNRtree(2, "foto1.jpg", 4)
# print(list(result))

# NImagenes = 100
# path = "index"
# rtreeName = path + 'rtreeFile' + str(NImagenes)

# FacesRtree = image_indexing(rtreeName, NImagenes)
# print(KNNSequential(4,"foto1.jpg"))


# print(KNNSequential(3, "Abdoulaye_Wade/Abdoulaye_Wade_0004.jpg", 100))

test = fr.load_image_file("src\data\Aaron_Guiel\Aaron_Guiel_0001.jpg")
encoding = fr.face_encodings(test)



