import datetime
incidence = [{
    "id" : 1,
    "createdOn" : "11/02/1998",  
    "createdBy" : 30071294, 
    "type" : 'redflag',       
    "location" : 14,   
    "status" : 'draft',     
    "Images" : ['url'], 
    "Videos" : ['url'],
    "comment" : 'String'
    },
    {
    "id" : 2,
    "createdOn" : "11/02/1998",  
    "createdBy" : 24454515, 
    "type" : 'intervention',       
    "location" : 14,   
    "status" : 'resolved',     
    "Images" : ['url'], 
    "Videos" : ['url'],
    "comment" : 'String'
    }
    ]

    
class myRedflags(object):
    def __init__(self):
        self.db = incidence
        self.id = len(incidence) - 1
    def save(self,name, flag, location):
        data = {
                 "id" : self.id,
                "createdOn" : datetime.datetime.utcnow(),  
                "createdBy" : name, 
                "type" : flag,       
                "location" : location,   
                "status" : 'draft',     
                "Images" : ['url'], 
                "Videos" : ['url'],
                "comment" : 'String'
            }

        incidence.append(data)

        return incidence