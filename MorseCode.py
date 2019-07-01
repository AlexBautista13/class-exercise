morseCode = {"A":".-","B":"-...","C":"-.-."}
morseCode["D"] = "-.."
morseCode["E"] = "."
morseCode["F"] = "..-."
morseCode["G"] = "--."
morseCode["H"] = "...."
morseCode["I"] = ".."
morseCode["J"] = ".---"
morseCode["K"] = "-.-"
morseCode["L"] = ".-.."
morseCode["M"] = "--"
morseCode["N"] = "-."
morseCode["O"] = "---"
morseCode["P"] = ".--."
morseCode["Q"] = "--.-"
morseCode["R"] = ".-."
morseCode["S"] = "..."
morseCode["T"] = "-"
morseCode["U"] = "..-"
morseCode["V"] = "...-"
morseCode["W"] = ".--"
morseCode["X"] = "-..-"
morseCode["Y"] = "-.--"
morseCode["Z"] = "--.."

message = input("Type a message to convert in morse code (e.g. \"SOS\"?)").upper()
encodedMessage = ""

for character in message:

  if character in morseCode:
    encodedMessage += morseCode[character] + " "
  else:

    encodedMessage += " "
    

print("Your message in morse code is:")
print(encodedMessage)