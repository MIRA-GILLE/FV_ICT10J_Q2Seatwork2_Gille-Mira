from pyscript import document

def CheckMem(e):
    mem_bers = ["Dany", "Mira"]
    firstName = document.getElementById("firstName").value
    lastName = document.getElementById("lastName").value

    confirm_mem = firstName in mem_bers

    firstName = "Mira"
    firstName2 = "Dany"
    lastName = "Gille"
    message = (f"Congratulations {firstName} + {lastName}, you are a member of the group!") , (f"Sorry {firstName} + {lastName}, you are not a member of the group.")
