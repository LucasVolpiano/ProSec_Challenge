import os, hashlib, psutil, 
from tkinter import messagebox, Tk
from os import listdir
from os.path import isfile, join

hash = ()
user = os.getlogin()
cd = [f'C:\\Users\\{user}', f'C:\\Users\\{user}\\Downloads', f'C:\\Users\\{user}\\Documents', f'C:\\Users\\{user}\\Desktop']
dirx = [f'C:\\Users\\{user}\\!', f'C:\\Users\\{user}\\Downloads\\!', f'C:\\Users\\{user}\\Documents\\!', f'C:\\Users\\{user}\\Desktop\\!']


def alert(title, message, kind='info', hidemain=True):
    if kind not in ('error', 'warning', 'info'):
        raise ValueError('Unsupported alert kind.')

    show_method = getattr(messagebox, 'show{}'.format(kind))
    show_method(title, message)

def mkdir():
    for dir in cd:
        os.chdir(dir)
        os.system("mkdir !")

def mkfile():
    for dir in dirx:
        try:
            os.chdir(dir)
            all_files = (item for item in listdir(dir) if isfile(join(dir, item)))
            for a in all_files:
                os.remove(a)
            os.system('echo "hello, I suppose that you have a lot of questions abaout this arquive but no worry i am not bad" > !.txt')
            os.system('echo "hello, I suppose that you have a lot of questions abaout this arquive but no worry i am not bad" > !.docx')
            os.system('echo "hello, I suppose that you have a lot of questions abaout this arquive but no worry i am not bad" > !.pdf')
            os.system('echo "hello, I suppose that you have a lot of questions abaout this arquive but no worry i am not bad" > !.doc')
            os.system('echo "hello, I suppose that you have a lot of questions abaout this arquive but no worry i am not bad" > !.rtf')
        except:
            pass

alvos = ('.txt', '.docx', '.pdf', '.doc', '.rtf')
caminhos = []
for i in dirx:
    for root, diretorios, arquivos in os.walk(i):
        for arquivo in arquivos:
            caminho, extenção = os.path.splitext(root + '\\' + arquivo)
            if extenção in alvos:
                caminhos.append(root + '\\' + arquivo)

def pid():
    global process
    process = []
    a = ("","VSSVC.exe","WinStore.App.exe","SecurityHealthSystray.exe","python3.10.exe","msdtc.exe","MsMpEng.exe","VGAuthService.exe","vm3dservice.exe","vmtoolsd.exe","YourPhone.exe","WMIADAP.exe","NisSrv.exe","OneDrive.exe","uhssvc.exe","Trapware copy.exe","msedge.exe","TiWorker.exe","wireguard.exe","browserhost.exe","McAMTaskAgent.exe","BackgroundTransferHost.exe","CompPkgSrv.exe","sppsvc.exe","dllhost.exe","ShellExperienceHost.exe","uihost.exe","vmmem","SystemSettings.exe","Microsoft.Photos.exe","ApplicationFrameHost.exe","UserOOBEBroker.exe","Video.UI.exe","LockApp.exe","PhoneExperienceHost.exe","AdobeCollabSync.exe","AppMonitorPlugIn.exe","wslhost.exe","vmwp.exe","taskhostw.exe","SystemSettingsBroker.exe","System Idle Process","MfeBrowserHost.exe","MemCompression","System","TextInputHost.exe","QcShm.exe","RuntimeBroker.exe","CodeSetup-stable-e4503b30fc78200f846c62cf8091b76ff5547662.tmp","audiodg.exe","smartscreen.exe","steamwebhelper.exe","Trapware.exe","conhost.exe","svchost.exe","powershell.exe","python.exe","Code.exe","Trapware.py","sihost.exe","MoUsoCoreWorker.exe","explorer.exe","lsass.exe","smss.exe","csrss.exe","fontdrvhost.exe","services.exe","LsaIso.exe","WUDFHost.exe","WmiPrvSE.exe","fontdrvhost.exe","vmware-usbarbitrator64.exe","MMSSHOST.exe","mfevtps.exe","SgrmBroker.exe","ProtectedModuleHost.exe","McCSPServiceHost.exe","GoogleCrashHandler64.exe","QASvc.exe","MfeAVSvc.exe","SecurityHealthService.exe","CamUsage.exe","MicUsage.exe","SearchApp.exe","vmcompute.exe","SearchIndexer.exe","ONENOTEM.EXE","SearchProtocolHost.exe","winlogon.exe","OfficeClickToRun.exe","ModuleCoreService.exe","vmware-tray.exe","SCTBSvc.exe","steam.exe","igfxextN.exe","QAAdminAgent.exe","dwm.exe","McUICnt.exe","unsecapp.exe","ctfmon.exe","StorPSCTL.exe","TrustedInstaller.exe","StartMenuExperienceHost.exe","SearchFilterHost.exe","ACCStd.exe","mcapexe.exe","servicehost.exe","mcshield.exe","AcerRegistrationBackGroundTask.exe","UBTService.exe","vmware-authd.exe","InstallAssistService.exe","GoogleCrashHandler.exe","jhi_service.exe","chrome.exe","vmnat.exe","vmnetdhcp.exe","RtkAudUService64.exe","RstMwService.exe","PEFService.exe","mfemms.exe","LMS.exe","IntelAudioService.exe","armsvc.exe","ACCSvc.exe","OneApp.IGCC.WinService.exe","HPPrintScanDoctorService.exe","wlanext.exe","spoolsv.exe","Bridge_Service.exe","GTFidoService.exe","PresentationFontCache.exe","igfxCUIServiceN.exe","IntelCpHDCPSvc.exe","wininit.exe","Registry")
    p = psutil.process_iter()
    for proc in p:
        i = proc.name()
        if i not in a:
            process.append(i)
            print(i)
            

def find():
    for xxx in process:
        '''
        os.system(f'TASKLIST /V /fi "STATUS eq running" /FO list /FI "IMAGENAME eq {xxx}"  > xxx.txt')
        with open('xxx.txt') as o:
            lastp = o.readlines()[9]
            length = len(lastp)
            lastp[length-1]
            z = (lastp.split())
            z = (z[3])
            print(z)
            o.close
        os.remove('xxx.txt')
        '''
        os.system(f"taskkill /F /im {xxx}")
        for (dirpath, dirnames, filenames) in os.walk(f"C:\\Users\\{user}\\Downloads"):
            for filename in filenames:
                print(filename)
                if filename == xxx or filename.endswith(".wnry") or filename == "taskdl.exe" or filename == "taskse.exe":
                    kill = (dirpath +'\\'+ filename)
                    os.remove(kill)
        Tk().withdraw()
        alert('Trapware', 'Usuario ocorreu um tentativa de ataque de Ransoware na sua máquina!!!\nA ameaça foi neutralizada pelo Trapware, aconselhamos a tomar mais cuidado!!!')
                    
                

mkdir()
mkfile()
while 1 == 1:
    try:
        for arquivos in caminhos:
                with open(arquivos,"rb") as f:
                    bytes = f.read()
                    hash = hashlib.sha256(bytes).hexdigest();
                    f.close
                if hash != 'c5365d91bad451da42de1640bb62b4a867613dff51a7f886ebcf8170684f465a':
                    pid()
                    find()
                    mkfile()
                    
    except:
        pass 
