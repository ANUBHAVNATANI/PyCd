"""
trying to make a database using python
schema creation time 
make a er diagram before defining the schema 
the databse once made can not be changed logically
just a fun project not for any industrial use
at the start of the project i do not completely know sql or oop in python
but want to make something cool
and make a visualization software that automatically gives some sensible results
ideas change during the creation of the soft ware 
i also don't know how to structure the software development process 
so there may be some bugs or redundency
"""
"""Also try python oop for the first time"""
class enterSchema:
    def __init__(self,number=0,inputs=[]):
        self.number = number
        self.inputs = inputs
    def takeInput(self):
        a = []
        while(self.number!=1):
            a.append(input())
            if(a[-1]=="1"):
                self.number=1
                a.pop()
        self.inputs = a
    def seeCommands(self):
        for i in range(0,len(self.inputs)):
            print(str(i)+" " + self.inputs[i])
    def commandsToFile(self):
        filename = "commandsSql.txt"
        fh = open(filename,"w")
        fh.writelines(self.inputs) 
        fh.close()

#testing code
print("Enter the commands for the schema(in the MYSql syntax)")
print("If your schema design is complete then you can opt out of design module")
x = enterSchema()
x.takeInput()
x.seeCommands()
x.commandsToFile()