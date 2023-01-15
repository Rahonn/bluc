vars = {
    
    "VERSION": "9.3.0"
    
}

defaultvars = {

    "VERSION": "9.3.0"

}

commandsList = []

runningLoop = False

def var_dump():
    
    print("////////////////")
    print("///DUMP START///")
    print("////////////////")
    
    for varname in vars:
        
        print(f"{varname}: {vars[varname]}")
        
    print("//////////////")
    print("///DUMP END///")
    print("//////////////")
    
