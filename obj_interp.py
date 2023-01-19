def read_verts(filename):
  verts = []
  file = open(filename, 'r')
  Lines = file.readlines()
  for line in Lines:
    if line[0] == "v" :
      raw = line.replace("\n", "").replace("v ","").split(" ")
      for x in range(len(raw)):
        raw[x] = float(raw[x])
      verts.append(raw)
  file.close()
  return verts

def read_faces(filename):
  verts = []
  file = open(filename, 'r')
  Lines = file.readlines()
  for line in Lines:
    if line[0] == "f" :
      raw = line.replace("\n", "").replace("f ","").split(" ")
      for x in range(len(raw)):
        raw[x] = int(raw[x])
      verts.append(raw)
  file.close()
  return verts