import cv2

im=cv2.imread('pic40.png')

f=open('input.txt','w')

#ngrid size, u have to enter
ngrid=1
xlist = list(range(0, im.shape[0], ngrid))
ylist = list(range(0, im.shape[1], ngrid))
#xlist.pop(-1)
#ylist.pop(-1)

for i in xlist:
    for j in ylist:
        print(i,j,ngrid,',',end=' ',file=f)

f.close()



def gridshade(im, y, x, ngrid):
    c = 0
    for i in range(ngrid):
        for j in range(ngrid):
            if(shade(im[y+i][x+j])):
                c += 1
    #threshold
    if c/(ngrid**2) >= 0.6:
        return ngrid**2
    else:
        return 0


def shade(pix):
    # if pix[0] < 10 and pix[1] < 10 and pix[2] < 10 or pix[0] < 60 and pix[1] < 100 and pix[2] < 50:
    #     return 1
    # return 0
    if ((pix[0]>=22 and pix[0]<=140) and (pix[1]>=13 and pix[1]<=255) and (pix[2]>=0 and pix[2]<=225)):
        return 1
    elif(pix[2]>=0 and pix[2]<=25):
        return 0
    return 0


def gridcolor(im, y, x, ngrid):
    for i in range(ngrid):
        for j in range(ngrid):
            im[y+i][x+j][0] = 0
            im[y+i][x+j][1] = 255
            im[y+i][x+j][2] = 0
            
c=0

img = cv2.imread('pic40.png',-1)




grid_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#cv2.imshow('rgb',grid_RGB) 
#cv2.waitKey(0)

image = cv2.cvtColor(grid_RGB, cv2.COLOR_RGB2HSV)
imager = cv2.imread('pic40.png',-1)
#cv2.imshow("hsv",grid_HSV) 
#cv2.waitKey(0)


            
f1=open('input.txt','r')
lr=f1.read()
l = lr.split(',')
l.pop(-1)
for i in l:
    i = i.split()
    if gridshade(image, int(i[0]), int(i[1]), int(i[2])):
        c+=1
        gridcolor(imager, int(i[0]), int(i[1]), int(i[2]))


cv2.imshow('gbr',img) 
cv2.waitKey(0)           

cv2.imshow("hello", imager)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(str(c/(imager.shape[0]*imager.shape[1])*110*(ngrid**2)))

