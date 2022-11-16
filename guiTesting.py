from appJar import gui


def press(button):
    # if button == "Cancel":
    #     app.stop()
    # else:
    app.infoBox("Could be used if you catch a block", f"Block Length: xx mins\nBlock Pay: $125\nBlock Start Time: 11-10-22 8:25AM")
    app.statusbar(text="Missed A Block")





with gui("AFGrabber", "400x200", font={'size':14}) as app:
    app.entry("Username", label=True, focus=True)
    app.entry("Password", label=True, secret=True)
    app.option("Max Block Length:", label=True, value=[3, 3.5, 4, 4.5, 5])
    app.entry("Min Pay Per Hour:", label=True)
    app.buttons(["Start", "Cancel"], [press, app.stop])
    app.statusbar(text="Running")




# app = gui()
# app.addLabelEntry("Email:")
# app.addLabelSecretEntry("Password:")
# app.addLabelOptionBox("Max Block Length:", ["3", "3.5", "4", "4.5", "5"])
# app.addLabelEntry("Min Per Hour:")
# app.addLabelEntry("Time Needed To Arrive:")
# app.addButtons(["Start", "Cancel"], press)
# #app.button('Accessibility', app.showAccess, icon='ACCESS')
# app.addMessage("Could Be Used As A Log")
# app.go()


# time.sleep(2)
# app.addMessage("To Keep Track Of")
# time.sleep(2)
# app.addMessage("Missed Blocks")
# time.sleep(2)
# app.addMessage("Or Just A Sanity Check")
# app.addMessage("To Know It's Running.")
