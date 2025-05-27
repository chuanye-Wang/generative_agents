import re

def __func_clean_up(gpt_response, prompt=""):
    cr = []
    _cr = gpt_response.split(")")
    for i in _cr: 
        if i[-1].isdigit(): 
            i = i[:-1].strip()
            if i and (i[-1].isdigit()): 
                i = i[:-1].strip()
        if i and (i[-1] == "." or i[-1] == ","): 
            cr += [i[:-1].strip()]
    return cr

desp = "1) wake up and complete the morning routine at 6:00 am,\n2) check on Hobbs Cafe's inventory and prepare for the day from 7:00 am to 8:00 am,\n3) open Hobbs Cafe at 8:00 am, welcoming customers and starting to work at the counter until 5:00 pm, \n4) begin planning the Valentine's Day party setup from 5:00 pm to 6:00 pm,\n5) send out invitations and announcements for the Valentine's Day party to her customers from 6:00 pm to 6:30 pm,\n6) continue preparing decorations and snacks for the party until 7:00 pm,\n7) inform Hobbs Cafe staff about the evening plans at 7:00 pm,\n8) arrive at Hobbs Cafe with party materials from 7:15 pm, \n9) set up the cafe for the Valentine's Day party from 7:30 pm to 8:00 pm, \n10) start welcoming guests and hosting the party from 8:00 pm to 10:00 pm,\n11) assist with serving food and drinks during the party from 8:00 pm to 10:00 pm,\n12) close Hobbs Cafe at 10:00 pm, \n13) clean up the cafe after the party from 10:00 pm to 11:30 pm,\n14) go over the day’s events and plan for tomorrow with staff from 11:30 pm to 12:00 am,\n15) go to bed at 12:00 am," 
cr = __func_clean_up(desp)
print(cr)
print(len(cr))