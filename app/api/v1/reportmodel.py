import datetime
incidence = [

]

class myRedflags():
    def __init__(self):
        self.db = incidence
        self.id = len(incidence) 
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
        for inc in incidence:
            if inc in incidence:
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

    def patch_RedflagsById(self,name,id,location,comment):
        data = {
            "id" : self.id,
            "createdOn" : datetime.datetime.utcnow(),  
            "createdBy" : name, 
            "type" : 'redflag',       
            "location" : location,   
            "status" : 'draft',     
            "Images" : ['url'], 
            "Videos" : ['url'],
            "comment" : comment
                }

        for inc in incidence:
            if id == inc["id"]:
                incidence[id] = data
            return data



