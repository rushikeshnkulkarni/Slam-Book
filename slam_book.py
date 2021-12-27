
from datetime import datetime
import os
import sys
from time import sleep, time
def ru():
           sleep(2)
           print("\n#######################################################################################################3\n")
           print(" choose  option \n \t 1. Yes\t\t 2. No")
           an=int(input("do  you want to repeat again :   "))
           if an==2:
              sys.exit()


print("\n\n======================================\4\4\4 Welcome to our slam book mini project \4\4\4 ===========================\n\n")
while True:
    print(" 1) create new slam book\n 2) delete slam book\n 3) change slam book name\n 4) edit slam book\n 5) See youe nformation")
    option= int(input("\n Please choose the option: "))
    if option==1 :
     try:
         book_name=input("Enter book name:  ")            
         book=book_name+".txt"  
         file1=open(book,"x")       
         date1=datetime.now().date()
         date2= date1.strftime("%m/%d/%Y")
         file1.write(book+"created at   "+date2)   
         full_name=  input ("\nEnter your full name\4  ")
         file1.write("\nyour full name = %s"%(full_name))
         date=  input ("Enter your birth date\4  ")
         file1.write("\nyour birth date is= %s"%(date))
         blood=  input ("Enter your blood group\4  ")
         file1.write("\n your address = %s"%(blood))
         mother= input("Enter mother name\4  ")
         file1.write("\nYour mother name =%s"%(mother))
         brother=input("enter your brother and sister name\4 ")
         file1.write("\nyour brother and sister name  =%s"%(brother))   
         mobile= int(input("Enter mobile number\4 "))
         file1.write("\nYour mobile number=%d"%(mobile))
         aadhar=int(input("Enter your aadhar number\4 "))
         file1.write("\nyour aadhar number =%d"%(aadhar))
         school_name=  input ("Enter your school  name\4  ")
         file1.write("\nyour School name = %s"%(school_name))
         address=  input ("Enter your address\4  ")
         file1.write("\n your address = %s"%(address))
         teacher=  input ("Enter your favourite teacher \4  ")
         file1.write("\nyour favour teacher name is = %s"%(teacher))
         friend=  input ("Enter your best friend name\4  ")
         file1.write("\nyour friend name is = %s"%(friend))
         sport=  input ("Enter your favourite sport name\4  ")
         file1.write("\nyour favourite sport name is = %s"%(sport))
         singer=  input ("Enter your favourite singer\4  ")
         file1.write("\nyour favourite singer is = %s"%(singer))
         song=  input ("Enter your favourite song\4  ")
         file1.write("\nyour favourite song is = %s"%(song))
         actor=  input ("Enter your actor\4  ")
         file1.write("\nyour favourite actor is = %s"%(actor))
         movie=  input ("Enter your favourite movie\4  ")
         file1.write("\nyour favourite movie is = %s"%(movie))
         place=  input ("Enter your favourite place\4  ")
         file1.write("\nyour favourite place s is = %s"%(place))
         file1.write("\n ===========================================================================================================")
         file1.close()  
         ru()
     except IOError:
         print("this file ame is already exist \n please choose another name..")
         sys.exit()
  

    elif option==2 :
        try:
           remove_file=input("Enter slam book name name\4  ")
           remove_f=remove_file+".txt"
           n= os.remove(remove_f)
           print("file deleted successfully.....")
          
        except IOError:
            print("fle does not exist")
        ru()    
      
    elif option==3 :
     try :

       cname=input("enter your slam book name  ")
       cbname=cname+".txt"
       dd=open(cbname,"r")     
       dd.close()
    

       cnname=input("enter new name  ")
       new_name=cnname+".txt"
       os.rename(cbname,new_name)    
       dd1=open(new_name,"a")     
       date3=datetime.now().date()
       date4= date3.strftime("%m/%d/%Y")
       dd1.write("\n\t\t\t\tfile renamed " +cbname+ " to "+new_name+" at "+date4)      
       dd1.close()
       print("name changed successfully.....")
       ru()
     
     except IOError:
        print("please enter correct book name ")


    if option==4:

        
          editbooke=input("Enter book name: ")      
        
          ebook=editbooke+".txt"
          try:
              ebook2=open(ebook,"r") 
              ebook2.close()
          except IOError:
              print("book does not exist")
              sys.exit()   
          ebook1=open(ebook,"a")
           
          date1=datetime.now().date()
          date2= date1.strftime("%m/%d/%Y")
          ebook1.write("\n\n================================================================================\n\n "+ebook+"below information edited at   "+date2)      
          full_name=  input ("Enter your full name\4  ")
          ebook1.write("\nyour full name = %s"%(full_name))
          date=  input ("Enter your birth date\4  ")
          ebook1.write("\nyour birth date is= %s"%(date))
          blood=  input ("Enter your blood group\4  ")
          ebook1.write("\nyour address = %s"%(blood))
          mother= input("Enter mother name\4  ")
          ebook1.write("\nYour mother name =%s"%(mother))
          brother=input("enter your brother and sister name\4 ")
          ebook1.write("\nyour brother and sister name  =%s"%(brother))   
          mobile= int(input("Enter mobile number\4 "))
          ebook1.write("\nYour mobile number=%d"%(mobile))
          aadhar=int(input("Enter your aadhar number\4 "))
          ebook1.write("\nyour aadhar number =%d"%(aadhar))
          school_name=  input ("Enter your school  name\4  ")
          ebook1.write("\nyour School name = %s"%(school_name))
          address=  input ("Enter your address\4  ")
          ebook1.write("\nyour address = %s"%(address))
          teacher=  input ("Enter your favourite teacher \4  ")
          ebook1.write("\nyour favour teacher name is = %s"%(teacher))
          friend=  input ("Enter your best friend name\4  ")
          ebook1.write("\nyour friend name is = %s"%(friend))
          sport=  input ("Enter your favourite sport name\4  ")
          ebook1.write("\nyour favourite sport name is = %s"%(sport))
          singer=  input ("Enter your favourite singer\4  ")
          ebook1.write("\nyour favourite singer is = %s"%(singer))
          song=  input ("Enter your favourite song\4  ")
          ebook1.write("\nyour favourite song is = %s"%(song))
          actor=  input ("Enter your actor\4  ")
          ebook1.write("\nyour favourite actor is = %s"%(actor))
          movie=  input ("Enter your favourite movie\4  ")
          ebook1.write("\nyour favourite movie is = %s"%(movie))
          place=  input ("Enter your favourite place\4  ")
          ebook1.write("\nyour favourite place  is = %s"%(place))         
          ebook1.close()
          ru()
          if ebook1:
           print("data saved sucessfuly.....")

    if option==5:

        try:
          editbooke=input("Enter book name: ")      
        
          ebook=editbooke+".txt"
    
    
          ebook1=open(ebook,"r")
          readd=ebook1.read();
          print(readd)
          ebook1.close()
         
        except IOError:
           print("file does not exist")
        ru()

    else:
        print('please choose correct option ')
        ru()






        




         

          
      



    






