from pyscript import document

def CheckMem(e):
    mem_bers = ["Camerron Bufford", "Mira Gille", "Keisha Valiente", "Renn Santos", "Dany Gille"]
   

    mem1 = document.getElementById("firstName").value
    name = "MirGil"
    
    confirm_mem = mem1 in mem_bers

    message = (f"Congratulations {mem1}, you are a member of the group!"), (f"Sorry {mem1}, you are not a member of the group.")

    
   
