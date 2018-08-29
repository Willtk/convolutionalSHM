import os
import imageio
import numpy

# Imagens originais devem estar dentro da pasta oImages.
# Imagens geradas devem estar dentro da pasta gImages.

# As imagens originais e geradas devem estar com o mesmo nome e o
# mesmo formato.

# A comparação será feita pelo nome , portanto a imagem 'd1.jpg' da
# pasta oImages e comparada com a 'd1,jpg' da pasta gImages.


#################### PARÂMETROS INICIAIS ###########################


PASTA_DE_IMAGENS_ORIGINAIS = 'oImages'
PASTA_DE_IMAGENS_GERADAS = 'gImages'
CORTAR_IMAGENS_ORIGINAIS = True
CORTAR_IMAGENS_GERADAS = True
FORCAR_RESIZE = True


####################################################################


original_data_path = os.getcwd()  + '//' + PASTA_DE_IMAGENS_ORIGINAIS
geradas_data_path = os.getcwd()   + '//' + PASTA_DE_IMAGENS_GERADAS

oImages = os.listdir(original_data_path)

erro_medio = {}


'''
def compareWhite(arrayA,arrayB,p):
    perc = 0
    cont = 0
    cont2 = 0
    
    for r in arrayA:
        cont += 1
        if((sum(r)/3) > 250):
            cont2 += 1
    perc = cont2/cont
    return (perc>p)
'''

def rgb2gray(rgb):
    return numpy.dot(rgb[...,:3], [0.299, 0.587, 0.114])

def cutImages(img):
    
    img_rows = img.shape[0]
    img_columns = img.shape[1]
    
    white_line = numpy.ones((875,3), dtype = 'uint8')
    white_line = white_line * 255
    
    cont = 0
    new_img = img[:]
    
    for i in range(0,img_rows):
        row = img[i]
        if(numpy.allclose(row,white_line,rtol=0.99,atol=0.99)):
            new_img = numpy.delete(new_img, (cont), axis=0)
            cont -= 1
        cont+=1

    white_column = numpy.ones((656,3), dtype = 'uint8')
    white_column = white_column * 255
    cont = 0
    
    
    for j in range(0,img_columns):
        column = img[:,j]
        if(numpy.allclose(column,white_column,rtol=0.99,atol=0.99)):
            new_img = numpy.delete(new_img, (cont), axis=1)
            cont -= 1
        cont+=1

    return new_img

all_mean = []

for o in oImages:
    ori_img = imageio.imread(original_data_path + '//' + o)
    if(CORTAR_IMAGENS_ORIGINAIS):
        ori_img = cutImages(ori_img)
    ger_img = imageio.imread(geradas_data_path + '//' + o)
    if(CORTAR_IMAGENS_GERADAS):
        ger_img = cutImages(ger_img)
    if(FORCAR_RESIZE):
        minrow = min(ori_img.shape[0],ger_img.shape[0])
        mincol = min(ori_img.shape[1],ger_img.shape[1])
        ori_img = ori_img[0:minrow,0:mincol]
        ger_img = ger_img[0:minrow,0:mincol]
        gray_ori = rgb2gray(ori_img)
        gray_ger = rgb2gray(ger_img)
        e = gray_ori - gray_ger
        e = sum(abs(e))                      #Manhattan norm
        e = e.mean()
        e = e/70000
        #e = numpy.linalg.norm(e.ravel(), 0)   #Zero norm
        erro_medio[o] = e
    else:
        if((ori_img.shape[0] != ger_img.shape[0]) or (ori_img.shape[1] != ger_img.shape[1])):
            erro_medio[o] = 'NaN'
        else:
            e = (ori_img == ger_img).all(axis=(0,2)).mean()
            erro_medio[o] = e

    all_mean.append(e)

erro_medio["TODOS"] = sum(all_mean)/len(all_mean)
print(erro_medio)


    





