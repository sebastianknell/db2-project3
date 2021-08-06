def image_processing(rtree_name, n_images):
  from rtree import index
  import face_recognition
  import os

  # Image collection folder path
  path = "src\data"
  dirList = os.listdir(path)

  prop = index.Property()
  prop.dimension = 128 #D
  prop.buffering_capacity = 10 #M
  rtreeIndex = index.Index(rtree_name, properties = p) #r-tree filename

  index = 0
  breakUtility = False
  imagesList = []

  # Iterate over all person folders in collection
  for file_path in dirList:
    path_tmp = path + "/" + file_path

    imgList = os.listdir(path_tmp)
    
    # Iterate over all images inside folder
    for file_name in imgList: 
      path_tmp2 = path_tmp + "/" + file_name
      img = face_recognition.load_image_file(path_tmp2)

    # Get encodings for all faces in current image
      unknown_face_encodings = face_recognition.face_encodings(img)

      for elem in unknown_face_encodings:

        # MAX Images  
        if index == n_images:
          break_fg = True
          break

        coor_tmp = list(elem)
        for coor_i in elem:
          coor_tmp.append(coor_i)
        tmp_obj = {"path": path_tmp, "name": file_name};
        rtreeIndex.insert(index, coor_tmp, tmp_obj)
        imagesList.append((index, path_tmp2))
        index = index + 1
        
      if break_fg:
        break

    if break_fg:
      break    
  rtreeIndex.close()

  print(str(index) + " images processed")
  
  return rtreeIndex

NImagenes = 100
path = "test"
rtreeName = path + 'rtreeFile' + str(NImagenes)

FacesRtree = image_processing(rtreeName, NImagenes)