'''
Created on 2014-9-8

@author: lqh
'''

import os
import os.path

class DirLooper(object):
    '''
    classdocs
    '''


    def __init__(self,params):
        '''
        Constructor
        '''
        self.path=params
    
    def looper(self):
        for parent,dirnames,filenames in os.walk(self.path):
#            for driname in dirnames:
#                print ("parent is :"+parent)
#                print("dirname is "+dirname)
            for filename in filenames:
                yield os.path.join(parent,filename)
                #print("parent is :"+parent)
                #print("filename is :"+filename)
                #print("the full name of the file is "+os.path.join(parent,filename))
        

        
        
if __name__=="__main__":
    d=DirLooper("D:\study\pictures")
    for file in d.looper():
        print (file)
    
    
    