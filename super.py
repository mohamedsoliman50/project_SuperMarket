from tkinter import *
import math ,random,os
from tkinter import messagebox,Tk,Frame,Text,Scrollbar,Y,BOTH
class super :
    def __init__(self,root):
        self.root = root
        self.root.geometry("1200x620+30+10")
        self.root.title("SuperMarket : سوبر ماركت")
        self.root.resizable(False,False)
        self.root.iconbitmap("C:\\Users\\HP\\Downloads\\project shop\\super_logo.ico")
        title = Label(self.root,text ="project management : SuperMarket",fg="white",bg="#0B2F3A",font =("tajawal",15,"bold"))
        title.pack(fill = X)
        # variable  bacoliat 
        self.q1 = IntVar()
        self.q2 = IntVar()
        self.q3 = IntVar()
        self.q4 = IntVar()
        self.q5 = IntVar()
        self.q6 = IntVar()
        self.q7 = IntVar()
        self.q8 = IntVar()
        self.q9 = IntVar()
        self.q10 = IntVar()
        self.q11 = IntVar()
        self.q12 = IntVar()
        self.q13 = IntVar()
        self.q14 = IntVar()
        self.q15 = IntVar()
        self.q16 = IntVar()
        self.q17 = IntVar()
        self.q18 = IntVar()
        self.q19 = IntVar()
        self.q20 = IntVar()
        
        # variable dariy 
        self.qq1 = IntVar()
        self.qq2 = IntVar()
        self.qq3 = IntVar()
        self.qq4 = IntVar()
        self.qq5 = IntVar()
        self.qq6 = IntVar()
        self.qq7 = IntVar()
       
        #variable adoat 
        self.qqq1 = IntVar()
        self.qqq2 = IntVar()
        self.qqq3 = IntVar()
        self.qqq4 = IntVar()
        self.qqq5 = IntVar()
        self.qqq6 = IntVar()
        self.qqq7 = IntVar()
        self.qqq8 = IntVar()
        self.qqq9 = IntVar()
        self.qqq10 = IntVar()
        self.qqq11 = IntVar()
        self.qqq12 = IntVar()
        self.qqq13 = IntVar()
        self.qqq14 = IntVar()
        self.qqq15 = IntVar()
        self.qqq16 = IntVar()
        self.qqq17 = IntVar()
        self.qqq18 = IntVar()

         # variable drinks 
        self.qqqq1 = IntVar()
        self.qqqq2 = IntVar()
        self.qqqq3 = IntVar()
        self.qqqq4 = IntVar()
        self.qqqq5 = IntVar()
        self.qqqq6 = IntVar()
        self.qqqq7 = IntVar()
        self.qqqq8 = IntVar()

       # variable kahraba 
        self.qqqqq1 = IntVar()
        self.qqqqq2 = IntVar()
        self.qqqqq3 = IntVar()
        self.qqqqq4 = IntVar()
        self.qqqqq5 = IntVar()
        self.qqqqq6 = IntVar()
        self.qqqqq7 = IntVar()
        self.qqqqq8 = IntVar()
        self.qqqqq9 = IntVar()
        self.qqqqq10 = IntVar()
        self.qqqqq11 = IntVar()
       
        # variable customer 
        self.namo = StringVar()
        self.phono = StringVar()
        self.fatora = StringVar()
        invoice3= random.randint(1000,9999)
        self.fatora.set(str(invoice3))
        # Total account variables
        self.bacoliat =StringVar()
        self.adoat =StringVar()
        self.kahraba =StringVar()
        self.dariy =StringVar()
        self.drinks = StringVar()
        

        # Customer Data
        
        F1 = Frame(root,bd= 3,width =340 ,height=170,bg="#0B4C5F")
        F1.place(x=859 ,y=31 )
        tit = Label(F1,text =":بيانات المشتري",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="tomato")
        tit.place(x=217 ,y= 0)
        his_name = Label(F1,text="اسم المشتري",font=("tajawal",12,"bold"),bg="#0B4C5F",fg ="white")
        his_name.place(x=245 ,y=36 )

        his_phone = Label(F1,text="رقم التليفون",font=("tajawal",12,"bold"),bg="#0B4C5F",fg ="white")
        his_phone.place(x=250 ,y=66 )

        bill_num = Label(F1,text="رقم الفاتورة",font=("tajawal",12,"bold"),bg="#0B4C5F",fg ="white")
        bill_num.place(x=255 ,y=96)
        # create Label name
        Ent_name = Entry(F1,textvariable=self.namo,justify="center")
        Ent_name.place(x=115 ,y=42)
        # create Label phone
        Ent_phone = Entry(F1,textvariable=self.phono,justify="center")
        Ent_phone.place(x=115 ,y=72)
        # create Label bill
        Ent_bill = Entry(F1 ,textvariable=self.fatora,justify="center")
        Ent_bill.place(x=115 ,y=102)
        # create Button 
        btn_customer = Button(F1,text="بحث",font=("tajawal",11),width= 10,height =4,bg="white")
        btn_customer.place(x=3 ,y=41 )

        # Fatora :bill 
        title_invoice =Label(F1, text="[الفواتير]",font=("tajawal",16,"bold"),bg="#0B4C5F",fg="gold")
        title_invoice.place(x=125 ,y =135 )

        # create Frame2()
        F2 = Frame(root,bd=2,width=250 ,height= 380 ,bg= "white")
        F2.place(x =860 ,y =203 )
        scroll_y = Scrollbar(F2,orient=VERTICAL)
        self.textarea = Text(F2,yscrollcommand= scroll_y.set)
        scroll_y.pack(side=LEFT ,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH ,expand=1)
        

        # create itme 1  
        F4 = Frame(root,bd=3,width= 300,height= 665,bg="#0B4C5F")
        F4.place(x= 1, y= 35)
        title_1 = Label(F4,text="قسم البقوليات",font= ("tajawal",15,"bold"),bg="#0B4C5F",fg="gold")
        title_1.place(x =113, y=0 )
        bq1 = Label(F4,text="الرز ",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        bq1.place(x=263 ,y=50 )
        bq2 = Label(F4,text="فاصوليا",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        bq2.place(x=240 ,y=80 )
        bq3 = Label(F4,text="مكرونة",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        bq3.place(x=243 ,y=110 )
        bq4 = Label(F4,text="العدس",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        bq4.place(x=251 ,y=140 )
        bq5 = Label(F4,text="الفول",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        bq5.place(x=255 ,y=170 )
        bq6 = Label(F4,text="الحمص",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        bq6.place(x=243 ,y=200 )
        bq7 = Label(F4,text="الملح",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        bq7.place(x=256 ,y=230 )
        bq8 = Label(F4,text="الترمس",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        bq8.place(x=243 ,y=260 )
        bq9 = Label(F4,text="البازلاء",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        bq9.place(x=244 ,y=290 )
        bq10 = Label(F4,text="البن",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        bq10.place(x=263 ,y=320 )
        bq11 = Label(F4,text="لوبيا",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        bq11.place(x=259 ,y=350 )
        bq12 = Label(F4,text="  سكر",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        bq12.place(x=100 ,y=50 )
        bq13 = Label(F4,text="  شعرية",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        bq13.place(x=95 ,y=80 )
        bq14 = Label(F4,text="فلفل اسود",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        bq14.place(x=85 ,y=110 )
        bq15 = Label(F4,text="فلفل احمر",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        bq15.place(x=85 ,y=140 )
        bq16 = Label(F4,text=" القمح",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        bq16.place(x=95 ,y=170 )
        bq17 = Label(F4,text="الشعير",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        bq17.place(x=95 ,y=200 )
        bq18 = Label(F4,text="الشوفان",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        bq18.place(x=95 ,y=230 )
        bq19 = Label(F4,text="الذره",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        bq19.place(x=96 ,y=260)
        bq20 = Label(F4,text=" زيت",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        bq20.place(x=96 ,y=290 )
        # create Entry to items
        bqent1 = Entry(F4,textvariable=self.q1,width=12)
        bqent1.place(x=160  ,y=55 )
        bqent2 = Entry(F4,textvariable=self.q2,width=12)
        bqent2.place(x=160  ,y=85 )
        bqent3 = Entry(F4,textvariable=self.q3,width=12)
        bqent3.place(x=160  ,y=115 )
        bqent4 = Entry(F4,textvariable=self.q4,width=12)
        bqent4.place(x=160  ,y=145 )
        bqent5 = Entry(F4,textvariable=self.q5,width=12)
        bqent5.place(x=160  ,y=175 )
        bqent6 = Entry(F4,textvariable=self.q6,width=12)
        bqent6.place(x=160  ,y=205 )
        bqent7 = Entry(F4,textvariable=self.q7,width=12)
        bqent7.place(x=160  ,y=235 )
        bqent8 = Entry(F4,textvariable=self.q8,width=12)
        bqent8.place(x=160  ,y=265 )
        bqent9 = Entry(F4,textvariable=self.q9,width=12)
        bqent9.place(x=160 ,y=295 )
        bqent10 = Entry(F4,textvariable=self.q10,width=12)
        bqent10.place(x=160  ,y=325 )
        bqent11 = Entry(F4,textvariable=self.q11,width=12)
        bqent11.place(x=160 ,y=355 )
        bqent12 = Entry(F4,textvariable=self.q12,width=12)
        bqent12.place(x=1  ,y=55 )
        bqent13 = Entry(F4,textvariable=self.q13,width=12)
        bqent13.place(x=1  ,y=85 )
        bqent14 = Entry(F4,textvariable=self.q14,width=12)
        bqent14.place(x=1  ,y=115 )
        bqent15 = Entry(F4,textvariable=self.q15,width=12)
        bqent15.place(x=1  ,y=145 )
        bqent16 = Entry(F4,textvariable=self.q16,width=12)
        bqent16.place(x=1  ,y=175 )
        bqent17= Entry(F4,textvariable=self.q17,width=12)
        bqent17.place(x=1  ,y=205 )
        bqent18 = Entry(F4,textvariable=self.q18,width=12)
        bqent18.place(x=1  ,y=235 )
        bqent19 = Entry(F4,textvariable=self.q19,width=12)
        bqent19.place(x=1 ,y=265 )
        bqent20 = Entry(F4,textvariable=self.q20,width=12)
        bqent20.place(x=1 ,y=295 )

        # create department Dairy 
        title_2 = Label(F4,text="قسم الالبان",font= ("tajawal",15,"bold"),bg="#0B4C5F",fg="gold")
        title_2.place(x =115, y=415 )

        Dairy1 = Label(F4,text="الحليب",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        Dairy1.place(x=249 ,y=440 )
        Dairy2 = Label(F4,text=" الزبادي الفواكه",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        Dairy2.place(x=198 ,y=470 )
        Dairy3 = Label(F4,text="زبادي عادي",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        Dairy3.place(x=215 ,y=500 )
        Dairy4= Label(F4,text="القشطه",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        Dairy4.place(x=247,y=530 )
        Dairy5= Label(F4,text="زبده",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        Dairy5.place(x=263 ,y=555 )
        Dairy6= Label(F4,text="الجبنة",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        Dairy6.place(x=65 ,y=440 )
        Dairy7= Label(F4,text="جبنة رومي",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        Dairy7.place(x=55 ,y=465 )

        # create Label items

        Darity_ent1 = Entry(F4,textvariable=self.qq1,width=8)
        Darity_ent1.place(x=150 ,y=445 )
        Darity_ent2 = Entry(F4,textvariable=self.qq2,width=8)
        Darity_ent2.place(x=150 ,y=475 )
        Darity_ent3 = Entry(F4,textvariable=self.qq3,width=8)
        Darity_ent3.place(x=150 ,y=505 )
        Darity_ent4 = Entry(F4,textvariable=self.qq4,width=8)
        Darity_ent4.place(x=150 ,y=535 )
        Darity_ent5 = Entry(F4,textvariable=self.qq5,width=8)
        Darity_ent5.place(x=150 ,y=565 )
        Darity_ent6 = Entry(F4,textvariable=self.qq6,width=8)
        Darity_ent6.place(x=1 ,y=445 )
        Darity_ent7 = Entry(F4,textvariable=self.qq7,width=8)
        Darity_ent7.place(x=1 ,y=475 )

        # create Items 2 
        F5 = Frame(root,bd=3,width=305 ,height=665 ,bg ="#0B4C5F")
        F5.place(x=303,y=35)
        # create department house
        title1 = Label(F5,text="قسم الادوات المنزليه",font= ("tajawal",15,"bold"),bg="#0B4C5F",fg="gold")
        title1.place(x =70, y=0 )
        a_tool1 = Label(F5,text="مصفاة",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        a_tool1.place(x=255 ,y=50 )

        a_tool2 = Label(F5,text="صحن",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        a_tool2.place(x=259 ,y=80 )

        a_tool3 = Label(F5,text="كأس",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        a_tool3.place(x=262 ,y=110 )

        a_tool4 = Label(F5,text="ابريق",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        a_tool4.place(x=260 ,y=140 )

        a_tool5 = Label(F5,text="سكين",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        a_tool5.place(x=260 ,y=170 )

        a_tool6 = Label(F5,text="شوك",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        a_tool6.place(x=261 ,y=200 )

        a_tool7 = Label(F5,text="مبشره",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        a_tool7.place(x=254 ,y=230 )

        a_tool8 = Label(F5,text="ملاعق",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        a_tool8.place(x=255 ,y=260 )

        a_tool9 = Label(F5,text="مقص",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        a_tool9.place(x=254 ,y=290 )

        a_tool10 = Label(F5,text="وعاء الخلاط",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        a_tool10.place(x=80 ,y=50)

        a_tool11 = Label(F5,text="مقشره",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        a_tool11.place(x=113 ,y=80 )

        a_tool12 = Label(F5,text="فتاحه علب",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        a_tool12.place(x=94 ,y=110 )

        a_tool13 = Label(F5,text="لوح التقطيع",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        a_tool13.place(x=88 ,y=140 )

        a_tool14 = Label(F5,text="حفارة",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        a_tool14.place(x=116 ,y=170 )

        a_tool15 = Label(F5,text="سله قمامة",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        a_tool15.place(x=95 ,y=200 )

        a_tool16 = Label(F5,text="منفضة",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        a_tool16.place(x=113 ,y=230 )

        a_tool17 = Label(F5,text="اكياس",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        a_tool17.place(x=113 ,y=260 )

        a_tool18 = Label(F5,text="مضارب بيض",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        a_tool18.place(x=85 ,y=290 )
        # create Entry Label items
        atool_ent1 = Entry(F5,textvariable=self.qqq1,width=9)
        atool_ent1.place(x=180 ,y=55 )
        atool_ent2 = Entry(F5,textvariable=self.qqq2,width=9)
        atool_ent2.place(x=180 ,y=85 )
        atool_ent3 = Entry(F5,textvariable=self.qqq3,width=9)
        atool_ent3.place(x=180 ,y=115 )
        atool_ent4 = Entry(F5,textvariable=self.qqq4,width=9)
        atool_ent4.place(x=180 ,y=145 )
        atool_ent5 = Entry(F5,textvariable=self.qqq5,width=9)
        atool_ent5.place(x=180 ,y=175 )
        atool_ent6 = Entry(F5,textvariable=self.qqq6,width=9)
        atool_ent6.place(x=180 ,y=205 )
        atool_ent7 = Entry(F5,textvariable=self.qqq7,width=9)
        atool_ent7.place(x=180 ,y=235 )
        atool_ent8 = Entry(F5,textvariable=self.qqq8,width=9)
        atool_ent8.place(x=180 ,y=265 )
        atool_ent9 = Entry(F5,textvariable=self.qqq9,width=9)
        atool_ent9.place(x=180 ,y=295 )
        atool_ent10 = Entry(F5,textvariable=self.qqq10,width=9)
        atool_ent10.place(x=1 ,y=55 )
        atool_ent11 = Entry(F5,textvariable=self.qqq11,width=9)
        atool_ent11.place(x=1,y=85 )
        atool_ent12 = Entry(F5,textvariable=self.qqq12,width=9)
        atool_ent12.place(x=1 ,y=115 )
        atool_ent13 = Entry(F5,textvariable=self.qqq13,width=9)
        atool_ent13.place(x=1 ,y=145 )
        atool_ent14 = Entry(F5,textvariable=self.qqq14,width=9)
        atool_ent14.place(x=1 ,y=175)
        atool_ent15 = Entry(F5,textvariable=self.qqq15,width=9)
        atool_ent15.place(x=1 ,y=205 )
        atool_ent16 = Entry(F5,textvariable=self.qqq16,width=9)
        atool_ent16.place(x=1 ,y=235 )
        atool_ent17 = Entry(F5,textvariable=self.qqq17,width=9)
        atool_ent17.place(x=1 ,y=265 )
        atool_ent18 = Entry(F5,textvariable=self.qqq18,width=9)
        atool_ent18.place(x=1 ,y=295 )
     
        # create department drinks
        title2 = Label(F5,text="قسم المشروبات",font= ("tajawal",15,"bold"),bg="#0B4C5F",fg="gold")
        title2.place(x =70, y=360 )

        drink1 = Label(F5,text="مشروبات غازية",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        drink1.place(x=190 ,y=390 )

        drink2 = Label(F5,text="الماه المعدنية",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        drink2.place(x=210 ,y=420 )

        drink3 = Label(F5,text="الشاي",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        drink3.place(x=255 ,y=450 )

        drink4 = Label(F5,text="كاكاو",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        drink4.place(x=259 ,y=480 )

        drink5 = Label(F5,text="السحلب",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        drink5.place(x=249 ,y=510 )

        drink6 = Label(F5,text="العصائر",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        drink6.place(x=249 ,y=540 )

        drink7 = Label(F5,text="النعناع",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        drink7.place(x=65 ,y= 390 )

        drink8 = Label(F5,text="الينسون",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        drink8.place(x=65 ,y=420 )

        # create Entry Label items 
        drink_ent1 = Entry(F5,textvariable=self.qqqq1,width=8)
        drink_ent1.place(x=130 ,y=395 )

        drink_ent2 = Entry(F5,textvariable=self.qqqq2,width=8)
        drink_ent2.place(x=130 ,y=425 )

        drink_ent3 = Entry(F5,textvariable=self.qqqq3,width=8)
        drink_ent3.place(x=130 ,y=455 )

        drink_ent4 = Entry(F5,textvariable=self.qqqq4,width=8)
        drink_ent4.place(x=130,y=485 )

        drink_ent5 = Entry(F5,textvariable=self.qqqq5,width=8)
        drink_ent5.place(x= 130,y=515 )

        drink_ent6 = Entry(F5,textvariable=self.qqqq6,width=8)
        drink_ent6.place(x=130 ,y=545 )

        drink_ent7 = Entry(F5,textvariable=self.qqqq7,width=8)
        drink_ent7.place(x=1 ,y=395 )

        drink_ent8 = Entry(F5,textvariable=self.qqqq8,width=8)
        drink_ent8.place(x=1 ,y= 425)
        
        # create item 3
        F6 = Frame(root,bd=3,width=247 ,height=665 ,bg ="#0B4C5F")
        F6.place(x=610,y=35)
        title = Label(F6,text="قسم ادوات الكهرباء",font= ("tajawal",15,"bold"),bg="#0B4C5F",fg="gold")
        title.place(x =60, y=5 )

        atools1 = Label(F6,text="مكنسه",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        atools1.place(x=190 ,y=35 )

        atools2 = Label(F6,text="تليفزيون",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        atools2.place(x=180 ,y=65)

        atools3 = Label(F6,text="غساله",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        atools3.place(x=193 ,y=95 )

        atools4 = Label(F6,text="مكرويف",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        atools4.place(x=182 ,y=125 )

        atools5 = Label(F6,text="خلاط",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        atools5.place(x=200 ,y=155 )

        atools6 = Label(F6,text="فرن غاز",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        atools6.place(x=180 ,y=185 )

        atools7 = Label(F6,text="مروحة",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        atools7.place(x=188 ,y=215)

        atools8 = Label(F6,text="فلتر ماء",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        atools8.place(x=180 ,y=245 )

        atools9 = Label(F6,text="مكواة",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        atools9.place(x=192 ,y=275 )

        atools10= Label(F6,text="تكيف",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        atools10.place(x=193 ,y=305 )

        atools11 = Label(F6,text="للابتوب",font= ("tajawal",14,"bold"),bg="#0B4C5F",fg="white")
        atools11.place(x=183 ,y=335 )

        label_o1 = Label(F6,text="الحساب الكلي للبقوليات",font= ("tajawal",11,"bold"),bg= "#0B4C5F",fg= "gold")
        label_o1.place(x =120 ,y =370)

        label_o2 = Label(F6,text="  حساب اللوازم المنزليه",font= ("tajawal",11,"bold"),bg= "#0B4C5F",fg= "gold")
        label_o2.place(x =120 ,y =400)

        label_o3 = Label(F6,text="  حساب ادوات الكهرباء",font= ("tajawal",11,"bold"),bg= "#0B4C5F",fg= "gold")
        label_o3.place(x =120 ,y =430)

        label_o4 = Label(F6,text="  حساب قسم الالبان",font= ("tajawal",11,"bold"),bg= "#0B4C5F",fg= "gold")
        label_o4.place(x =140 ,y =460)

        label_o4 = Label(F6,text="  حساب قسم المشروبات",font= ("tajawal",11,"bold"),bg= "#0B4C5F",fg= "gold")
        label_o4.place(x =120 ,y =490)

        account = Button(F6,text="الحساب",width= 8,height= 1,font =("tajawal",12,"bold"),bg="#DBA901",command=self.total)
        account.place(x=175 ,y=520)

        # create invoice 
        invoice = Button(F6,text="تصدير الفاتورة",width =8,height=1,font =("tajawal",12,"bold"),bg="#DBA901",command=self.billing)
        invoice.place(x =90 ,y =520 )
        
        # create button clear 
        clear = Button(F6,text="افراغ الحقول",width= 8,height= 1,font =("tajawal",12,"bold"),bg="#DBA901",command=self.clear)
        clear.place(x= 1 ,y=520 )
        # create button exit program 
        exit = Button(F6,text="اغلاق البرنامج" ,width= 8,height= 1,font =("tajawal",13,"bold"),bg="#DBA901",command=self.close)
        exit.place(x= 90 ,y=553 )


    
        # Create Entry
        Ento1 = Entry(F6,textvariable=self.bacoliat,width=17)
        Ento1.place(x=9 ,y=370 )
        Ento2 = Entry(F6,textvariable=self.adoat,width=17)
        Ento2.place(x=9 ,y=400 )
        Ento3 = Entry(F6,textvariable=self.kahraba,width=17)
        Ento3.place(x=9 ,y=430)
        Ento4 = Entry(F6,textvariable=self.dariy,width=17)
        Ento4.place(x=9 ,y=460 )
        Ento5 = Entry(F6,textvariable=self.dariy,width=17)
        Ento5.place(x=9 ,y=490 )
    

        # create Entry Label 
        atools1_ent = Entry(F6,textvariable=self.qqqqq1,width=10)
        atools1_ent.place(x=100 ,y=40 )
        atools2_ent = Entry(F6,textvariable=self.qqqqq2,width=10)
        atools2_ent.place(x=100 ,y=70 )
        atools3_ent = Entry(F6,textvariable=self.qqqqq3,width=10)
        atools3_ent.place(x=100 ,y=100 )
        atools4_ent = Entry(F6,textvariable=self.qqqqq4,width=10)
        atools4_ent.place(x=100 ,y=130 )
        atools5_ent = Entry(F6,textvariable=self.qqqqq5,width=10)
        atools5_ent.place(x=100 ,y=160 )
        atools6_ent = Entry(F6,textvariable=self.qqqqq6,width=10)
        atools6_ent.place(x=100 ,y=190 )
        atools7_ent = Entry(F6,textvariable=self.qqqqq7,width=10)
        atools7_ent.place(x=100 ,y=220 )
        atools8_ent = Entry(F6,textvariable=self.qqqqq8,width=10)
        atools8_ent.place(x=100 ,y=250 )
        atools9_ent = Entry(F6,textvariable=self.qqqqq9,width=10)
        atools9_ent.place(x=100 ,y=280 )
        atools10_ent = Entry(F6,textvariable=self.qqqqq10,width=10)
        atools10_ent.place(x=100 ,y=310 )
        atools11_ent = Entry(F6,textvariable=self.qqqqq11,width=10)
        atools11_ent.place(x=100 ,y=340 )
        self.welcome()
    
    def total(self):
        # create price bacoliat
        self.bacoliat1  = self.q1.get()*1.5
        self.bacoliat2  = self.q2.get()*1.5
        self.bacoliat3  = self.q3.get()*2
        self.bacoliat4  = self.q4.get()*1.5
        self.bacoliat5  = self.q5.get()*2
        self.bacoliat6  = self.q6.get()*1.5
        self.bacoliat7  = self.q7.get()*1
        self.bacoliat8  = self.q8.get()*1.7
        self.bacoliat9  = self.q9.get()*2
        self.bacoliat10 = self.q10.get()*2
        self.bacoliat11 = self.q11.get()*2
        self.bacoliat12 = self.q12.get()*2
        self.bacoliat13 = self.q13.get()*1.5
        self.bacoliat14 = self.q14.get()*1.7
        self.bacoliat15 = self.q15.get()*2
        self.bacoliat16 = self.q16.get()*2.3
        self.bacoliat17 = self.q17.get()*1.8
        self.bacoliat18 = self.q18.get()*2
        self.bacoliat19 = self.q18.get()*5
        self.bacoliat20 = self.q20.get()*3

        self.bacoliat_total = float(
            self.bacoliat1 + 
            self.bacoliat2 + 
            self.bacoliat3 + 
            self.bacoliat4 + 
            self.bacoliat5 + 
            self.bacoliat6 + 
            self.bacoliat7 + 
            self.bacoliat8 + 
            self.bacoliat9 + 
            self.bacoliat10 + 
            self.bacoliat11 + 
            self.bacoliat12 + 
            self.bacoliat13 + 
            self.bacoliat14 + 
            self.bacoliat15 + 
            self.bacoliat16 + 
            self.bacoliat17 + 
            self.bacoliat18 + 
            self.bacoliat20 


        )
        self.bacoliat.set(str(self.bacoliat_total) +"$")

        # create price dariy 
        self.dariy1 = self.qq1.get()*20
        self.dariy2 = self.qq2.get()*2
        self.dariy3 = self.qq3.get()*2
        self.dariy4 = self.qq4.get()*3.5
        self.dariy5 = self.qq5.get()*5
        self.dariy6 = self.qq6.get()*3.5
        self.dariy7 = self.qq7.get()*2.5

        self.dariy_total = float(
            self.dariy1 +
            self.dariy2+
            self.dariy3 +
            self.dariy4 +
            self.dariy4 +
            self.dariy5 +
            self.dariy6 +
            self.dariy7
        )

        self.dariy.set(str(self.dariy_total)+"$")

        # creat price adoat  
        self.adoat1 = self.qqq1.get()*10
        self.adoat2 = self.qqq2.get()*5
        self.adoat3 = self.qqq3.get()*540
        self.adoat4 = self.qqq4.get()*18
        self.adoat5 = self.qqq5.get()*50
        self.adoat6 = self.qqq6.get()*30
        self.adoat7 = self.qqq7.get()*40
        self.adoat8 = self.qqq8.get()*70
        self.adoat9 = self.qqq9.get()*100
        self.adoat10 = self.qqq10.get()*200
        self.adoat11 = self.qqq11.get()*50
        self.adoat12= self.qqq12.get()*50
        self.adoat13 = self.qqq13.get()*50
        self.adoat14 = self.qqq14.get()*50
        self.adoat15 = self.qqq15.get()*50
        self.adoat16 = self.qqq16.get()*50
        self.adoat17 = self.qqq17.get()*50
        self.adoat18 = self.qqq18.get()*600

        self.adoat_total = float(
            self.adoat1 +
            self.adoat2 +
            self.adoat3 +
            self.adoat4 +
            self.adoat5 +
            self.adoat6 +
            self.adoat7 +
            self.adoat8 +
            self.adoat9 +
            self.adoat10 +
            self.adoat11 +
            self.adoat12 +
            self.adoat13 +
            self.adoat14 +
            self.adoat15 +
            self.adoat16 +
            self.adoat17 +
            self.adoat18 
            )
        self.adoat.set(str(self.adoat_total)+"$")

        # create price drinks 
        self.drink1 =self.qqqq1.get()*15
        self.drink2 =self.qqqq2.get()*10
        self.drink3 =self.qqqq3.get()*50
        self.drink4 =self.qqqq4.get()*30
        self.drink5 =self.qqqq5.get()*25
        self.drink6 =self.qqqq6.get()*20
        self.drink7 =self.qqqq7.get()*20.5
        self.drink8 =self.qqqq8.get()*20.5
        
        self.drink_total = float(
            self.drink1 +
            self.drink2 +
            self.drink3 +
            self.drink4 +
            self.drink5 +
            self.drink6 +
            self.drink7 +
            self.drink8 
        )
        self.drinks.set(str(self.drink_total)+"$")

        # create price kahraba
        self.atool1 = self.qqqqq1.get()*100
        self.atool2 = self.qqqqq2.get()*10000
        self.atool3 = self.qqqqq3.get()*7000
        self.atool4 = self.qqqqq4.get()*9500
        self.atool5 = self.qqqqq5.get()*2500
        self.atool6 = self.qqqqq6.get()*3500
        self.atool7 = self.qqqqq7.get()*1200
        self.atool8 = self.qqqqq8.get()*2500
        self.atool9 = self.qqqqq9.get()*500
        self.atool10 = self.qqqqq10.get()*10000
        self.atool11 = self.qqqqq11.get()*15000

        self.atool_total = float(
            self.atool1 +
            self.atool2 +
            self.atool3 +
            self.atool4 +
            self.atool5 +
            self.atool6 +
            self.atool7 +
            self.atool8 +
            self.atool9 +
            self.atool10 +
            self.atool11
        )
        self.kahraba.set(str(self.atool_total)+"$")


        # add all product 
        self.all = float(
            self.bacoliat_total +
            self.dariy_total +
            self.adoat_total +
            self.drink_total +
            self.atool_total
        )
 
    def welcome(self):
        self.textarea.delete("1.0",END)
        self.textarea.insert(END,"\t Welcome To SuperMarket")
        self.textarea.insert(END,"\n===============================")
        self.textarea.insert(END,f"\n\t B.Num  :{self.fatora.get()}")
        self.textarea.insert(END,f"\n\t Name   :{self.namo.get()}")
        self.textarea.insert(END,f"\n\t Phone  :{self.phono.get()}")
        self.textarea.insert(END,"\n ===============================")
        self.textarea.insert(END,f"\n السعر\t         العدد\t        المشتريات")
        self.textarea.insert(END,"\n ===============================")
    def clear(self):
        self.q1.set(0)
        self.q2.set(0)
        self.q3.set(0)
        self.q4.set(0)
        self.q5.set(0)
        self.q6.set(0)
        self.q7.set(0)
        self.q8.set(0)
        self.q9.set(0)
        self.q10.set(0)
        self.q11.set(0)
        self.q12.set(0)
        self.q13.set(0)
        self.q14.set(0)
        self.q15.set(0)
        self.q16.set(0)
        self.q17.set(0)
        self.q18.set(0)
        self.q19.set(0)
        self.q20.set(0)

        self.qq1.set(0)
        self.qq2.set(0)
        self.qq3.set(0)
        self.qq4.set(0)
        self.qq5.set(0)
        self.qq6.set(0)
        self.qq7.set(0)
        
        self.qqq1.set(0)
        self.qqq2.set(0)
        self.qqq3.set(0)
        self.qqq4.set(0)
        self.qqq5.set(0)
        self.qqq6.set(0)
        self.qqq7.set(0)
        self.qqq8.set(0)
        self.qqq9.set(0)
        self.qqq10.set(0)
        self.qqq11.set(0)
        self.qqq12.set(0)
        self.qqq13.set(0)
        self.qqq14.set(0)
        self.qqq15.set(0)
        self.qqq16.set(0)
        self.qqq17.set(0)
        self.qqq18.set(0)
        
        self.qqqq1.set(0)
        self.qqqq2.set(0)
        self.qqqq3.set(0)
        self.qqqq4.set(0)
        self.qqqq5.set(0)
        self.qqqq6.set(0)
        self.qqqq7.set(0)
        self.qqqq8.set(0)

        self.qqqqq1.set(0)
        self.qqqqq2.set(0)
        self.qqqqq3.set(0)
        self.qqqqq4.set(0)
        self.qqqqq5.set(0)
        self.qqqqq6.set(0)
        self.qqqqq7.set(0)
        self.qqqqq8.set(0)
        self.qqqqq9.set(0)
        self.qqqqq10.set(0)
        self.qqqqq11.set(0)

        self.bacoliat.set(0)
        self.dariy.set(0)
        self.adoat.set(0)
        self.drinks.set(0)
        self.kahraba.set(0)

        self.namo.set("")
        self.phono.set("")
        self.fatora.set("")
       
    
    def close(self):
        self.root.destroy()

    def save(self):
        ob = messagebox.askyesno("حفظ"," هل تريد حفظ الفاتورة؟")
        if ob > 0 :
            self.text =self.textarea.get("1.0",END,)
            file = open("C:\\Users\\HP\\Downloads\\project shop\\buy"+str(self.fatora.get())+".txt","w",encoding="utf-8")
            file.write(self.text)
            file.close()
        else :
            return 
        
    def billing(self):
        if self.namo.get() =="" or self.phono.get() =="":
            messagebox.showerror("حدث خطأ","لا يجوز ترك حقل الاسم او رقم التليفون فارغا")
        elif self.bacoliat.get()=="0$" and self.dariy.get()=="0$"and self.adoat.get()=="0$"and self.drinks.get()=="0$" and self.kahraba.get()=="0$":
            messagebox.showerror("حدث خطأ","ليس هناك منتجات محددة")
        else :
            self.welcome()
            if self.q1.get() !=0:
                self.textarea.insert(END,f"\n {self.bacoliat1}\t\t{self.q1.get()}\t\tالرز")
            if self.q2.get() !=0:
                self.textarea.insert(END,f"\n {self.bacoliat2}\t\t{self.q2.get()}\t\tفاصوليا")
            if self.q3.get() !=0:
                self.textarea.insert(END,f"\n {self.bacoliat3}\t\t{self.q3.get()}\t\tمكرونة")
            if self.q4.get() !=0:
                self.textarea.insert(END,f"\n {self.bacoliat4}\t\t{self.q4.get()}\t\tالعدس")
            if self.q5.get() !=0:
                self.textarea.insert(END,f"\n {self.bacoliat5}\t\t{self.q5.get()}\t\tالفول")
            if self.q6.get() !=0:
                self.textarea.insert(END,f"\n {self.bacoliat6}\t\t{self.q6.get()}\t\tالحمص")
            if self.q7.get() !=0:
                self.textarea.insert(END,f"\n {self.bacoliat7}\t\t{self.q7.get()}\t\tالملح")
            if self.q8.get() !=0:
                self.textarea.insert(END,f"\n {self.bacoliat8}\t\t{self.q8.get()}\t\tالترمس")
            if self.q9.get() !=0:
                self.textarea.insert(END,f"\n {self.bacoliat9}\t\t{self.q9.get()}\t\tالبازلاء")
            if self.q10.get() !=0:
                self.textarea.insert(END,f"\n {self.bacoliat10}\t\t{self.q10.get()}\t\tالبن")
            if self.q11.get() !=0:
                self.textarea.insert(END,f"\n {self.bacoliat11}\t\t{self.q11.get()}\t\tلوبيا")
            if self.q12.get() !=0:
                self.textarea.insert(END,f"\n {self.bacoliat12}\t\t{self.q12.get()}\t\tسكر")
            if self.q13.get() !=0:
                self.textarea.insert(END,f"\n {self.bacoliat13}\t\t{self.q13.get()}\t\tشعرية")
            if self.q14.get() !=0:
                self.textarea.insert(END,f"\n {self.bacoliat14}\t\t{self.q14.get()}\t\tفلفل اسود")
            if self.q15.get() !=0:
                self.textarea.insert(END,f"\n {self.bacoliat15}\t\t{self.q15.get()}\t\tفلفل احمر")
            if self.q16.get() !=0:
                self.textarea.insert(END,f"\n {self.bacoliat16}\t\t{self.q16.get()}\t\tالقمح")
            if self.q17.get() !=0:
                self.textarea.insert(END,f"\n {self.bacoliat17}\t\t{self.q17.get()}\t\tالشعير")
            if self.q18.get() !=0:
                self.textarea.insert(END,f"\n {self.bacoliat18}\t\t{self.q18.get()}\t\tالشوفان")
            if self.q19.get() !=0:
                self.textarea.insert(END,f"\n {self.bacoliat19}\t\t{self.q19.get()}\t\tالذرة")
            if self.q20.get() !=0:
                self.textarea.insert(END,f"\n {self.bacoliat20}\t\t{self.q20.get()}\t\tالزيت")
            

            if self.qq1.get() !=0:
                self.textarea.insert(END,f"\n {self.dariy1}\t\t{self.qq1.get()}\t\tحليب")
            if self.qq2.get() !=0:
                self.textarea.insert(END,f"\n {self.dariy2}\t\t{self.qq2.get()}\t\tزبادي فواكه")
            if self.qq3.get() !=0:
                self.textarea.insert(END,f"\n {self.dariy3}\t\t{self.qq3.get()}\t\tزبادي عادي")
            if self.qq4.get() !=0:
                self.textarea.insert(END,f"\n {self.dariy4}\t\t{self.qq4.get()}\t\tقشطه")
            if self.qq5.get() !=0:
                self.textarea.insert(END,f"\n {self.dariy5}\t\t{self.qq5.get()}\t\tزبدة")
            if self.qq6.get() !=0:
                self.textarea.insert(END,f"\n {self.dariy6}\t\t{self.qq6.get()}\t\tجبنه")
            if self.qq7.get() !=0:
                self.textarea.insert(END,f"\n {self.dariy7}\t\t{self.qq7.get()}\t\tجبنه رومي")
            

            if self.qqq1.get() !=0:
                self.textarea.insert(END,f"\n {self.adoat1}\t\t{self.qqq1.get()}\t\tمصفاة")
            if self.qqq2.get() !=0:
                self.textarea.insert(END,f"\n {self.adoat2}\t\t{self.qqq2.get()}\t\tصحن")
            if self.qqq3.get() !=0:
                self.textarea.insert(END,f"\n {self.adoat3}\t\t{self.qqq3.get()}\t\tكأس")
            if self.qqq4.get() !=0:
                self.textarea.insert(END,f"\n {self.adoat4}\t\t{self.qqq4.get()}\t\tابريق")
            if self.qqq5.get() !=0:
                self.textarea.insert(END,f"\n {self.adoat5}\t\t{self.qqq5.get()}\t\tسكين")
            if self.qqq6.get() !=0:
                self.textarea.insert(END,f"\n {self.adoat6}\t\t{self.qqq6.get()}\t\tشوك")
            if self.qqq7.get() !=0:
                self.textarea.insert(END,f"\n {self.adoat7}\t\t{self.qqq7.get()}\t\tمبشره")
            if self.qqq8.get() !=0:
                self.textarea.insert(END,f"\n {self.adoat8}\t\t{self.qqq8.get()}\t\tملاعق")
            if self.qqq9.get() !=0:
                self.textarea.insert(END,f"\n {self.adoat9}\t\t{self.qqq9.get()}\t\tمقص")
            if self.qqq10.get() !=0:
                self.textarea.insert(END,f"\n {self.adoat10}\t\t{self.qqq10.get()}\t\tوعاء الخلاط")
            if self.qqq11.get() !=0:
                self.textarea.insert(END,f"\n {self.adoat11}\t\t{self.qqq11.get()}\t\tمقشره")
            if self.qqq12.get() !=0:
                self.textarea.insert(END,f"\n {self.adoat12}\t\t{self.qqq12.get()}\t\tفتاحه علب")
            if self.qqq13.get() !=0:
                self.textarea.insert(END,f"\n {self.adoat13}\t\t{self.qqq13.get()}\t\tلوخ تقطيع")
            if self.qqq14.get() !=0:
                self.textarea.insert(END,f"\n {self.adoat14}\t\t{self.qqq14.get()}\t\tحفارة")
            if self.qqq15.get() !=0:
                self.textarea.insert(END,f"\n {self.adoat15}\t\t{self.qqq15.get()}\t\tسله قمامه")
            if self.qqq16.get() !=0:
                self.textarea.insert(END,f"\n {self.adoat16}\t\t{self.qqq16.get()}\t\tمنفضه")
            if self.qqq17.get() !=0:
                self.textarea.insert(END,f"\n {self.adoat17}\t\t{self.qqq17.get()}\t\tاكياس")
            if self.qqq18.get() !=0:
                self.textarea.insert(END,f"\n {self.adoat18}\t\t{self.qqq18.get()}\t\tمضارب بيض")    

            if self.qqqq1.get() !=0:
                self.textarea.insert(END,f"\n {self.drink1}\t\t{self.qqqq1.get()}\t\tمشروبات غذيه")
            if self.qqqq2.get() !=0:
                self.textarea.insert(END,f"\n {self.drink2}\t\t{self.qqqq2.get()}\t\t المياه المعدنيه"      )
            if self.qqqq3.get() !=0:
                self.textarea.insert(END,f"\n {self.drink3}\t\t{self.qqqq3.get()}\t\tالشاي")
            if self.qqqq4.get() !=0:
                self.textarea.insert(END,f"\n {self.drink4}\t\t{self.qqqq4.get()}\t\tكاكاو")
            if self.qqqq5.get() !=0:
                self.textarea.insert(END,f"\n {self.drink5}\t\t{self.qqqq5.get()}\t\tالسحلب")
            if self.qqqq6.get() !=0:
                self.textarea.insert(END,f"\n {self.drink6}\t\t{self.qqqq6.get()}\t\tعصائر")
            if self.qqqq7.get() !=0:
                self.textarea.insert(END,f"\n {self.drink7}\t\t{self.qqqq7.get()}\t\tنعناع")
            if self.qqqq8.get() !=0:
                self.textarea.insert(END,f"\n {self.drink8}\t\t{self.qqqq8.get()}\t\tالينسون")                                                                                        
            
            if self.qqqqq1.get() !=0:
                self.textarea.insert(END,f"\n {self.atool1}\t\t{self.qqqqq1.get()}\t\tمكنسه")                                                                                        
            if self.qqqqq2.get() !=0:
                self.textarea.insert(END,f"\n {self.atool2}\t\t{self.qqqqq2.get()}\t\tتليفزيون")                                                                                        
            if self.qqqqq3.get() !=0:
                self.textarea.insert(END,f"\n {self.atool3}\t\t{self.qqqqq3.get()}\t\tغساله")                                                                                        
            if self.qqqqq4.get() !=0:
                self.textarea.insert(END,f"\n {self.atool4}\t\t{self.qqqqq4.get()}\t\tمكرويف")                                                                                      
            if self.qqqqq5.get() !=0:
                self.textarea.insert(END,f"\n {self.atool5}\t\t{self.qqqqq5.get()}\t\tخلاط")  
            if self.qqqqq6.get() !=0:
                self.textarea.insert(END,f"\n {self.atool6}\t\t{self.qqqqq6.get()}\t\tفرن غاز")                                                                                          
            if self.qqqqq7.get() !=0:
                self.textarea.insert(END,f"\n {self.atool7}\t\t{self.qqqqq7.get()}\t\tمروحه")
            if self.qqqqq8.get() !=0:
                self.textarea.insert(END,f"\n {self.atool8}\t\t{self.qqqqq8.get()}\t\tفلتر ماء")
            if self.qqqqq9.get() !=0:
                self.textarea.insert(END,f"\n {self.atool9}\t\t{self.qqqqq9.get()}\t\tمكواة")
            if self.qqqqq10.get() !=0:
                self.textarea.insert(END,f"\n {self.atool10}\t\t{self.qqqqq10.get()}\t\tتكيف")
            if self.qqqqq11.get() !=0:
                self.textarea.insert(END,f"\n {self.atool11}\t\t{self.qqqqq11.get()}\t\tللاتوب")                

            self.textarea.insert(END,"\n ..............................") 
            self.textarea.insert(END,f"\n\t {self.all} $\t         : المجموع الكلي   ") 
            self.textarea.insert(END,"\n ..............................") 
            self.save()

            



root = Tk()
ob = super(root)

root.mainloop()
