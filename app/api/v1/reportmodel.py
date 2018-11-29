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
    def get_Redflags(self):
        return self.db
    def get_RedflagsById(self, id):
        for inc in incidence:
            if id == inc["id"]:
                return inc

    def delete_RedflagsById(self,id):
        for inc in incidence:
            if id == inc["id"]:
                incidence.pop(id)
                return ""

    def update(self):

        return ""



item= myRedflags()
print(item.save)