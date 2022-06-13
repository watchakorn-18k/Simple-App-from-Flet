import flet
from flet import TextField, FilledButton, Text,Page,Container,padding,theme,Image,FloatingActionButton,Icon,icons,SnackBar,Theme


class AppMain:
    """
    หน้าหลัก
    """
    def __init__(self,page):
        self.page = page
        self.page.horizontal_alignment = 'center'
        self.page.vertical_alignment = 'center'
        self.TextHeaderWelcome = Text('สวัสดีสมาชิกทุกท่านด้วยนี่คือแอพทดสอบของ wk-18k',style="headlineLarge",text_align='center')
        self.BtnToRes = FilledButton('กดเพื่อลงทะเบียน',height=50,width=200)
        self.BtnToRes.on_click = self.to_res
        self.Container1 = Container(content=self.TextHeaderWelcome,margin=5,padding=padding.only(left=30,right=30))
        self.Container2 = Container(content=self.BtnToRes,margin=5,padding=padding.only(left=30,right=30))
        self.img = Image(src=f"/icons/icon-512.png",width=100,height=100,fit="contain",)
        self.WidgetList = [self.img,self.Container1,self.Container2]
        for i in self.WidgetList:
            self.page.add(i)
        self.page.update()
        
    
    def to_res(self,event):
        """
        ไปหน้าลงทะเบียน
        """
        for i in self.WidgetList:
            self.page.controls.pop()
        AppRegister(self.page)
        self.page.update()

class AppRegister:
    """
    หน้าลงทะเบียน
    """
    def __init__(self,page):
        self.page = page
        self.page.horizontal_alignment = 'center'
        self.page.vertical_alignment = 'start'
        self.NameInput = TextField(label='ชื่อ',hint_text='กรอกชื่อจริง',width=300)
        self.SurnameInput = TextField(label='นามสกุล',hint_text='กรอกนามสกุล',width=300)
        self.AgeInput = TextField(label='อายุ',hint_text='อายุ',width=300,keyboard_type='number',value = 0)
        self.TextHeader = Text('สมัครสมาชิก',style="displaySmall")
        self.Submit = FilledButton('ลงทะเบียน',height=50,width=200)
        self.Submit.on_click = self.submit
        self.BackMain = FilledButton('กลับหน้าหลัก',height=50,width=200)
        self.BackMain.on_click = self.back_main
        self.Container1 = Container(content=self.TextHeader,margin=10,)
        self.Container2 = Container(content=self.NameInput,margin=5,padding=padding.only(left=30,right=30))
        self.Container3 = Container(content=self.SurnameInput,margin=5,padding=padding.only(left=30,right=30))
        self.Container4 = Container(content=self.AgeInput,margin=5,padding=padding.only(left=30,right=30))
        self.Container5 = Container(content=self.Submit,margin=5,padding=padding.only(left=30,right=30))
        self.Container6 = Container(content=self.BackMain,margin=5,padding=padding.only(left=30,right=30))
        self.InputList = [self.Container1,self.Container2,self.Container3,self.Container4,self.Container5,self.Container6]
        for i in self.InputList:
            self.page.add(i)
        self.page.update()


    def back_main(self,event):
        """
        กลับไปหน้าหลัก
        """
        for i in self.InputList:
            self.page.controls.pop()
        AppMain(self.page)

    def submit(self,event):
        import json
        """
        ส่งข้อมูลลงฐานข้อมูล
        """
        data = {
            "id":self.page.session_id,
            "name":self.NameInput.value,
            "surname":self.SurnameInput.value,
            "age":self.AgeInput.value
        }
        with open('data.json','r') as f:
            data_json = json.load(f)
        data_json.append(data)
        with open('data.json','w') as f:
            json.dump(data_json,f)
            
        # print(self.page.session_id)
        # print(self.NameInput.value)
        # print(self.SurnameInput.value)
        # print(self.AgeInput.value)

class SwithMode:
    """
    เปลี่ยนโหมด
    """
    def __init__(self,page):
        self.page = page
        self.page.floating_action_button = FloatingActionButton("+",icon="add",content=Icon(icons.DARK_MODE))
        self.page.floating_action_button.on_click = self.switch_mode
    def switch_mode(self,e):
        """
        สลับโหมดมืด สว่าง
        """
        self.page.theme_mode="light" if self.page.theme_mode=="dark" else "dark"
        self.page.floating_action_button.content = Icon(icons.LIGHT_MODE) if self.page.theme_mode=="dark" == "dark" else Icon(icons.DARK_MODE)
        self.page.update()


    
def main(page: Page):
    page.title = 'แอพ wk18k'
    page.theme = theme.Theme(color_scheme_seed="indigo")
    page.theme_mode = "dark"
    page.horizontal_alignment = 'center'
    AppMain(page)
    SwithMode(page)

    page.update()


flet.app(target=main,port=25648,)