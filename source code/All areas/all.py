from mrjob.job import MRJob
#from mrjob.step import MRStep


class classifier(MRJob):

    DIRS = ['/home/niksram/.local/lib/python3.6/site-packages/numpy','/home/niksram/.local/lib/python3.6/site-packages/cv2','hdfs:///user/niksram/Input/images#IMAGES']
    #DIRS=['directory containing numpy __init__.py','directory containing opencv __init__.py','uri(or)directory of images#IMAGES']

    def mapper(self, _, record):
        import numpy as np
        import cv2
        def gridshade(self, im, y, x, ngrid): #identifies whether a chunk of pixels of size ngrid**2 can be classified as green-area
            c = 0
            for i in range(ngrid):
                for j in range(ngrid):
                    c+=shade(self, im[y+i][x+j])
            if c/(ngrid**2) >= 0.5: #threshold percentage for classifying a given ngrid**2 chunk as green 
                return ngrid**2
            else:
                return 0
        
        def shade(self, pix): #identifies whether a given hsv pixel is within the green range
            if ((pix[0]>=22 and pix[0]<=140) and (pix[1]>=13 and pix[1]<=255) and (pix[2]>=0 and pix[2]<=220)):
                return 1
            else:
                return 0
        #for item in record
        k = record.split('-') #splitting the line to extract data
        im=cv2.imread('IMAGES/'+k[2])
        im = cv2.cvtColor(cv2.cvtColor(im, cv2.COLOR_BGR2RGB), cv2.COLOR_RGB2HSV) #converting BGR image to HSV format
        ngrid = 1 #deciding the chunk span
        c = 0
        for i in list(range(0, im.shape[0]-(ngrid-im.shape[0]%ngrid), ngrid)): #excluding the last chunk of pixels in a column
            for j in list(range(0, im.shape[1]-(ngrid-im.shape[1]%ngrid), ngrid)): #excluding the last chunk of pixels in a row
                c += gridshade(self, im, i, j, ngrid)
        per = c/(im.shape[0]*im.shape[1])*100 #calculating percentage of green area in the given image
        yield(k[0], '-'.join([str(int(per)), k[1]]))

    def combiner(self, area, values):
        for i in area.split(): #for every key provided at an instance
            prop = 0
            totarea = 0
            for j in values: #for every image from that area
                v = j.split('-')
                prop += float(v[0])*float(v[1]) 
                totarea += float(v[1])
            if totarea == 0: #avoid zero-division error
                val = 0
            else:
                val = prop/totarea
            yield(str(i), '-'.join([str(val), str(totarea)]))

    def reducer(self, area, values):
        for i in area.split():
            for j in values:
                v = j.split('-')
                yield(str(i), '-'.join([str(float(v[0])*1.2), str(v[1])])) #adding an extra 20 percent which acts as a bias to result in better overall accuracy (to include void spaces)


if __name__ == '__main__':
    classifier.run()
