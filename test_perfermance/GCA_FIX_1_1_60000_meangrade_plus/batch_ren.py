import os 
import glob
def get_path(path):
    list_path=glob.glob(path)
    return list_path
def rename(path):
    list_path=get_path(path)
    print(list_path)
    for i in range(len(list_path)):
        os.system('ren'+" "+list_path[i]+" "+'test_'+str(i)+'.bmp')
rename("./*.tiff")
os.system("ren batch_rename.py batch_ren.py")