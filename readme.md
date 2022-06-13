<center>
<p align="center">
<image src="https://github.com/flet-dev/flet/raw/main/media/logo/flet-logo.svg" width="20%">
</p>
<h1>ตัวอย่างง่ายๆแอพจาก Flet</h1>
<p align="center">
<image src="https://img.shields.io/github/repo-size/watchakorn-18k/Simple-App-from-Flet?label=Size&style=flat-square">
<image src="https://img.shields.io/github/last-commit/watchakorn-18k/Simple-App-from-Flet?style=flat-square">
<image src="https://img.shields.io/badge/flet-v0.1.30-tomato">
</p>
</center>

<p align="center">
<image src="https://media.discordapp.net/attachments/581018943041306641/985786567203368970/chrome-capture-2022-5-13.gif" width="50%">
</p>

<p>นี่คือตัวอย่างการพัฒนาแอพพลิเคชั่น Flet ง่ายๆ ผมได้ทดลองเล่นดูแล้ว พยายามเปลี่ยนหน้าของแอพ เนื่องจากเอกสารยังไม่มีได้มีแนวทางที่ชัดเจน ผมทำได้แค่เพียง pop() ลบ container ออกไปที่ละก้อนแทน นี่อาจไม่ใช่วิธีที่ดีที่สุด แต่ก็หวังว่าอนาคตจะมีวิธีที่ดีกว่านี้</p>

# แอพหน้า index
```py
def main(page: Page):
    page.title = 'แอพ wk18k'
    #ชื่อแอพ
    page.theme = theme.Theme(color_scheme_seed="indigo")
    #สีของธีมแอพเป็นแบบ indigo
    page.theme_mode = "dark"
    #เริ่มต้นด้วยโหมดมืด
    page.horizontal_alignment = 'center'
    #จัดตำแหน่งแนวนอนของแอพให้อยู่กลางของหน้าจอ
    AppMain(page)
    #เรียกคลาส AppMain มาใช้งาน
    SwithMode(page)
    #เรียกคลาส SwithMode เพื่อเพิ่มปุ่มสลับโหมดธีมมาใช้งาน
    page.update()
    #อัพเดทหน้าจอทั้งหมด แต่ก็สามารถใช้ page.add() ได้เหมือนกัน

flet.app(target=main,port=25648,)
#เรียกใช้งานแอพจาก Flet ตัวนี้จะทำงานที่หน้าจอ สามารถเปิดใน brownser ได้ที่อยู่ที่ http://localhost:25648/
```

# สลับโหมดมืดและโหมดสว่าง
```py
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
```

# หน้าแอพหลัก

<p align="center">
<image src="https://media.discordapp.net/attachments/581018943041306641/985785921679028244/unknown.png?width=331&height=532" width="50%">
</p>

```py
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
```

# หน้าแอพลงทะเบียน

<p align="center">
<image src="https://media.discordapp.net/attachments/581018943041306641/985785951722815528/unknown.png?width=333&height=532" width="50%">
</p>


```py
class AppRegister:
    """
    หน้าลงทะเบียน
    """
    def __init__(self,page):
        self.page = page
        #สร้าง object page เพื่อเอามาใช้สร้างวิดเจ็ท
        self.page.horizontal_alignment = 'center'
        #จัดตำแหน่งแนวนอนของแอพให้อยู่กลางของหน้าจอ
        self.page.vertical_alignment = 'start'
        #จัดตำแหน่งแนวตั้งของแอพให้อยู่ส่วนบนสุด

        #สร้างฟอร์มปกติ
        self.NameInput = TextField(label='ชื่อ',hint_text='กรอกชื่อจริง',width=300)
        self.SurnameInput = TextField(label='นามสกุล',hint_text='กรอกนามสกุล',width=300)
        self.AgeInput = TextField(label='อายุ',hint_text='อายุ',width=300,keyboard_type='number',value = 0)
        self.TextHeader = Text('สมัครสมาชิก',style="displaySmall")
        self.Submit = FilledButton('ลงทะเบียน',height=50,width=200)
        self.Submit.on_click = self.submit
        self.BackMain = FilledButton('กลับหน้าหลัก',height=50,width=200)
        self.BackMain.on_click = self.back_main

        #จัดรูปแบบมาอยู่ในแบบ Container
        self.Container1 = Container(content=self.TextHeader,margin=10,)
        self.Container2 = Container(content=self.NameInput,margin=5,padding=padding.only(left=30,right=30))
        self.Container3 = Container(content=self.SurnameInput,margin=5,padding=padding.only(left=30,right=30))
        self.Container4 = Container(content=self.AgeInput,margin=5,padding=padding.only(left=30,right=30))
        self.Container5 = Container(content=self.Submit,margin=5,padding=padding.only(left=30,right=30))
        self.Container6 = Container(content=self.BackMain,margin=5,padding=padding.only(left=30,right=30))
        self.InputList = [self.Container1,self.Container2,self.Container3,self.Container4,self.Container5,self.Container6]

        #ให้วิดเจ็ทแสดงผลท
        for i in self.InputList:
            self.page.add(i)
        self.page.update()

    #method ใช้ในการกลับไปหน้าหลัก
    def back_main(self,event):
        """
        กลับไปหน้าหลัก
        """
        for i in self.InputList:
            self.page.controls.pop()
        AppMain(self.page)

     #method ใช้ในการ submit ข้อมูล
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
        #ทดสอบบันทึกเป็น json
        with open('data.json','r') as f:
            data_json = json.load(f)
        data_json.append(data)
        with open('data.json','w') as f:
            json.dump(data_json,f)
            
        # print(self.page.session_id)
        # print(self.NameInput.value)
        # print(self.SurnameInput.value)
        # print(self.AgeInput.value)
```

