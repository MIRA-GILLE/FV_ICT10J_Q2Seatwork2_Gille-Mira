
from pyscript import document

def CheckMem(e):
    members = ["Keisha Valiente", "Mira Gille" , "Cameron Bufford" , "Gian Ibit"]

    first = document.getElementById("firstName").value
    last = document.getElementById("lastName").value

    valid = first == first.capitalize() and last == last.capitalize()

    fullName = first + " " + last

    result = members.count(fullName) == 1

    message = (
    (result) and f"Congratulations {fullName}! You are a member of the Social Sciences Club. See you there! :D"
    or f"Sorry {fullName}, you are not a member of the Social Sciences Club. Better luck next time! ;)"
    )

    document.getElementById("output1").innerText = message
