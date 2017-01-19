import os

dir_name1 = '/home/users/xiangye/fzxl/carbonnanotube/cnt99/2tube/16/isolated/caledinSHNU/static'
os.chdir(dir_name1)
os.system('cp ../../../../../1tube/isolated/caledinSHNU/LDA/band/vasp.pbs ../band')
os.system('cp POSCAR CHG CHGCAR ../band')
os.system('cd ../band')
os.system('qsub vasp.pbs')

dir_name2 = '/home/users/xiangye/fzxl/carbonnanotube/cnt99/2tube/17/isolated/caledinSHNU/static'
os.chdir(dir_name2)
os.system('cp ../../../../../1tube/isolated/caledinSHNU/LDA/band/vasp.pbs ../band')
os.system('cp POSCAR CHG CHGCAR ../band')
os.system('cd ../band')
os.system('qsub vasp.pbs')

dir_name3 = '/home/users/xiangye/fzxl/carbonnanotube/cnt99/2tube/18/isolated/caledinSHNU/static'
os.chdir(dir_name3)
os.system('cp ../../../../../1tube/isolated/caledinSHNU/LDA/band/vasp.pbs ../band')
os.system('cp POSCAR CHG CHGCAR ../band')
os.system('cd ../band')
os.system('qsub vasp.pbs')

dir_name4 = '/home/users/xiangye/fzxl/carbonnanotube/cnt99/2tube/19/isolated/caledinSHNU/static'
os.chdir(dir_name4)
os.system('cp ../../../../../1tube/isolated/caledinSHNU/LDA/band/vasp.pbs ../band')
os.system('cp POSCAR CHG CHGCAR ../band')
os.system('cd ../band')
os.system('qsub vasp.pbs')

dir_name5 = '/home/users/xiangye/fzxl/carbonnanotube/cnt99/2tube/20/isolated/caledinSHNU/static'
os.chdir(dir_name5)
os.system('cp ../../../../../1tube/isolated/caledinSHNU/LDA/band/vasp.pbs ../band')
os.system('cp POSCAR CHG CHGCAR ../band')
os.system('cd ../band')
os.system('qsub vasp.pbs')

dir_name6 = '/home/users/xiangye/fzxl/carbonnanotube/cnt99/2tube/25/isolated/caledinSHNU/static'
os.chdir(dir_name6)
os.system('cp ../../../../../1tube/isolated/caledinSHNU/LDA/band/vasp.pbs ../band')
os.system('cp POSCAR CHG CHGCAR ../band')
os.system('cd ../band')
os.system('qsub vasp.pbs')