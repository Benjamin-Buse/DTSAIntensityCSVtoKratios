import pandas as pd
import tkinter
import tkinter.filedialog
import tkinter.simpledialog
import os
import datetime
import re
import dateutil.parser
date_time = datetime.datetime.now()
userstarttime = tkinter.simpledialog.askstring(title="Start Time",prompt="Enter start date and time",initialvalue=date_time.strftime("%c"))
userstarttimeP = dateutil.parser.parse(userstarttime)
#simhr = tkinter.simpledialog.askinteger("Simulation selection","How many hours ago first simulation wish to process?")
#if simhr == 0:
#    simmin = tkinter.simpledialog.askinteger("Simulation selection","How many minutes ago first simulation wish to process?")
#else:
#    simmin = 0

folder_dir = tkinter.filedialog.askdirectory(title="Select directory containing simulations folders")
csvlocation = []
for root, dirs, files in os.walk(folder_dir):
    for file in files:
        if file == "Intensity.csv":
            print(root)
            print(os.path.getmtime(root+'/'+file))
            #print(file)
            if datetime.datetime.fromtimestamp(os.path.getmtime(root+'/'+file)) > userstarttimeP:
                print(file)
                #print(root+'/'+file)
                csvlocation.append(root+'/'+file)

#numofexperiments=tkinter.simpledialog.askinteger(title="number of experiments",prompt="enter number of simulations")
print(len(csvlocation))
numofexperiments=len(csvlocation)
#csvlocation = []
ExperimentName = []
vars()['El' + 'elm']=[]
for exp in range(0,numofexperiments):
    print(exp)
    #csvlocation.append(tkinter.filedialog.askopenfile(title="select csv intensity file"+str(exp)))
    df = pd.read_csv(csvlocation[exp], delimiter=('\t'),names=list('abc'))
    #extracts the element intensities
    ExperimentName.append(df.loc[0]["a"])
    vars()['El' + str(exp) + 'elm']=[]
    vars()['El' + str(exp) + 'inten']=[]
    for z in range(0,len(df)):
        if df.loc[z]["a"]=="Transition":
            print("yes")
            x=z+1
            #i=1
            #vars()['El' + str(i) + 'elm']=[]
            while str(df.loc[x]["a"])[1:2]==" " or str(df.loc[x]["a"])[2:3]==" ":
                print(df.loc[x]["a"])
                if df.loc[x]["a"] in eval('El' + str(exp) + 'elm'):
                    print("element present")
                    Elelm.index(df.loc[x]["a"])
                    #add intensity to existing intensity i.e. char + char fluor + brems
                    vars()['El' + str(exp) + 'inten'][Elelm.index(df.loc[x]["a"])]=float(vars()['El' + str(exp) + 'inten'][Elelm.index(df.loc[x]["a"])])+float(df.loc[x]["c"])
                else:
                    print("element not present")
                    vars()['El' + str(exp) +'elm'].append(df.loc[x]["a"])
                    vars()['El' + str(exp) + 'inten'].append(df.loc[x]["c"])
                if df.loc[x]["a"] in Elelm:
                    print("element already present, possibly from previous simulation")
                    #element already present
                else:
                    Elelm.append(df.loc[x]["a"])
                x=x+1
                if x == len(df):
                    break
#Elelm is list of elements in all simulations combined
#El0elm is list of elements in simulation 0
#El0inten is list of intensities in simulation 0


#Now input from other script - html - kratios and calczaf
#user select which experiment is standard
standardselectionname = []
standardselectionnum = []
import tkinter
import tkinter.messagebox
for i in range(0,len(ExperimentName)):
    #only bulk experiments as standards
    if ExperimentName[i].find("bulk") > 0:
        standardselection = tkinter.messagebox.askquestion(title="experiment selection", message=ExperimentName[i]+'\r'+"Is this a standard")
        if standardselection == 'yes':
            standardselectionname.append(ExperimentName[i])
            standardselectionnum.append(i)

#selecting which standard for which element
Elelm2 = Elelm
elementstandard = []
standardelement = []
standardelementname = []
standardexperimentnum = []
for i in range(0,len(Elelm2)):
    #for iv in range(0,len(eval('El'+str(i)+'elm2'))):
    checkelementselected=0
    for ii in range(0,len(standardselectionname)):
        #standardselection = tkinter.messagebox.askquestion(title="standard selection", message=standardselectionname[ii]+'\r'+"Is this the standard for"+'\r'+eval('El'+str(i)+'elm2'+'['+str(iv)+']'))
        if checkelementselected == 0:
            standardselection = tkinter.messagebox.askquestion(title="standard selection", message=standardselectionname[ii]+'\r'+"Is this the standard for"+'\r'+Elelm2[i])
            if standardselection == 'yes':
                print(i)
                elementstandard.append(Elelm2[i])
                print(Elelm2[i])
                print(ii)
                print(standardselectionname[ii])
                standardelement.append(ii)
                standardelementname.append(standardselectionname[ii])
                standardexperimentnum.append(standardselectionnum[ii])
                checkelementselected=1
                
#calculate kratio
#f = open("C:/Users/glxbb/Documents/DTSA-II Reports/2024/September/26-Sep-2024/PythonKratios.txt","a")
#f = open(csvlocation[0].split('Intensity.csv')[0]+'PythonKratios.txt',"a")
f = open(csvlocation[0].split('\\')[0]+'/'+datetime.datetime.now().strftime("%c").replace(':','')+' PythonKratios.txt',"a")
f.write('Name'+','+'Xray'+','+'Kratio'+','+'Sphere Size'+'Rectangle Size'+','+'Dist from contact'+'contact-sphere'+'contact-rectangle'+'\n')

for i in range(0,len(ExperimentName)):
    #for each x-ray line in first one experiment then next etc
    for ii in range(0,len(eval('El'+str(i)+'elm'))):
        try:
            #find standard
            print(elementstandard.index(eval('El'+str(i)+'elm')[ii]))
            #so experiment no is
            print(standardexperimentnum[elementstandard.index(eval('El'+str(i)+'elm')[ii])])
            #so kratio is
            #unknown/
            #eval('ElG'+str(i)+'_'+str(ii))/
            #print(eval('ElG'+str(i)+'_'+str(ii)))
            print(eval('El'+str(i)+'inten')[ii])
            UNKint=eval('El'+str(i)+'inten')[ii]
            #standard intensity is - but ii needs to be determined
            #eval('ElG'+str(standardexperimentnum[elementstandard.index(eval('El'+str(i))[ii][:2])])+'_'+str(ii))
            #standard list of elements is
            print(eval('El'+str(standardexperimentnum[elementstandard.index(eval('El'+str(i)+'elm')[ii])])+'elm'))
            #position of element for standard is
            print(eval('El'+str(standardexperimentnum[elementstandard.index(eval('El'+str(i)+'elm')[ii])])+'elm').index(eval('El'+str(i)+'elm')[ii]))
            #standard intensity is
            print(eval('El'+str(standardexperimentnum[elementstandard.index(eval('El'+str(i)+'elm')[ii])])+'inten')[(eval('El'+str(standardexperimentnum[elementstandard.index(eval('El'+str(i)+'elm')[ii])])+'elm')).index(eval('El'+str(i)+'elm')[ii])])
            STDint=eval('El'+str(standardexperimentnum[elementstandard.index(eval('El'+str(i)+'elm')[ii])])+'inten')[(eval('El'+str(standardexperimentnum[elementstandard.index(eval('El'+str(i)+'elm')[ii])])+'elm')).index(eval('El'+str(i)+'elm')[ii])]
            #so kratio is
            #sum(eval('El'+str(i)+'inten')[ii])/sum(eval('ElG'+str(standardexperimentnum[elementstandard.index(eval('El'+str(i)+'elm')[ii][:2])])+'_'+str(eval('El'+str(standardexperimentnum[elementstandard.index(eval('El'+str(i)+'elm')[ii][:2])])).index(eval('El'+str(i)+'elm')[ii]))))
            #print(sum(eval('El'+str(i)+'inten')[ii])/sum(eval('ElG'+str(standardexperimentnum[elementstandard.index(eval('El'+str(i)+'elm')[ii][:2])])+'_'+str(eval('El'+str(standardexperimentnum[elementstandard.index(eval('El'+str(i)+'elm')[ii][:2])])).index(eval('El'+str(i)+'elm')[ii])))))
            UNKint/STDint
            print(UNKint/STDint)
            #Extract Size of sphere
            SphereSize=0
            try:
                SphereSize=float(re.search(r'of a(.*?)micron',ExperimentName[i]).group(1))
            except:
                print("not a sphere")
            #Extract distance from sphere of interface
            DistContact=0
            try:
                DistContact=float(ExperimentName[i].split('(')[1].split(')')[0])
            except:
                print("no distance")
            RectangleSize=0
            try:
                RectangleSize=float(ExperimentName[i].split('[')[1].split(']')[0].split(' microns')[0])
            except:
                print("no distance")
            ContactSphere = DistContact-(SphereSize*1e-6)
            ContactRectangle = DistContact-(RectangleSize*1e-6)
            #f.write(str(ExperimentName[i])+','+str(eval('El'+str(i)+'elm')[ii])+','+str(sum(eval('ElG'+str(i)+'_'+str(ii)))/sum(eval('ElG'+str(standardexperimentnum[elementstandard.index(eval('El'+str(i)+'elm')[ii][:2])])+'_'+str(eval('El'+str(standardexperimentnum[elementstandard.index(eval('El'+str(i)+'elm')[ii][:2])])).index(eval('El'+str(i)+'elm')[ii])))))+'\n')
            f.write(str(ExperimentName[i])+','+str(eval('El'+str(i)+'elm')[ii])+','+str(UNKint/STDint)+','+str(SphereSize)+','+str(RectangleSize)+','+str(DistContact)+','+str(ContactSphere)+','+str(ContactRectangle)+'\n')
        except ValueError:
            print("Element not in standard list")
            print(eval('El'+str(i)+'elm')[ii][:2])
        except:
            print("Something else went wrong")
f.close()
print("results file saved at:")
#print(csvlocation[0].split('Intensity.csv')[0]+'PythonKratios.txt')
print(csvlocation[0].split('\\')[0]+'/'+datetime.datetime.now().strftime("%c").replace(':','')+' PythonKratios.txt')