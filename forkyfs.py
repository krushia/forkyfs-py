# forkyfs
import os
import shutil

class forkyfs:
	def __init__(self):
		self.basepath = '/home/krushia/forkfs-test/'
	def listInstances(self, template, subdict=None):
		tpath = template.lower() + "s/"
		fullpath = self.basepath + tpath
		results = os.listdir(fullpath)
		if subdict is None:
			return results
		matchresults = list()
		for i in results:
			for s in subdict:
				v = self.get(tpath+i+"/"+s)
				if v != subdict[s]:
					break
			else:
				matchresults.append(i)
		return matchresults
	def get(self, path):
		fullpath = self.basepath + path
		f = open(fullpath, 'r')
		result = f.read()
		f.close()
		return result
	def set(self, path, value):
		fullpath = self.basepath + path
		f = open(fullpath, 'w')
		f.write(value)
		f.close()
		return True
	def listTemplates(self):
		fullpath = self.basepath + "definitions"
		return os.listdir(fullpath)
	def newInstance(self, name, template, subdict=None):
		src = self.basepath + "definitions/" + template.upper()
		dst = self.basepath + template.lower() + "s/" + name
		shutil.copytree(src, dst)
		if subdict is None:
			return

	def delInstance(self, name, template):
		dst = self.basepath + template.lower() + "s/" + name
		shutil.rmtree(dst)
