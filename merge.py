import glob
from PIL import Image
from tqdm.notebook import tqdm

DIR = "C:/Users/10595/OneDrive/바탕 화면/NFT/"

skin_dir = DIR + "skin/"
face_dir =  DIR + "face/"
cloth_dir =  DIR + "cloth/"
hair_dir =  DIR + "hair/"

# 폴더에 있는 image file list로 할당
skins = glob.glob(skin_dir + "*.png")
faces = glob.glob(face_dir + "*.png")
clothes = glob.glob(cloth_dir + "*.png")
hairs = glob.glob(hair_dir + "*.png")

# skin, face, cloth, hair 순으로 위에 얹기
for i in range(0,len(skins)):
    for j in range(0,len(faces)):
        for k in range(0,len(clothes)):
            for l in range(0,len(hairs)):

                skinImage = Image.open(skins[i])
                faceImage = Image.open(faces[j])
                clothImage = Image.open(clothes[k])
                hairImage = Image.open(hairs[l])

                newImage = Image.alpha_composite(skinImage, faceImage)
                newImage = Image.alpha_composite(newImage, clothImage)
                newImage = Image.alpha_composite(newImage, hairImage)

                newImage.save(f"#{i}{j}{k}{l}.png","png")