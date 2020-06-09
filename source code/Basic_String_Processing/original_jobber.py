from mrjob.job import MRJob

class MRWordCount(MRJob):

   def mapper(self, _, line):
	a = line.strip('\n')
	a="".join(a)
	a=a.split(' ')
	yield(float(a[-1]),a[0:-1])

   def reducer(self, per,word):
	if per>0.75:
	      yield(" ".join(list(word)[0]),per)

if __name__ == '__main__':
   MRWordCount.run()
