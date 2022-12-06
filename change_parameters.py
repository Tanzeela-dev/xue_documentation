# This code will write new values of the parameters lambda, kappa, poissons ratio and M in the prj file for 
# running a new simulation for different values of these parameters.  The first path is just to check
# if the file that we want to change is on path or not.
# path check. In line 78, give the prj file name which needs changed.
import os
from path import Path

def valChange(name,newval,prj):
    if isinstance(prj,str):
        prj = io.StringIO(prj)
    counter=0
    flag=False
    # pattern= re.compile(r'<values>(.+?)</values>')

    newfile=""
    flag2=True
    for l in prj:
        if f'<name>{name}</name>' in l:
            newfile = newfile +l
            flag=True
            counter=0
            flag2=False
        else:
            if flag2==True:
                newfile = newfile +l
        counter=counter+1
        if counter==3 and flag==True:
#             print(l)
            flag=False
    #         l=re.sub(pattern,str(-250e3),l)
    #         loadingvalue=[float(v) for v in re.findall(pattern,l)]

            
            cl = r'<type>Constant</type>' + '\n'
            newfile+=cl
            nl= r'<value>' + str(newval) + r'</value>'+'\n'
            newfile = newfile +nl
            flag2=True
#             print(nl)
    return newfile





import io
def newValues(fileToread,lamda, kappa,M,pr):
    prj=open(fileToread)
    newfile = valChange('PoissonRatio',pr,prj)
    newfile = valChange('CriticalStateLineSlope',M,newfile)
    newfile = valChange('SwellingLineSlope',kappa,newfile)
    newfile = valChange('VirginConsolidationLineSlope',lamda,newfile)
    prj.close()
    return newfile



cur_dir = Path(os.getcwd())
def r(num):
    num = str(num)
    return num.replace(".","_")
def path_check(lamda=0.1, kappa=0.01,M=1.15,pr=0.2):
    folder_name = f"lambda_{r(lamda)}_kappa_{r(kappa)}_pr_{r(pr)}_M_{r(M)}"
    out_folder_path = cur_dir / Path(f'../out/{folder_name}')
    out_folder_path = str(out_folder_path)
    if not os.path.exists(out_folder_path):
        os.makedirs(out_folder_path)
    return out_folder_path
from subprocess import call, PIPE,run

# cmd = [f"{ogs_path} {input_path} -o {out_path}"]

# !$ogs_path $input_path -o $out_path
# print(cmd)
# res = run(cmd,stdout=PIPE)
# print(res.stdout.decode('utf-8'))
if __name__=='__main__':
    fileToread = 'study2_.prj'
    lamda = 0.033
    kappa = 0.010
    poisson_ratio = 0.25
    M = 1.075
  
    
    newfile = newValues(fileToread=fileToread,lamda=lamda, kappa=kappa,M=M,pr=poisson_ratio)
    newfileName = 'study2_result.prj' 
    with open(newfileName,'w') as f:
        f.write(newfile)
    ogs_path = cur_dir / Path('../lib/ogs_local')
    input_path = cur_dir/ Path(newfileName)
    
    
    out_path = path_check(lamda=lamda, kappa=kappa,M=M,pr=poisson_ratio)
    print(f'Output file path: {out_path}')
    # input_path = '"' + str(input_path) + '"'
    # out_path = '"' + out_path + '"'
    # ogs_path = '"' + str(ogs_path) + '"'
    
    cmd = [ogs_path, input_path, '-o', out_path]
    
    call(cmd)

    # print(res.stdout.decode('utf-8'))




















