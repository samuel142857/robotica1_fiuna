# este script de python esta hecho para poder hacer las imagenes mas pequenhas
# para que puedan ser procesadas durante el entrenamiento de la red neuronal
import glob
import cv2
import pandas as pd

path2="/content/Tf_config/TFmodels/research/workspace/training_demo/training/test/*.jpg"
path8="/content/Tf_config/TFmodels/research/workspace/training_demo/training/train/*.jpg"

name2 = "/_20/*.jpg"  # glob va a tomar todas las imagenes .jpg
name8 = "/_80/*.jpg"
# aplicamos resize a las imagenes, pero luego debemos hacer lo mismo con los labels
for file in glob.glob(path2):
    cv2.imwrite(file,cv2.resize(cv2.imread(file),(700,700),interpolation=cv2.INTER_CUBIC))
for file in glob.glob(path8):
    cv2.imwrite(file,cv2.resize(cv2.imread(file),(700,700),interpolation=cv2.INTER_CUBIC))

# este es el size inicial de las imagenes
w=4624
h=3472
#resize de los labels de train_clean
df=pd.read_csv("/content/Tf_config/TFmodels/research/workspace/training_demo/training/train_clean.csv")
df['xmin']=df['xmin']//(w//700)
df['ymin']=df['ymin']//(h//700)
df['xmax']=df['xmax']//(w//700)
df['ymax']=df['ymax']//(h//700)
df['width']=700
df['height']=700
print(df.dtypes)
df.to_csv("/content/Tf_config/TFmodels/research/workspace/training_demo/training/train_clean.csv")
# resize de los labels de test_clean
df=pd.read_csv("/content/Tf_config/TFmodels/research/workspace/training_demo/training/test_clean.csv")
df['xmin']=df['xmin']//(w//700)
df['ymin']=df['ymin']//(h//700)
df['xmax']=df['xmax']//(w//700)
df['ymax']=df['ymax']//(h//700)
df['width']=700
df['height']=700
print(df.dtypes)

print(df.head(10))
df.to_csv("/content/Tf_config/TFmodels/research/workspace/training_demo/training/test_clean.csv")
