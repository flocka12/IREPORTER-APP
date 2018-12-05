import datetime
incidence = []

class myRedflags():
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
        for inc in incidence:
            if inc in incidence:
                return self.db
            else:
                return "No redflags"
    def get_RedflagsById(self, id):
        for inc in incidence:
            if id == inc["id"]:
                return inc
            if id != inc["id"]:
                return "red flag " + str(id) + " does not exist"
    def delete_RedflagsById(self,id):
        for inc in incidence:
            if id == inc["id"]:
                incidence.pop(id)
                return ""
            if id != inc["id"]:
                return "red flag " + str(id) + " does not exist"

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
        if data["comment"] == "":
            return "no comment added"
        else:
            for inc in incidence:
                if id == inc["id"]:
                    incidence[id] = data
                return data



