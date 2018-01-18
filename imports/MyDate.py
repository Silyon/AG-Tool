class MyDate:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        self.toString = str(self.day) + "." + str(self.month) + "." + str(self.year)

    def checkSeason(self, season):
        se = season.split(' ')
        change = False
        
        if self.day == '?':
            self.day = 25
            change = True
        
        for s in se:
            if s.isdigit():
                y = int(s)
            else:
                z = s
            
        if int(y) != int(self.year):
            return False

        if z == "fall":
            #can sart up to June 25
            if int(self.month) in [1,2,3,4,5,12]:
                return False
            else:
                if int(self.day) < 25 and int(self.month) == 6:
                    return False

        elif z == "summer":
            #can start up to March 25
            if int(self.month) in [1,2,9,10,11,12]:
                return False
            else:
                if int(self.day) < 25 and int(self.month) == 3:
                    return False
                
        elif z == "spring":
            #can start up to January 1st
            if int(self.month) in [7,8,9,10,11,12]:
                return False
            else:
                if int(self.day) > 25 and int(self.month) == 1:
                    return False
                
        elif z == "winter":
            #can start up to September 25
            if int(self.month) in [4,5,6,7,8]:
                return False
            else:
                if int(self.day) < 25 and int(self.month) == 9:
                    return False

        if change == True:
            self.day = '?'
            change = False
        
        return True
