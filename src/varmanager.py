vars = {
    
    "VERSION": "8.0.3"
    
}

defaultvars = {

    "VERSION": "8.0.3"

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
    
