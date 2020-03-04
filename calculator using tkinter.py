from tkinter import *
from time import *


class Mybuttons:
    def __init__(self,root):
        self.str1  = ''     
        

        self.f0 = Frame(root,bg='black')
        self.f0.grid(row=0,column=0,padx=10)
        self.l = Text(self.f0,height=1,width=20,bd = 6,bg = 'powder blue')
        self.l.grid(row=0,column=0,padx=30,pady=30) 
        
        self.f = Frame(root,bg='black')
        self.f.grid(row =1,column =0,padx = 23)
        Button(self.f,bd=4,width=3,text=' 1 ',command = lambda:self.set(1)).grid(row=0,column=0,sticky=W,padx = 10,pady = 10)
        Button(self.f,bd=4,width=3,text=' 2 ',command = lambda:self.set(2)).grid(row=0,column=1,sticky=W,padx = 10,pady = 10)
        Button(self.f,bd=4,width=3,text=' 3 ',command = lambda:self.set(3)).grid(row=0,column=2,sticky=W,padx = 10,pady = 10)
        Button(self.f,bd=4,width=3,text=' 4 ',command = lambda:self.set(4)).grid(row=1,column=0,sticky=W,padx = 10,pady = 10)
        Button(self.f,bd=4,width=3,text=' 5 ',command = lambda:self.set(5)).grid(row=1,column=1,sticky=W,padx = 10,pady = 10)
        Button(self.f,bd=4,width=3,text=' 6 ',command = lambda:self.set(6)).grid(row=1,column=2,sticky=W,padx = 10,pady = 10)
        Button(self.f,bd=4,width=3,text=' 7 ',command = lambda:self.set(7)).grid(row=2,column=0,sticky=W,padx = 10,pady = 10)
        Button(self.f,bd=4,width=3,text=' 8 ',command = lambda:self.set(8)).grid(row=2,column=1,sticky=W,padx = 10,pady = 10)
        Button(self.f,bd=4,width=3,text=' 9 ',command = lambda:self.set(9)).grid(row=2,column=2,sticky=W,padx = 10,pady = 10)
        Button(self.f,bd=4,width=3,text=' 0 ',command = lambda:self.set(0)).grid(row=3,column=1,sticky=W,padx = 10,pady = 10)


        self.f1 = Frame(root,bg='black')
        self.f1.grid(row =2,column =0,padx=23)
        Button(self.f1,width=3,text=' + ',command = lambda:self.set('+')).grid(row=0,column=0,sticky=W,padx = 3,pady = 3)
        Button(self.f1,width=3,text=' - ',command = lambda:self.set('-')).grid(row=0,column=1,sticky=W,padx = 3,pady = 3)
        Button(self.f1,width=3,text=' * ',command = lambda:self.set('*')).grid(row=0,column=2,sticky=W,padx = 3,pady = 3)
        Button(self.f1,width=3,text=' / ',command = lambda:self.set('/')).grid(row=0,column=3,sticky=W,padx = 3,pady = 3)
        Button(self.f1,width=3,text=' % ',command = lambda:self.set('%')).grid(row=0,column=4,sticky=W,padx = 3,pady = 3)

        self.f2 = Frame(root,bg='black')
        self.f2.grid(row =3,column =0,padx=23)
        Button(self.f2,width=15,text=' = ',command = lambda:self.set('=')).grid(row=0,column=0,sticky=W,padx = 3,pady = 3)
        Button(self.f2,width=5,text='CLEAR',command = lambda:self.set(' ')).grid(row=0,column=1,sticky=W,padx = 3,pady = 3)

    def set(self,n):
       
       if(n==0):
           self.str1+='0'
           self.l.delete(0.0,END)
           self.l.insert(END,self.str1)
       if(n==1):
           self.str1+='1'
           self.l.delete(0.0,END)
           self.l.insert(END,self.str1)
       if(n==2):
           self.str1+='2'
           self.l.delete(0.0,END)
           self.l.insert(END,self.str1)
       if(n==3):
           self.str1+='3'
           self.l.delete(0.0,END)
           self.l.insert(END,self.str1)
       if(n==4):
           self.str1+='4'
           self.l.delete(0.0,END)
           self.l.insert(END,self.str1)
       if(n==5):
           self.str1+='5'
           self.l.delete(0.0,END)
           self.l.insert(END,self.str1)
       if(n==6):
           self.str1+='6'
           self.l.delete(0.0,END)
           self.l.insert(END,self.str1)
       if(n==7):
           self.str1+='7'
           self.l.delete(0.0,END)
           self.l.insert(END,self.str1)
       if(n==8):
           self.str1+='8'
           self.l.delete(0.0,END)
           self.l.insert(END,self.str1)
       if(n==9):
           self.str1+='9'
           self.l.delete(0.0,END)
           self.l.insert(END,self.str1)

       if(n == '='):
            self.str1 = str(eval(self.str1))
            self.l.delete(0.0,END)
            self.l.insert(END,self.str1)
       if(n== '+'):
           self.str1+='+'
           self.l.delete(0.0,END)
           self.l.insert(END,self.str1)
       if(n== '-'):
           self.str1+='-'
           self.l.delete(0.0,END)
           self.l.insert(END,self.str1)
       if(n== '*'):
           self.str1+='*'
           self.l.delete(0.0,END)
           self.l.insert(END,self.str1)
       if(n== '/'):
           self.str1+='/'
           self.l.delete(0.0,END)
           self.l.insert(END,self.str1)
       if(n== '%'):    
           self.str1+='%'
           self.l.delete(0.0,END)
           self.l.insert(END,self.str1)




       if(n == ' '):
          self.str1 = ''
          self.l.delete(0.0,END)
           
           
         
root = Tk()

root.title('Simple calculator')
root.geometry('260x400')
root.configure(background='black')


b = Mybuttons(root)


root.mainloop()
