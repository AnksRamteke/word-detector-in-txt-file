import os

def isBinod(filename):
    with open(filename,"r") as f:
        filecontent = f.read()
        #detect all forms of vinod
        if "binod" in filecontent.lower():
            return True
        else:
            return false
    #listing content of the folder

    dir_contents = os.listdir()
    nBinod = 0

    #For each files,run isBinod for them
    for item in dir_content:
        if item.endswith('.txt'):
            print(f'********************Detecting Binod in {item}*******************')

            flag = isBinod(item)
            if(flag):
                print(f'********************Biond found in {item}********************')
            else:
                print(f'Binod not found in {item}')

    
    print('Binod detector summary')
    print(f'{nBinod} files found with Binod hidden into them')
