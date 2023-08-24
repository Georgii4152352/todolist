class Task:
    def __init__(self,title, deadline,status):
        self.title = title
        self.deadline = deadline
        self.status = status

    def get_color_day(self,cal,cd):
        day = self.deadline.day
        month = self.deadline.month
        year = self.deadline.year

        date1 = datetime.date(year,month,day) # task
        date2 = datetime.date(cd.year,cd.month,cd.day) # current
        if date2 > date1 and self.status is False:
            cal.calevent_create(self.deadline,self.title, "code_red")
            cal.tag_config("code_red",background = "red", foreground = "white")
        else:
            days = (date1 - date2).days
            if days <= 2:
                cal.calevent_create(self.deadline,self.title,"code_orange")
                cal.tag_config("code_orange", background="orange", foreground="white")
            elif days <= 4:
                cal.calevent_create(self.deadline, self.title, "code_gold")
                cal.tag_config("code_gold", background="gold", foreground="white")
            elif days >= 5:
                cal.calevent_create(self.deadline, self.title, "code_blue")
                cal.tag_config("code_blue", background="blue", foreground="white")

        if self.status is True:
            cal.calevent_create(self.deadline, self.title, "code_green")
            cal.tag_config("code_green", background="green", foreground="white")
