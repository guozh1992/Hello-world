class addbookentry(object):
    def __init__(self,nm,ph):
        self.name=nm
        self.phone=ph
        print 'create instance for:',self.name
    def updatePhone(self,newph):
        self.phone=newph
        print 'Update phone for:',self.name

book=addbookentry('guo','15')
print book.name
print book.phone



