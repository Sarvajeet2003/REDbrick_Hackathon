def register_donor(request):
    if request.method == 'POST':
        donor_form = DonorForm(request.POST)
        if donor_form.is_valid():
            donor_data = donor_form.cleaned_data
            save_donor_to_mongodb(donor_data)
            return redirect('donate')
    else:
        donor_form = DonorForm()
    return render(request, 'donations/register_donor.html', {'donor_form': donor_form})

def save_donor_to_mongodb(donor_data):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["food_donation_db"]
    donors_collection = db["donors"]
    
    donor_info = {
        "name": donor_data["name"],
        "email": donor_data["email"],
        "phone": donor_data["phone"],
        "location": {
            "latitude": donor_data["latitude"],
            "longitude": donor_data["longitude"]
        },
        "donation_items": [
            {
                "item_name": donor_data["item_name"],
                "quantity": donor_data["quantity"]
            }
        ]
    }
    
    donors_collection.insert_one(donor_info)
