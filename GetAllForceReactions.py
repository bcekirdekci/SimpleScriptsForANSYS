#####################################
#   Coded by Burak Tunc CEKIRDEKCI
#   https://www.linkedin.com/in/bcekirdekci/
#   burak.cekirdekci@computelabs.io
#####################################

clr.AddReference("Ans.UI.Toolkit")
clr.AddReference("Ans.UI.Toolkit.Base")
from Ansys.UI.Toolkit import*

def GetAllForceReaction():
    
    temp = clr.Reference[str]()
    myDocumentsPath = System.Environment.GetFolderPath(System.Environment.SpecialFolder.MyDocuments)
    dlgRes = FolderBrowserDialog.ShowFolderBrowserDialog(ExtAPI.UserInterface.MainWindow,myDocumentsPath, temp)
    selectedFolder = temp.Value
    
    file = open(str(selectedFolder) + '\ForceReactionyResult.txt',"w")
    file.write(' {:20s}   {:11s} {:8s} {:9s}\n'.format("Object Name","FX[N]","FY[N]","FZ[N]"))
    
    All_FRs = DataModel.GetObjectsByType(DataModelObjectCategory.ForceReaction) #Get all "Force Reaction" objects
    
    for any_obj in All_FRs:
        name = any_obj.Name
        fx = any_obj.XAxis.Value
        fy = any_obj.YAxis.Value
        fz = any_obj.ZAxis.Value
        file.write('{:20s} {:10.3f} {:10.3f} {:10.3f}\n'.
                   format(name,fx,fy,fz))
                   
    file.close()

    

GetAllForceReaction()