import dtsa2 as dtsa2
import dtsa2.mcSimulate3 as mc3
import datetime

det = findDetector("SDD") # Replace with your detector's name
nE = 4000 # number of electrons simulated
e0 = 20	# kV

x = datetime.datetime.now()
#sample = epq.Material(epq.Composition(map(dtsa2.element,["Ca","O","C","Mg"],),[0.39,0.48,0.12,0.01],"ccMg"+x.strftime("%M")),epq.ToSI.gPerCC(2.84)) 	# epq.ToSI.gPerCC(2.72) converts 2.65g/cc into SI units 2650 kg/m3, composition is mass fraction
sample = epq.Material(epq.Composition(map(dtsa2.element,["Cr","Fe","Al","Mg","O"],),[0.42,0.10,0.05,0.09,0.34],"chr"+x.strftime("%M")),epq.ToSI.gPerCC(4.75)) 	# epq.ToSI.gPerCC(2.72) converts 2.65g/cc into SI units 2650 kg/m3, composition is mass fraction
#matrixsubstrate = epq.Material(epq.Composition(map(dtsa2.element,["Si","O"],),[0.47,0.53],"qz"+x.strftime("%M")),epq.ToSI.gPerCC(2.65)) 	# epq.ToSI.gPerCC(2.72) converts 2.65g/cc into SI units 2650 kg/m3, composition is mass fraction
matrixsubstrate = epq.Material(epq.Composition(map(dtsa2.element,["Si","Fe","Mg","O"],),[0.19,0.07,0.30,0.44],"olv"+x.strftime("%M")),epq.ToSI.gPerCC(3.35)) 	# epq.ToSI.gPerCC(2.72) converts 2.65g/cc into SI units 2650 kg/m3, composition is mass fraction
range = dtsa2.electronRange(sample,e0,density=None)

#xtraP = {}
#xtraP = {"Characteristic Accumulator":True, "Char Fluor Accumulator":True, "Brem Fluor Accumulator":True}
#xtraP.update(mc3.configureXRayAccumulators(mc3.suggestTransitions("CaOCMg",e0),charAccum=True,charFluorAccum=True,bremFluorAccum=True))
#xtraP.update(mc3.configureOutput(DefaultOutput))
#xtraP.update(mc3.configurePhiRhoZ(1.5*range))
#xtraP.update(mc3.configureEmissionImages(mc3.suggestTransitions("CaOCMg",e0), 1.5*range, size = 512))
#xtraP.update(mc3.configureTrajectoryImage(1.5*range, size = 512))
#xtraP.update(mc3.configureOutput('C:\DTSAii\Scripts')) 	# change to output folder
#xtraP.update(mc3.configureBeam(0.000001,0,0,10))
#print xtraP

xrts=mc3.suggestTransitions("CrFeAlMgSiO")
xtraParams={}
xtraParams.update(mc3.configureXRayAccumulators(xrts,charAccum=True,charFluorAccum=True,bremFluorAccum=True))
xtraParams.update(mc3.configureEmissionImages(xrts,2.0e-5,512))
xtraParams.update(mc3.configureContinuumImages( ((2.3,2.5), (4.2,4.4 )), 1.0e-5, 512 ))
xtraParams.update(mc3.configurePhiRhoZ(1.0e-5))
xtraParams.update(mc3.configureTrajectoryImage(2.0e-5,512))
#xtraParams.update(mc3.configureVariablePressure(pathLen, gas))
#xtraParams.mc3.configureVRML(nElectrons = 40)
xtraParams.update(mc3.configureBeam(x=0.000001,y=0,z=0,szNm=10))
print xtraParams

#run bulk standards
specSample = mc3.simulate(sample, det,e0=e0, nTraj=nE, dose=500.0, sf=True, bf=True,xtraParams=xtraParams)
specSample.save("%s/%s.msa" % ( reportPath(), specSample ))		# using report path
specSample.display()

specSample = mc3.simulate(matrixsubstrate, det,e0=e0, nTraj=nE, dose=500.0, sf=True, bf=True,xtraParams=xtraParams)
specSample.save("%s/%s.msa" % ( reportPath(), specSample ))		# using report path
specSample.display()

#pure metal standards
x = datetime.datetime.now()
std = epq.Material(epq.Composition(map(dtsa2.element,["Cr"],),[1],"Cr"+x.strftime("%M")),epq.ToSI.gPerCC(7.19)) 	# epq.ToSI.gPerCC(2.72) converts 2.65g/cc into SI units 2650 kg/m3, composition is mass fraction
specSample = mc3.simulate(std, det,e0=e0, nTraj=nE, dose=500.0, sf=True, bf=True,xtraParams=xtraParams)
specSample.save("%s/%s.msa" % ( reportPath(), specSample ))		# using report path
specSample.display()
x = datetime.datetime.now()
std = epq.Material(epq.Composition(map(dtsa2.element,["Al"],),[1],"Al"+x.strftime("%M")),epq.ToSI.gPerCC(2.70)) 	# epq.ToSI.gPerCC(2.72) converts 2.65g/cc into SI units 2650 kg/m3, composition is mass fraction
specSample = mc3.simulate(std, det,e0=e0, nTraj=nE, dose=500.0, sf=True, bf=True,xtraParams=xtraParams)
specSample.save("%s/%s.msa" % ( reportPath(), specSample ))		# using report path
specSample.display()
#run unknowns particle in bulk.

#x = datetime.datetime.now()
#sample = epq.Material(epq.Composition(map(dtsa2.element,["Ca","O","C","Mg"],),[0.39,0.48,0.12,0.01],"calcite-Mg-1um-"+str(x)),epq.ToSI.gPerCC(2.84)) 	# epq.ToSI.gPerCC(2.72) converts 2.65g/cc into SI units 2650 kg/m3, composition is mass fraction


#specSample = mc3.embeddedSphere(sample,0.000000500,matrixsubstrate,0.000000500,det,e0=e0, nTraj=nE, dose=500.0, sf=True, bf=True,xtraParams=xtraParams)
#specSample.save("%s/%s.msa" % ( 'C:\DTSAii\Scripts2', specSample ))		# change to output folder
#specSample.save("%s/%s.msa" % (reportPath(), specSample))		# change to output folder

#specSample.display()

#x = datetime.datetime.now()
#sample = epq.Material(epq.Composition(map(dtsa2.element,["Ca","O","C","Mg"],),[0.39,0.48,0.12,0.01],"calcite-Mg-10um-"+str(x)),epq.ToSI.gPerCC(2.84)) 	# epq.ToSI.gPerCC(2.72) converts 2.65g/cc into SI units 2650 kg/m3, composition is mass fraction
#xtraParams.update(mc3.configureBeam(0.00001,0,0,10))
#specSample = mc3.embeddedSphere(sample,0.000000500,matrixsubstrate,0.000000500,det,e0=e0, nTraj=nE, dose=500.0, sf=True, bf=True,xtraParams=xtraParams)
#specSample.save("%s/%s.msa" % ( 'C:\DTSAii\Scripts2', specSample ))		# change to output folderA
#specSample.save("%s/%s.msa" % (reportPath(), specSample))		# change to output folder
#specSample.display()

#loop from range of distances from inclusion
#createlist=[]
#range as microns
#initial short step
#for d in range(0,20,2):
    #store as meters
    #print(d)
    #createlist.append(float('%s' % float('%.11g' % (d*1e-6))))
#then larger step
#upper limit one extra
#for dd in range(20,55,5):
#    createlist.append(float('%s' % float('%.11g' % (dd*1e-6))))
#    print(dd)

#distfromincl = [0,1e-6,1e-5,1e-4]
#distfromincl = createlist
distfromincl = [0.0, 2e-06, 4e-06, 6e-06, 8e-06, 1e-05, 1.2e-05, 1.4e-05, 1.6e-05, 1.8e-05]
spheresize = [0.5e-6,1e-6, 5e-6,1e-5,2e-5]
for y in distfromincl:
#for y in range(0,5e-5,2e-6)
    x = datetime.datetime.now()
    sample = epq.Material(epq.Composition(map(dtsa2.element,["Cr","Fe","Al","Mg","O"],),[0.42,0.10,0.05,0.09,0.34],"chr-("+str(y)+")um-"+x.strftime("%M")),epq.ToSI.gPerCC(4.75)) 	# epq.ToSI.gPerCC(2.72) converts 2.65g/cc into SI units 2650 kg/m3, composition is mass fraction
    xtraParams.update(mc3.configureBeam(y,0,0,10))
    xtraParams.update(mc3.configureEmissionImages(xrts,((y*2)+3e-6),512))
    xtraParams.update(mc3.configureContinuumImages( ((2.3,2.5), (4.2,4.4 )), ((y*2)+3e-6), 512 ))
    xtraParams.update(mc3.configureTrajectoryImage(((y*2)+3e-6),512))
    for z in spheresize:
        #0 depth means top surface of sphere at surface. can't be negative
        specSample = mc3.embeddedSphere(sample,z,matrixsubstrate,0,det,e0=e0, nTraj=nE, dose=500.0, sf=True, bf=True,xtraParams=xtraParams)
        specSample.save("%s/%s.msa" % (reportPath(), specSample))		# change to output folder
        specSample.display()
        specSample = mc3.embeddedRectangle(sample,[z,z,(z/2)],matrixsubstrate,0,det,e0=e0, nTraj=nE, dose=500.0, sf=True, bf=True,xtraParams=xtraParams)
        specSample.save("%s/%s.msa" % (reportPath(), specSample))		# change to output folder
        specSample.display()
    #for comparison create a interface - one material next to the other material
    specSample = mc3.interface(sample, 0, matrixsubstrate,det,e0=e0,nTraj=nE, dose=500.0, sf=True, bf=True,xtraParams=xtraParams)
    specSample.save("%s/%s.msa" % (reportPath(), specSample))		# change to output folder
    specSample.display()