import face_recognition as fr
import heapq
import numpy as np
from rtree import index
import os

def image_indexing(rtree_name, n_images):
  import os
  from rtree import index

  # Image collection folder path
  path = "src/data"
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

        format = {"path": folderPath, "name": file};

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
    path = 'src/Test'
    image = fr.load_image_file(path + '/' + unencodedQuery)
    return fr.face_encodings(image)[0]

def encodeRtree(unencoded):
    path = 'src/data'
    image = fr.load_image_file(path + '/' + unencoded)
    return fr.face_encodings(image)[0]

def KNNSequential(k, query):
    encodedQuery = encode(query)
    path = 'src/Test'
    dirList = os.listdir(path)

    count = 0
    names = []
    known = []

    for filename in dirList:
        count += 1

        print("Processing: ", filename)
        imageFile = path + '/' + filename
        image = fr.load_image_file(imageFile)

        encodings = fr.face_encodings(image)[0]

        names.append(filename)
        known.append(encodings)
    
    distances = fr.face_distance(known, encodedQuery)
    result = []

    for i in range(count):
        result.append((distances[i], names[i]))
    
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

# result = KNNRtree(2, "foto1.jpg", 4)
# print(list(result))





#print(KNNSequential(4,"foto1.jpg"))

nImagenes = 12000
path = 'index'
rtree = path + 'rtreeFile' + str(nImagenes)
image_indexing(rtree, nImagenes)

# result = KNNRtree(4, "Aaron_Sorkin/Aaron_Sorkin_0001.jpg", 100)
# print(list(result))

