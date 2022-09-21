from tkinter import *
from bettertables import PDF


root = Tk()

root.geometry("800x400")

own_damage_label = Label(root, text="Own Damage").place(x=15,y=10)
own_damage_text = IntVar()
own_damage_text.set(200000)
own_damage_entry = Entry(root, width=30, textvariable= own_damage_text)
own_damage_entry.place(x=150, y=10)


bi_pd_label = Label(root, text="Bodily Injury/Third Party Property Damage").place(x=15,y=40)
bi_pd_text = IntVar()
bi_pd_text.set(200000)
bi_pd_entry = Entry(root, width=30, textvariable= bi_pd_text)
bi_pd_entry.place(x=150, y=40)


auto_pass_label = Label(root, text="Auto Passenger").place(x=15,y=70)
auto_pass_text = IntVar()
auto_pass_text.set(250000)
auto_pass_entry = Entry(root, width=30, textvariable= auto_pass_text)
auto_pass_entry.place(x=150, y=70)

client_name_Label = Label(root, text="Name").place(x=15,y=100)
client_name_entry = Entry(root, width=30)
client_name_entry.insert(0, " ")
client_name_entry.place(x=150, y=100)

vehicle_name_Label = Label(root, text="Vehicle Description").place(x=15,y=130)
vehicle_name_entry = Entry(root, width=30)
vehicle_name_entry.insert(0, " ")
vehicle_name_entry.place(x=150, y=130)


def own_damage_calc():
    rate = 0.0
    if int(own_damage_entry.get()) > 500000:
        rate = 0.0
    if int(own_damage_entry.get()) < 350000:
        rate = 0.0
    return int(own_damage_entry.get()) * rate

def aog_calc():
    rate = 0.0
    return int(own_damage_entry.get()) * rate

def bi_pd_calc():
    min_100k = 270
    over_100k = ((int(bi_pd_entry.get())- 100000)/ 50000) * 75
    return  min_100k + over_100k

def third_party_calc():
    min_100k = 1095
    over_100k = ((int(bi_pd_entry.get())- 100000)/ 50000) * 75
    return  min_100k + over_100k

def auto_pass_calc():
    min_250k = 0
    over_250k = ((int(auto_pass_entry.get())- 250000)/ 50000) * 50
    return min_250k + over_250k



def quote():
    own_damage_cover = own_damage_entry.get()
    bi_pd_cover = bi_pd_entry.get()
    auto_pass_cover = auto_pass_entry.get()
    own_damage_premium = own_damage_calc()
    aog_premium = aog_calc()
    bi_pd_premium = bi_pd_calc()
    auto_pass_premium = auto_pass_calc()
    third_party_premium = third_party_calc()
    basic_premium = sum([own_damage_premium, bi_pd_premium,third_party_premium, auto_pass_premium])
    basic_premium_aog = sum([own_damage_premium, bi_pd_premium,third_party_premium, auto_pass_premium, aog_premium])
    doc_stamp = sum([own_damage_premium, bi_pd_premium,third_party_premium, auto_pass_premium]) * 0.125
    doc_stamp_aog = sum([own_damage_premium, bi_pd_premium,third_party_premium, auto_pass_premium, aog_premium]) * 0.125
    Vat = sum([own_damage_premium, bi_pd_premium,third_party_premium, auto_pass_premium]) * 0.12
    Vat_aog = sum([own_damage_premium, bi_pd_premium,third_party_premium, auto_pass_premium, aog_premium]) * 0.12
    local_gov_tax = sum([own_damage_premium, bi_pd_premium,third_party_premium, auto_pass_premium]) * 0.002
    local_gov_tax_aog = sum([own_damage_premium, bi_pd_premium,third_party_premium, auto_pass_premium, aog_premium]) * 0.002

    total_premium = sum([own_damage_premium, bi_pd_premium,third_party_premium, auto_pass_premium, doc_stamp, Vat, local_gov_tax])
    total_premium_aog = sum([own_damage_premium, bi_pd_premium,third_party_premium, auto_pass_premium, doc_stamp_aog, Vat_aog, local_gov_tax_aog, aog_premium])

    name = client_name_entry.get()
    vehicle = vehicle_name_entry.get()



    without_aog_label = Label(root, text=f"Without AOG\nOwn Damage/Theft/Riot, Strike & Civil Commotion: {own_damage_premium:.2f}\nBI/PD: {bi_pd_premium:.2f}\nThird Party Property Damage: {third_party_premium:.2f}\nAuto Passenger: {auto_pass_premium:.2f}\nBasic Premium: {basic_premium:.2f}\nDocumentary Stamp: {doc_stamp:.2f}\nVAT: {Vat:.2f}\nLocal Gov't Tax: {local_gov_tax:.2f}\nTotal Premium: {total_premium:.2f}")
    without_aog_label.place(x=0,y=200)

    with_aog_label = Label(root, text=f"With AOG\nOwn Damage/Theft/Riot, Strike & Civil Commotion: {own_damage_premium:.2f}\nActs of God/Nature: {aog_premium:.2f}\nBI/PD: {bi_pd_premium:.2f}\nThird Party Property Damage: {third_party_premium:.2f}\nAuto Passenger: {auto_pass_premium:.2f}\nBasic Premium: {basic_premium_aog:.2f}\nDocumentary Stamp: {doc_stamp_aog:.2f}\nVAT: {Vat_aog:.2f}\nLocal Gov't Tax: {local_gov_tax_aog:.2f}\nTotal Premium: {total_premium_aog:.2f}")
    with_aog_label.place(x=400,y=200)

    quote_details = [
        ["Coverage", "Limit of Liability", "W/AOG", "W/O AOG"],
        ["Own Damage", f"{int(own_damage_cover):,.2f}", f"{own_damage_premium:,.2f}", f"{own_damage_premium:,.2f}"],
        ["Theft | Riot, Strike & Civil Commotion", f"{int(own_damage_cover):,.2f}", "INCLUDED", "INCLUDED"],
        ["Acts of God/Nature", f"{int(own_damage_cover):,.2f}", f"{own_damage_premium:,.2f}", "Not Covered" ],
        ["Excess Bodily Injury", f"{int(bi_pd_cover):,.2f}", f"{bi_pd_premium:,.2f}", f"{bi_pd_premium:,.2f}"],
        ["Third Party Property Damage", f"{int(bi_pd_cover):,.2f}", f"{third_party_premium:,.2f}",f"{third_party_premium:,.2f}"],
        ["Auto PA (5 PASS.", f"{int(auto_pass_cover):,.2f}", f"{auto_pass_premium:,.2f}", f"{auto_pass_premium:,.2f}"],
        ["Basic Premium", "-", f"{basic_premium_aog:,.2f}", f"{basic_premium:,.2f}"],
        ["Documentary Stamp", "-", f"{doc_stamp_aog:,.2f}", f"{doc_stamp:,.2f}"],
        ["VAT", "-", f"{Vat_aog:,.2f}", f"{Vat:,.2f}"],
        ["Local Gov't Tax", "-", f"{local_gov_tax_aog:,.2f}", f"{local_gov_tax:,.2f}"],
        ["Total Premium", "-", f"{total_premium_aog:,.2f}", f"{total_premium:,.2f}"],
        ]
        
    create_pdf(quote_details, name, vehicle)

def create_pdf(quote_details: list, name, vehicle):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", size=15)
    
    pdf.create_table(table_data=quote_details,title=f"{name} | {vehicle}", data_size=10, cell_width=40)


    pdf.output(f"{name}.pdf")

quote_button = Button(root, text="quote", command=quote,pady= 10, padx= 10)
quote_button.place(x=400, y=70)


root.mainloop()

