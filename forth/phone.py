def show_phone(args,contacts):
    name = args[0]
    if name in contacts:
        return contacts.get(name)
    else:
        return("Contact not found.")