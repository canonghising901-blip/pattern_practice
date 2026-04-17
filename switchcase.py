class Solution:
    def whichWeekDay(self, day):
        # match day:
        #     case 1:
        #         return "Monday"
        #     case 2:
        #         return "Tuesday"
        #     case 3:
        #         return "Wednesday"
        #     case 4:
        #         return "Thursday"
        #     case 5:
        #         return "Friday"
        #     case 6:
        #         return "Saturday"
        #     case 7:
        #         return "Sunday"
        #     case 8:

        #         return "Invalid"
        switch={
            1:"Monday",
            2:"Tuesday",
            3:"Wednesday",
            4:"Thursday",
            5:"Friday",
            6:"Saturday",
            7:"Sunday"
        }
        return switch.get(day,"Invalid")
d1=Solution()
print(d1.whichWeekDay(1))