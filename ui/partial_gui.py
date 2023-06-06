# File: partial_gui.py
# Description: Prototype implementation of Game Developer Contract Matcher (GDCMatcher) case study
# Author: Chris Knowles


# Imports
import tkinter as tk
import tkinter.messagebox as mb


# Consts
# Globals


# Classes
class PartialGUI:
    """
    This is a prototype class that provides a partial GUI for the case study exercise, in particular it provides a set
    of GUI elements to allow the addition of Client, Contractor and base Contract entities and a simplified way of
    viewing these in the GUI, note - the full functionality of the main application is retained within this project but
    only those aspects of this functionality that related to the prototype GUI are employed (the rest are ignored)

    PartialGUI class - class variables
    """
    __wnd_main = tk.Tk()
    __wnd_add_client = None
    __wnd_add_contractor = None
    __wnd_add_contract = None

    __lst_clients = None
    __lst_contractors = None
    __lst_contracts = None
    __lst_owners = None
    __btn_remove_client = None
    __btn_remove_contractor = None
    __btn_remove_contract = None

    __var_clients = tk.StringVar()
    __var_selected_client_data = tk.StringVar()

    __var_contractors = tk.StringVar()
    __var_selected_contractor_data = tk.StringVar()

    __var_contracts = tk.StringVar()
    __var_selected_contract_data = tk.StringVar()

    __btn_ok = None
    __btn_cancel = None
    __var_name = tk.StringVar()
    __var_speciality = tk.StringVar()
    __var_contract_type = tk.StringVar()
    __var_owner_id = tk.StringVar()
    __var_payment = tk.DoubleVar()

    __CONTRACT_TYPES = [("Base", "b"), ("Fixed", "f"), ("Advert", "a")]

    def __init__(self):
        """
 -      Initialiser - instance variables:
            main_app: the instance of the main application this UI is operating, as MainApp, property with read/write
            access
        """
        self.__main_app = None  # Initially not set, injected into the main application as part of its initialisation

    @property
    def main_app(self):
        return self.__main_app

    @main_app.setter
    def main_app(self, main_app):
        self.__main_app = main_app

    def run(self):
        """
        Creates the main window and a prototype GUI arrangement for working with the client, contractor and contract
        data currently held in the main application, note - there is no implementation of the processing of the
        contracts provided here, just the ability to display and add new instances of these

        :return: None
        """
        # Specify dimensions of main window
        w = 1340  # Width for the main window
        h = 600  # Height for the main window

        # Get the current screen width and height
        ws = PartialGUI.__wnd_main.winfo_screenwidth()  # Width of the screen
        hs = PartialGUI.__wnd_main.winfo_screenheight()  # Height of the screen

        # Calculate x and y coordinates for the main window to locate at centre of the screen
        x = int((ws / 2) - (w / 2))
        y = int((hs / 2) - (h / 2))

        # Entitle the main window
        PartialGUI.__wnd_main.title(self.main_app.name)

        # Ensure the main window cannot be resized by locking its minimum and maximum size
        PartialGUI.__wnd_main.minsize(width=w, height=h)
        PartialGUI.__wnd_main.maxsize(width=w, height=h)

        # Locate the main window at the centre of the screen (and with its locked dimensions)
        PartialGUI.__wnd_main.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))

        # -------------------------------------------------------------------------------------------------------------

        # Build the client related list box, add button and details display area
        lbl_spacer_0 = tk.Label(PartialGUI.__wnd_main, text="", anchor="w", width=1)
        lbl_spacer_0.grid(row=1, column=0, pady=4)

        lbl_clients_list = tk.Label(PartialGUI.__wnd_main, text="Clients", anchor="w", width=8)
        lbl_clients_list.grid(row=0, column=1, padx=4, pady=4, sticky="we")

        # Build the horizontal and vertical scrollbars attached to the clients list box
        sbr_clients_hori = tk.Scrollbar(PartialGUI.__wnd_main, orient="horizontal")
        sbr_clients_hori.grid(row=2, column=1, sticky="nesw")
        sbr_clients_vert = tk.Scrollbar(PartialGUI.__wnd_main, orient="vertical")
        sbr_clients_vert.grid(row=1, column=2, sticky="nesw")

        # Build the clients list box, note - the list box widget reference has to made available to the remove_client()
        # method and therefore it has to be declared at class scope
        PartialGUI.__lst_clients = tk.Listbox(PartialGUI.__wnd_main, listvariable=PartialGUI.__var_clients,
                                              activestyle="none",
                                              xscrollcommand=sbr_clients_hori.set,
                                              yscrollcommand=sbr_clients_vert.set,
                                              width=50, height=12)
        PartialGUI.__lst_clients.grid(row=1, column=1, pady=4, sticky="nesw")
        PartialGUI.__lst_clients.bind('<<ListboxSelect>>', self.select_client)  # Bind change of selected item to select_client()

        # Attach clients list box to its horizontal and vertical scrollbars
        sbr_clients_hori.config(command=PartialGUI.__lst_clients.xview)
        sbr_clients_vert.config(command=PartialGUI.__lst_clients.yview)

        # Use a frame to hold the add and remove client buttons
        frm_client_buttons = tk.Frame(PartialGUI.__wnd_main)
        frm_client_buttons.grid(row=3, column=1, padx=4, pady=12, sticky="we")

        # Build the add client button and attach to show_add_client() handler
        btn_add_client = tk.Button(frm_client_buttons, text="Add Client", width=16, command=self.show_add_client)
        btn_add_client.grid(row=0, column=0, sticky="w")

        # Space the two buttons
        lbl_spacer_1 = tk.Label(frm_client_buttons, text="", width=7)
        lbl_spacer_1.grid(row=0, column=1, sticky="we")

        # Build the remove client button and attach to show_remove_client() handler, note - the reference to this widget
        # needs to be made available to the select_client() handler, so it is declared as class scope
        PartialGUI.__btn_remove_client = tk.Button(frm_client_buttons, text="Remove Client", width=16,
                                                   state="disabled", command=self.show_remove_client)
        PartialGUI.__btn_remove_client.grid(row=0, column=2, sticky="e")

        # Build the client data display area using a labelled frame container widget
        lbf_client_data = tk.LabelFrame(PartialGUI.__wnd_main, text="Selected Client", height=200)
        lbf_client_data.grid(row=4, column=1, padx=4, pady=4, sticky="nesw")
        lbf_client_data.grid_propagate(0)  # This ensures that the labelled frame can be given a set width

        # Build the message widget that will display the client data
        msg_client_data = tk.Message(lbf_client_data, textvariable=PartialGUI.__var_selected_client_data,
                                     anchor="w", justify="left", aspect=9999)  # Set aspect ratio to large number
        msg_client_data.grid(row=0, column=0, padx=4, pady=4, sticky="we")

        # Bind the clients list box data model to the list of clients currently held in the main application instance
        PartialGUI.__var_clients.set(value=self.main_app.get_all_clients())

        # Update the message widget's bound variable to the string returned by the selected client's make_displayable()
        # method (i.e. as if the client data was being displayed in the MenuUI version of the application), this is
        # only done if there are clients held in the main application, note - the remove client button starts as
        # disabled and is only enabled if there is a selected client
        if PartialGUI.__var_clients.get():
            PartialGUI.__lst_clients.select_set(0)  # Select the first entry in the clients list box
            PartialGUI.__var_selected_client_data.set(self.main_app.get_all_clients()
                                                 [PartialGUI.__lst_clients.curselection()[0]].make_displayable())
            PartialGUI.__btn_remove_client.config(state="normal")

        # -------------------------------------------------------------------------------------------------------------

        # Build the contractor related list boxes, add button, remove button and details display area, note - this is
        # identical to the way the client related widgets are build and bound to their variables so see above for more
        # detailed comments on this
        lbl_spacer_2 = tk.Label(PartialGUI.__wnd_main, text="", anchor="w", width=1)
        lbl_spacer_2.grid(row=1, column=3, pady=4)

        lbl_contractor_list = tk.Label(PartialGUI.__wnd_main, text="Contractors", anchor="w", width=8)
        lbl_contractor_list.grid(row=0, column=4, padx=4, pady=4, sticky="we")

        sbr_contractors_hori = tk.Scrollbar(PartialGUI.__wnd_main, orient="horizontal")
        sbr_contractors_hori.grid(row=2, column=4, sticky="nesw")
        sbr_contractors_vert = tk.Scrollbar(PartialGUI.__wnd_main)
        sbr_contractors_vert.grid(row=1, column=5, sticky="nesw")

        PartialGUI.__lst_contractors = tk.Listbox(PartialGUI.__wnd_main, listvariable=PartialGUI.__var_contractors,
                                                  activestyle="none",
                                                  xscrollcommand=sbr_contractors_hori.set,
                                                  yscrollcommand=sbr_contractors_vert.set,
                                                  width=50, height=12)
        PartialGUI.__lst_contractors.grid(row=1, column=4, padx=4, pady=4, sticky="nesw")
        PartialGUI.__lst_contractors.bind('<<ListboxSelect>>', self.select_contractor)

        sbr_contractors_hori.config(command=PartialGUI.__lst_contractors.xview)
        sbr_contractors_vert.config(command=PartialGUI.__lst_contractors.yview)

        frm_contractor_buttons = tk.Frame(PartialGUI.__wnd_main)
        frm_contractor_buttons.grid(row=3, column=4, padx=4, pady=12, sticky="we")

        btn_add_contractor = tk.Button(frm_contractor_buttons, text="Add Contractor", command=self.show_add_contractor,
                                       width=16)
        btn_add_contractor.grid(row=0, column=0, sticky="w")

        # Space the two buttons
        lbl_spacer_3 = tk.Label(frm_contractor_buttons, text="", width=7)
        lbl_spacer_3.grid(row=0, column=1, sticky="we")

        PartialGUI.__btn_remove_contractor = tk.Button(frm_contractor_buttons, text="Remove Contractor", width=16,
                                                       state="disabled", command=self.show_remove_contractor)
        PartialGUI.__btn_remove_contractor.grid(row=0, column=2, sticky="e")

        lbf_contractor_data = tk.LabelFrame(PartialGUI.__wnd_main, text="Selected Contractor")
        lbf_contractor_data.grid(row=4, column=4, padx=4, pady=4, sticky="nesw")

        msg_contractor_data = tk.Message(lbf_contractor_data, textvariable=PartialGUI.__var_selected_contractor_data,
                                         anchor="w", justify="left", aspect=9999)
        msg_contractor_data.grid(row=0, column=0, padx=4, pady=4, sticky="we")

        PartialGUI.__var_contractors.set(value=self.main_app.get_all_contractors())

        if PartialGUI.__var_contractors.get():
            PartialGUI.__lst_contractors.select_set(0)
            PartialGUI.__var_selected_contractor_data.set(self.main_app.get_all_contractors()
                                                     [PartialGUI.__lst_contractors.curselection()[0]].
                                                          make_displayable())
            PartialGUI.__btn_remove_contractor.config(state="normal")

        # -------------------------------------------------------------------------------------------------------------

        # Build the contract related list boxes, add button, remove button and details display area, note - this is
        # identical to the way the client related widgets are build and bound to their variables so see above for more
        # detailed comments on this
        lbl_spacer_4 = tk.Label(PartialGUI.__wnd_main, text="", anchor="w", width=1)
        lbl_spacer_4.grid(row=1, column=6, pady=4)

        lbl_contract_list = tk.Label(PartialGUI.__wnd_main, text="Contracts", anchor="w", width=8)
        lbl_contract_list.grid(row=0, column=7, padx=4, pady=4, sticky="we")

        sbr_contracts_hori = tk.Scrollbar(PartialGUI.__wnd_main, orient="horizontal")
        sbr_contracts_hori.grid(row=2, column=7, sticky="nesw")
        sbr_contracts_vert = tk.Scrollbar(PartialGUI.__wnd_main)
        sbr_contracts_vert.grid(row=1, column=8, sticky="nesw")

        PartialGUI.__lst_contracts = tk.Listbox(PartialGUI.__wnd_main, listvariable=PartialGUI.__var_contracts,
                                   activestyle="none",
                                   xscrollcommand=sbr_contracts_hori.set,
                                   yscrollcommand=sbr_contracts_vert.set,
                                   width=50, height=12)
        PartialGUI.__lst_contracts.grid(row=1, column=7, padx=4, pady=4, sticky="nesw")
        PartialGUI.__lst_contracts.bind('<<ListboxSelect>>', self.select_contract)

        sbr_contracts_hori.config(command=PartialGUI.__lst_contracts.xview)
        sbr_contracts_vert.config(command=PartialGUI.__lst_contracts.yview)

        frm_contract_buttons = tk.Frame(PartialGUI.__wnd_main)
        frm_contract_buttons.grid(row=3, column=7, padx=4, pady=12, sticky="we")

        btn_add_contract = tk.Button(frm_contract_buttons, text="Add Contract", command=self.show_add_contract,
                                       width=16)
        btn_add_contract.grid(row=0, column=0, sticky="w")

        # Space the two buttons
        lbl_spacer_5 = tk.Label(frm_contract_buttons, text="", width=7)
        lbl_spacer_5.grid(row=0, column=1, sticky="we")

        PartialGUI.__btn_remove_contract = tk.Button(frm_contract_buttons, text="Remove Contract", width=16,
                                                     state="disabled", command=self.show_remove_contract)
        PartialGUI.__btn_remove_contract.grid(row=0, column=2, sticky="e")

        lbf_contract_data = tk.LabelFrame(PartialGUI.__wnd_main, text="Selected Contract")
        lbf_contract_data.grid(row=4, column=7, padx=4, pady=4, sticky="nesw")

        msg_contract_data = tk.Message(lbf_contract_data, textvariable=PartialGUI.__var_selected_contract_data,
                                       anchor="w", justify="left", aspect=9999)
        msg_contract_data.grid(row=0, column=0, padx=4, pady=4, sticky="we")

        PartialGUI.__var_contracts.set(value=self.main_app.get_all_contracts())

        if PartialGUI.__var_contracts.get():
            PartialGUI.__lst_contracts.select_set(0)
            PartialGUI.__var_selected_contract_data.set(self.main_app.get_all_contracts()
                                                   [PartialGUI.__lst_contracts.curselection()[0]].make_displayable())
            PartialGUI.__btn_remove_contract.config(state="normal")

        # -------------------------------------------------------------------------------------------------------------

        # Start up the main loop that the main window of the GUI runs upon
        PartialGUI.__wnd_main.mainloop()

    def select_client(self, evt):
        """
        Handler to respond to the selection of a different client in the clients list box

        :param evt: event instance that this handler is responding to
        :return: None
        """
        # Ensure there is a selected client, list of selected clients will be empty of none are currently selected
        if evt.widget.curselection():
            PartialGUI.__var_selected_client_data.set(self.main_app.get_all_clients()[evt.widget.curselection()[0]].
                                                      make_displayable())
            PartialGUI.__btn_remove_client.config(state="normal")
        else:
            PartialGUI.__btn_remove_client.config(state="disabled")

    def show_add_client(self):
        """
        Shows a dialog for entering a new client, is accepted and the add_client() method called on the main application
        when the ok button is pressed (use cancel button or close the dialog via the X control to abort this add
        function), note - the ok button cannot be successfully used if the name entry widget is blank

        :return: None
        """
        # Specify dimensions of add client dialog
        w = 400  # Width for the add client dialog
        h = 100  # Height for the add client dialog

        # Get the current position of the main dialog
        x = PartialGUI.__wnd_main.winfo_x()  # X coordinate of the main window
        y = PartialGUI.__wnd_main.winfo_y()  # Y coordinate of the main window

        # Offset the x and y coordinates for the add client dialog relative to the main window
        x += 30
        y += 260

        # Create the add client dialog as a Toplevel widget
        PartialGUI.__wnd_add_client = tk.Toplevel(PartialGUI.__wnd_main)

        # Entitle the add client dialog
        PartialGUI.__wnd_add_client.title("Add Client")

        # Force the add client dialog to act in a modal (i.e. exclusive) fashion, it has no minimise, maximise or resize
        # functionality and has to be dismissed before access to the main window is returned
        PartialGUI.__wnd_add_client.attributes("-toolwindow", True)  # Remove minimise and maximise decorations
        PartialGUI.__wnd_add_client.transient(PartialGUI.__wnd_main)  # Always show on top of main window
        PartialGUI.__wnd_add_client.resizable(False, False)  # Cannot be resized
        PartialGUI.__wnd_add_client.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))  # Set size and position
        PartialGUI.__wnd_add_client.lift()  # Bring to front of the main window
        PartialGUI.__wnd_add_client.focus_force()  # Force dialog to retain any focus
        PartialGUI.__wnd_add_client.grab_set()  # Prevent access to main window

        # -------------------------------------------------------------------------------------------------------------

        # Build the add client dialog widgets
        lbl_name = tk.Label(PartialGUI.__wnd_add_client, text="Name: ", anchor="w", width=6)
        lbl_name.grid(row=0, column=0, padx=4, pady=4, sticky="we")

        # Clear the name entry variable
        PartialGUI.__var_name.set("")
        ent_name = tk.Entry(PartialGUI.__wnd_add_client, textvariable=PartialGUI.__var_name, width=36)
        ent_name.grid(row=0, column=1, padx=4, pady=4, sticky="we")

        # Add a frame to contain the ok and cancel buttons
        frm_okcancel_buttons = tk.Frame(PartialGUI.__wnd_add_client)
        frm_okcancel_buttons.grid(row=1, column=0, columnspan=2, padx=4, pady=12, sticky="we")

        # Space the buttons towards right side of frame
        lbl_spacer_0 = tk.Label(frm_okcancel_buttons, text="", width=18)
        lbl_spacer_0.grid(row=0, column=0, sticky="w")

        # Call the add_client() handler when this button is clicked
        PartialGUI.__btn_ok = tk.Button(frm_okcancel_buttons, text="Ok", width=8, command=self.add_client)
        PartialGUI.__btn_ok.grid(row=0, column=1, sticky="w")

        # Small space between the buttons
        lbl_spacer_1 = tk.Label(frm_okcancel_buttons, text="", width=1)
        lbl_spacer_1.grid(row=0, column=2, sticky="w")

        # Abort the dialog without adding a client
        PartialGUI.__btn_cancel = tk.Button(frm_okcancel_buttons, text="Cancel", width=8,
                                            command=PartialGUI.__wnd_add_client.destroy)
        PartialGUI.__btn_cancel.grid(row=0, column=3, sticky="w")


    def add_client(self):
        """
        Add a new client using the data entered into the add client dialog by calling the add_client() method of the
        main application and then destroy the add client dialog, note - if the name entry widget variable is blank then
        display an error message box, do not add a new client and return to the show_add_client() dialog

        :return: None
        """
        # Close down the add client dialog, it is now not needed
        PartialGUI.__wnd_add_client.destroy()

        # Check to see if user entered a blank name, blank means only contains whitespace so strip it of all whitespace
        # first and this will leave an empty string if it is blank
        if not PartialGUI.__var_name.get().strip():
            # Show the error message box
            mb.showerror(title="Cannot Add Client", message="Name cannot be blank")
            # Re-call the show add client dialog
            self.show_add_client()
            # Abort from this invocation of the add client method
            return

        # Call the main app add client method using the name entered into the add client dialog
        success, client = self.main_app.add_client(PartialGUI.__var_name.get())

        # If the add client method fails then show an error message box and abort
        if not success:
            mb.showerror(title="Cannot Add Client", message=client)
            return

        # If this is successful then update the client list box to include this new client
        PartialGUI.__var_clients.set(value=self.main_app.get_all_clients())

        # Deselect any existing selected client then select the newly added client (which will be the last in the main
        # app clients list) in the clients list box, update the client data display and ensure the remove client button
        # is enabled
        PartialGUI.__lst_clients.selection_clear(0, tk.END)
        PartialGUI.__lst_clients.select_set(len(self.main_app.get_all_clients()) - 1)
        PartialGUI.__var_selected_client_data.set(self.main_app.get_all_clients()
                                                  [PartialGUI.__lst_clients.curselection()[0]].make_displayable())
        PartialGUI.__btn_remove_client.config(state="normal")

    def show_remove_client(self):
        """
        Shows a confirmation dialog to confirm that the selected client should be removed from the list of clients held
        in the main application

        :return: None
        """
        # Get identifier of the selected client that is about to be removed
        ident = self.main_app.get_all_clients()[PartialGUI.__lst_clients.curselection()[0]].id

        # Use Yes/No message box to ask for confirmation of removal from the user
        if mb.askyesno(title="Are You Sure?", message="Do you really want to remove client with Id: {0}".
                    format(ident)):
            # Yes confirmed so remove the selected client
            self.remove_client(ident)

    def remove_client(self, ident):
        """
        Remove the selected client by calling the remove_client() method of the main app

        :param ident: identifier of the client to remove
        :return: None
        """
        # Call the main app remove_client() method using the id of the selected client item in the clients list box,
        # this is one reason why the clients list box widget reference has to be of class scope, note - removal of the
        # selected client will fail if it is an owner of an existing contract, if this occurs show an error message
        # box informing the user of this fact and abort
        success, msg = self.main_app.remove_client(ident)

        # If removal was not successful then show error box
        if not success:
            mb.showerror(title="Cannot Remove Client", message=msg)
            return

        # Reset the clients list box items
        PartialGUI.__var_clients.set(value=self.main_app.get_all_clients())

        # Clear the existing client selection from the clients list box and clear the selected client data display
        PartialGUI.__lst_clients.selection_clear(0, tk.END)
        PartialGUI.__var_selected_client_data.set("")

        # If there are clients in the clients list box then select the very first and update the selected client data
        # display, otherwise disable the remove client button
        if PartialGUI.__var_clients.get():
            PartialGUI.__lst_clients.select_set(0)
            PartialGUI.__var_selected_client_data.set(self.main_app.get_all_clients()
                                                      [PartialGUI.__lst_clients.curselection()[0]].make_displayable())
        else:
            PartialGUI.__btn_remove_client.config(state="disabled")

    def select_contractor(self, evt):
        """
        Handler to respond to the selection of a different contractor in the contractors list box

        :param evt: event instance that this handler is responding to
        :return: None
        """
        # Ensure there is a selected contractor, list of selected contractors will be empty of none are currently
        # selected
        if evt.widget.curselection():
            PartialGUI.__var_selected_contractor_data.set(self.main_app.get_all_contractors()
                                                          [evt.widget.curselection()[0]].
                                                          make_displayable())
            PartialGUI.__btn_remove_contractor.config(state="normal")
        else:
            PartialGUI.__btn_remove_contractor.config(state="disabled")

    def show_add_contractor(self):
        """
        Shows a dialog for entering a new contractor, is accepted and the add_contractor() method called on the main
        application when the ok button is pressed (use cancel button or close the dialog via the X control to abort this
        add function), note - the ok button cannot be successfully used if the name entry widget or the speciality
        entry widget is blank

        :return: None
        """
        # Specify dimensions of add contractor dialog
        w = 400  # Width for the add contractor dialog
        h = 132  # Height for the add contractor dialog

        # Get the current position of the main dialog
        x = PartialGUI.__wnd_main.winfo_x()  # X coordinate of the main window
        y = PartialGUI.__wnd_main.winfo_y()  # Y coordinate of the main window

        # Offset the x and y coordinates for the add contractor dialog relative to the main window
        x += 368
        y += 260

        # Create the add contractor dialog as a Toplevel widget
        PartialGUI.__wnd_add_contractor = tk.Toplevel(PartialGUI.__wnd_main)

        # Entitle the add contractor dialog
        PartialGUI.__wnd_add_contractor.title("Add Contractor")

        # Force the add contractor dialog to act in a modal (i.e. exclusive) fashion, it has no minimise, maximise or
        # resize functionality and has to be dismissed before access to the main window is returned
        PartialGUI.__wnd_add_contractor.attributes("-toolwindow", True)  # Remove minimise and maximise decorations
        PartialGUI.__wnd_add_contractor.transient(PartialGUI.__wnd_main)  # Always show on top of main window
        PartialGUI.__wnd_add_contractor.resizable(False, False)  # Cannot be resized
        PartialGUI.__wnd_add_contractor.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))  # Set size and position
        PartialGUI.__wnd_add_contractor.lift()  # Bring to front of the main window
        PartialGUI.__wnd_add_contractor.focus_force()  # Force dialog to retain any focus
        PartialGUI.__wnd_add_contractor.grab_set()  # Prevent access to main window

        # -------------------------------------------------------------------------------------------------------------

        # Build the add contractor dialog widgets
        lbl_name = tk.Label(PartialGUI.__wnd_add_contractor, text="Name: ", anchor="w", width=7)
        lbl_name.grid(row=0, column=0, padx=4, pady=4, sticky="we")

        # Clear the name entry variable
        PartialGUI.__var_name.set("")
        ent_name = tk.Entry(PartialGUI.__wnd_add_contractor, textvariable=PartialGUI.__var_name, width=36)
        ent_name.grid(row=0, column=1, padx=4, pady=4, sticky="we")

        lbl_speciality = tk.Label(PartialGUI.__wnd_add_contractor, text="Speciality: ", anchor="w", width=7)
        lbl_speciality.grid(row=1, column=0, padx=4, pady=4, sticky="we")

        # Clear the speciality entry variable
        PartialGUI.__var_speciality.set("")
        ent_speciality = tk.Entry(PartialGUI.__wnd_add_contractor, textvariable=PartialGUI.__var_speciality, width=36)
        ent_speciality.grid(row=1, column=1, padx=4, pady=4, sticky="we")

        # Add a frame to contain the ok and cancel buttons
        frm_okcancel_buttons = tk.Frame(PartialGUI.__wnd_add_contractor)
        frm_okcancel_buttons.grid(row=2, column=0, columnspan=2, padx=4, pady=12, sticky="we")

        # Space the buttons towards right side of frame
        lbl_spacer_0 = tk.Label(frm_okcancel_buttons, text="", width=18)
        lbl_spacer_0.grid(row=0, column=0, sticky="w")

        # Call the add_contractor() handler when this button is clicked
        PartialGUI.__btn_ok = tk.Button(frm_okcancel_buttons, text="Ok", width=8, command=self.add_contractor)
        PartialGUI.__btn_ok.grid(row=0, column=1, sticky="w")

        # Small space between the buttons
        lbl_spacer_1 = tk.Label(frm_okcancel_buttons, text="", width=1)
        lbl_spacer_1.grid(row=0, column=2, sticky="w")

        # Abort the dialog without adding a contractor
        PartialGUI.__btn_cancel = tk.Button(frm_okcancel_buttons, text="Cancel", width=8,
                                            command=PartialGUI.__wnd_add_contractor.destroy)
        PartialGUI.__btn_cancel.grid(row=0, column=3, sticky="w")

    def add_contractor(self):
        """
        Add a new contractor using the data entered into the add contractor dialog by calling the add_contractor()
        method of the main application and then destroy the add contractor dialog

        :return: None
        """
        # Close down the add contractor dialog, it is now not needed
        PartialGUI.__wnd_add_contractor.destroy()

        # Check to see if user entered a blank name, blank means only contains whitespace so strip it of all whitespace
        # first and this will leave an empty string if it is blank
        if not PartialGUI.__var_name.get().strip():
            # Show the error message box
            mb.showerror(title="Cannot Add Contractor", message="Name cannot be blank")
            # Re-call the show add contractor dialog
            self.show_add_contractor()
            # Abort from this invocation of the add contractor method
            return

        # Check to see if user entered a blank speciality, blank means only contains whitespace so strip it of all
        # whitespace first and this will leave an empty string if it is blank
        if not PartialGUI.__var_speciality.get().strip():
            # Show the error message box
            mb.showerror(title="Cannot Add Contractor", message="Speciality cannot be blank")
            # Re-call the show add contractor dialog
            self.show_add_contractor()
            # Abort from this invocation of the add contractor method
            return

        # Call the main app add contractor method using the name and speciality entered into the add contractor dialog
        success, contractor = self.main_app.add_contractor(PartialGUI.__var_name.get(),
                                                           PartialGUI.__var_speciality.get())

        # If the add contractor method fails then show an error message box and abort
        if not success:
            mb.showerror(title="Cannot Add Contractor", message=contractor)
            return

        # If this is successful then update the contractor list box to include this new contractor
        PartialGUI.__var_contractors.set(value=self.main_app.get_all_contractors())

        # Deselect any existing selected contractor then select the newly added contractor (which will be the last in
        # the main app contractors list) in the contractors list box, update the contractor data display and ensure the
        # remove client button is enabled
        PartialGUI.__lst_contractors.selection_clear(0, tk.END)
        PartialGUI.__lst_contractors.select_set(len(self.main_app.get_all_contractors()) - 1)
        PartialGUI.__var_selected_contractor_data.set(self.main_app.get_all_contractors()
                                                      [PartialGUI.__lst_contractors.curselection()[0]].
                                                      make_displayable())
        PartialGUI.__btn_remove_contractor.config(state="normal")

    def show_remove_contractor(self):
        """
        Shows a confirmation dialog to confirm that the selected contractor should be removed from the list of
        contractors held in the main application

        :return: None
        """
        # Get identifier of the selected contractor that is about to be removed
        ident = self.main_app.get_all_contractors()[PartialGUI.__lst_contractors.curselection()[0]].id

        # Use Yes/No message box to ask for confirmation of removal from the user
        if mb.askyesno(title="Are You Sure?", message="Do you really want to remove contractor with Id: {0}".
            format(ident)):
            # Yes confirmed so remove the selected contractor
            self.remove_contractor(ident)

    def remove_contractor(self, ident):
        """
        Remove the selected contractor by calling the remove_contractor() method of the main app

        :param ident: identifier of the contractor to remove
        :return: None
        """
        # Call the main app remove_contractor() method using the id of the selected contractor item in the contractors
        # list box, this is one reason why the contractors list box widget reference has to be of class scope, note -
        # removal of the selected contractor will fail if it is allocated to an existing contract, if this occurs show
        # an error message box informing the user of this fact and abort
        success, msg = self.main_app.remove_contractor(ident)

        # If removal was not successful then show error box
        if not success:
            mb.showerror(title="Cannot Remove Contractor", message=msg)
            return

        # Reset the contractors list box items
        PartialGUI.__var_contractors.set(value=self.main_app.get_all_contractors())

        # Clear the existing contractor selection from the contractors list box and clear the selected contractor data
        # display
        PartialGUI.__lst_contractors.selection_clear(0, tk.END)
        PartialGUI.__var_selected_contractor_data.set("")

        # If there are contractors in the contractors list box then select the very first and update the selected
        # contractor data display, otherwise disable the remove contractor button
        if PartialGUI.__var_contractors.get():
            PartialGUI.__lst_contractors.select_set(0)
            PartialGUI.__var_selected_contractor_data.set(self.main_app.get_all_contractors()
                                                          [PartialGUI.__lst_contractors.curselection()[0]].
                                                          make_displayable())
        else:
            PartialGUI.__btn_remove_contractor.config(state="disabled")

    def select_contract(self, evt):
        """
        Handler to respond to the selection of a different contract in the contracts list box

        :param evt: event instance that this handler is responding to
        :return: None
        """
        # Ensure there is a selected contract, list of selected contracts will be empty if none are currently selected,
        # if none selected then disable the remove contract button, enable this button if there is a selected contract
        if evt.widget.curselection():
            PartialGUI.__var_selected_contract_data.set(self.main_app.get_all_contracts()[evt.widget.curselection()[0]].
                                                        make_displayable())
            PartialGUI.__btn_remove_contract.config(state="normal")
        else:
            PartialGUI.__btn_remove_contract.config(state="disabled")

    def show_add_contract(self):
        """
        Shows a dialog for entering a new contract, is accepted and the add_contract() method called on the main
        application when the ok button is pressed (use cancel button or close the dialog via the X control to abort this
        add function), note - this will show an error message box and abort after closing this message box if there are
        no clients available to use as owners, also the ok button cannot be successfully used if the speciality entry
        widget is blank

        :return: None
        """
        # Specify dimensions of add contract dialog
        w = 400  # Width for the add contract dialog
        h = 450  # Height for the add contract dialog

        # Get the current position of the main dialog
        x = PartialGUI.__wnd_main.winfo_x()  # X coordinate of the main window
        y = PartialGUI.__wnd_main.winfo_y()  # Y coordinate of the main window

        # Offset the x and y coordinates for the add contract dialog relative to the main window
        x += 710
        y += 260

        # Create the add contract dialog as a Toplevel widget
        PartialGUI.__wnd_add_contract = tk.Toplevel(PartialGUI.__wnd_main)

        # Entitle the add contract dialog
        PartialGUI.__wnd_add_contract.title("Add Contract")

        # Force the add contract dialog to act in a modal (i.e. exclusive) fashion, it has no minimise, maximise or
        # resize functionality and has to be dismissed before access to the main window is returned
        PartialGUI.__wnd_add_contract.attributes("-toolwindow", True)  # Remove minimise and maximise decorations
        PartialGUI.__wnd_add_contract.transient(PartialGUI.__wnd_main)  # Always show on top of main window
        PartialGUI.__wnd_add_contract.resizable(False, False)  # Cannot be resized
        PartialGUI.__wnd_add_contract.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))  # Set size and position
        PartialGUI.__wnd_add_contract.lift()  # Bring to front of the main window
        PartialGUI.__wnd_add_contract.focus_force()  # Force dialog to retain any focus
        PartialGUI.__wnd_add_contract.grab_set()  # Prevent access to main window

        # -------------------------------------------------------------------------------------------------------------

        # Build the add contract dialog widgets
        lbl_type = tk.Label(PartialGUI.__wnd_add_contract, text="Type: ", anchor="w", width=5)
        lbl_type.grid(row=0, column=1, padx=4, pady=4, sticky="we")

        # Add radio buttons to allow user to select the contract type
        col = 2
        PartialGUI.__var_contract_type.set(PartialGUI.__CONTRACT_TYPES[0][1])  # Initially Base contract type is set
        for text, contract_type in PartialGUI.__CONTRACT_TYPES:
            rbn_contract_type = tk.Radiobutton(PartialGUI.__wnd_add_contract, text=text,
                                               variable=PartialGUI.__var_contract_type, value=contract_type)
            rbn_contract_type.grid(row=0, column=col)
            col += 1

        # Build the owner related list box
        lbl_owners_list = tk.Label(PartialGUI.__wnd_add_contract, text="Owners: ", anchor="w")
        lbl_owners_list.grid(row=1, column=1, padx=4, pady=4, sticky="we")

        lbl_spacer_0 = tk.Label(PartialGUI.__wnd_add_contract, text="", anchor="w", width=1)
        lbl_spacer_0.grid(row=2, column=0, pady=4)

        # Build the horizontal and vertical scrollbars attached to the owners list box
        sbr_owners_hori = tk.Scrollbar(PartialGUI.__wnd_add_contract, orient="horizontal")
        sbr_owners_hori.grid(row=3, column=1, columnspan=4, sticky="nesw")
        sbr_owners_vert = tk.Scrollbar(PartialGUI.__wnd_add_contract, orient="vertical")
        sbr_owners_vert.grid(row=2, column=5, sticky="nesw")

        # Build the owners list box
        PartialGUI.__lst_owners = tk.Listbox(PartialGUI.__wnd_add_contract, listvariable=PartialGUI.__var_clients,
                                             activestyle="none",
                                             xscrollcommand=sbr_owners_hori.set,
                                             yscrollcommand=sbr_owners_vert.set,
                                             height=12)
        PartialGUI.__lst_owners.grid(row=2, column=1, columnspan=4, sticky="nesw")
        PartialGUI.__lst_owners.bind('<<ListboxSelect>>', self.select_owner)

        # Attach owners list box to its horizontal and vertical scrollbars
        sbr_owners_hori.config(command=PartialGUI.__lst_owners.xview)
        sbr_owners_vert.config(command=PartialGUI.__lst_owners.yview)

        # Build the speciality related widgets
        lbl_speciality = tk.Label(PartialGUI.__wnd_add_contract, text="Speciality: ", anchor="w")
        lbl_speciality.grid(row=4, column=1, padx=4, pady=4, sticky="we")

        # Clear the speciality entry variable, build the speciality entry widget
        PartialGUI.__var_speciality.set("")
        ent_speciality = tk.Entry(PartialGUI.__wnd_add_contract, textvariable=PartialGUI.__var_speciality)
        ent_speciality.grid(row=4, column=2, columnspan=3, padx=4, pady=4, sticky="we")

        # Build the payment related widgets
        lbl_payment = tk.Label(PartialGUI.__wnd_add_contract, text="Payment: £", anchor="w")
        lbl_payment.grid(row=5, column=1, padx=4, pady=4, sticky="we")

        # Clear the payment entry variable, build the payment entry widget
        PartialGUI.__var_payment.set(0.0)
        ent_payment = tk.Entry(PartialGUI.__wnd_add_contract, textvariable=PartialGUI.__var_payment)
        ent_payment.grid(row=5, column=2, columnspan=3, padx=4, pady=4, sticky="we")

        # Add a frame to contain the ok and cancel buttons
        frm_okcancel_buttons = tk.Frame(PartialGUI.__wnd_add_contract)
        frm_okcancel_buttons.grid(row=6, column=0, columnspan=5, padx=4, pady=12, sticky="we")

        # Space the buttons towards right side of frame
        lbl_spacer_1 = tk.Label(frm_okcancel_buttons, text="", width=19)
        lbl_spacer_1.grid(row=0, column=0, sticky="w")

        # Call the add_contract() handler when this button is clicked, button is initially disabled until an owner is
        # selected in the owners list
        PartialGUI.__btn_ok = tk.Button(frm_okcancel_buttons, state="disabled", text="Ok", width=8,
                                        command=self.add_contract)
        PartialGUI.__btn_ok.grid(row=0, column=1, sticky="w")

        # Small space between the buttons
        lbl_spacer_2 = tk.Label(frm_okcancel_buttons, text="", width=1)
        lbl_spacer_2.grid(row=0, column=2, sticky="w")

        # Abort the dialog without adding a contract
        PartialGUI.__btn_cancel = tk.Button(frm_okcancel_buttons, text="Cancel", width=8,
                                            command=PartialGUI.__wnd_add_contract.destroy)
        PartialGUI.__btn_cancel.grid(row=0, column=3, sticky="w")

    def select_owner(self, evt):
        """
        Use this handler to enable and disable the ok button on the add contract dialog to mirror the existance of a
        selected owner in the owners list

        :return: None
        """
        # If there is a selected owner in the owners list then set the ok button to enabled and update the owner id
        # variable, else disable to ok button and set owner id to None
        if evt.widget.curselection():
            PartialGUI.__btn_ok.config(state="normal")
            PartialGUI.__var_owner_id.set(self.main_app.get_all_clients()[evt.widget.curselection()[0]].id)
        else:
            PartialGUI.__btn_ok.config(state="disabled")
            PartialGUI.__var_owner_id.set(None)

    def add_contract(self):
        """
        Add a new contract using the data entered into the add contract dialog by calling the add_contract() method of
        the main application and then destroy the add contract dialog

        :return: None
        """
        # Close down the add contract dialog, it is now not needed
        PartialGUI.__wnd_add_contract.destroy()

        # Check to see if user entered a blank speciality, blank means only contains whitespace so strip it of all
        # whitespace first and this will leave an empty string if it is blank
        if not PartialGUI.__var_speciality.get().strip():
            # Show the error message box
            mb.showerror(title="Cannot Add Contract", message="Speciality cannot be blank")
            # Re-call the show add contract dialog
            self.show_add_contract()
            # Abort from this invocation of the add contract method
            return

        # Call the main app add contract method using the name and speciality entered into the add contract dialog
        success, contract = self.main_app.add_contract(PartialGUI.__var_contract_type.get(),
                                                       self.main_app.get_client(PartialGUI.__var_owner_id.get()),
                                                       PartialGUI.__var_speciality.get(),
                                                       PartialGUI.__var_payment.get())

        # If the add contract method fails then show an error message box and abort
        if not success:
            mb.showerror(title="Cannot Add Contract", message=contract)
            return

        # If this is successful then update the contract list box to include this new contract
        PartialGUI.__var_contracts.set(value=self.main_app.get_all_contracts())

        # Deselect any existing selected contract then select the newly added contract (which will be the last in the
        # main app contracts list) in the contracts list box, update the contract data display and ensure the remove
        # contract button is enabled
        PartialGUI.__lst_contracts.selection_clear(0, tk.END)
        PartialGUI.__lst_contracts.select_set(len(self.main_app.get_all_contracts()) - 1)
        PartialGUI.__var_selected_contract_data.set(self.main_app.get_all_contracts()
                                                    [PartialGUI.__lst_contracts.curselection()[0]].
                                                    make_displayable())
        PartialGUI.__btn_remove_contract.config(state="normal")

    def show_remove_contract(self):
        """
        Shows a confirmation dialog to confirm that the selected contract should be removed from the list of contracts
        held in the main application

        :return: None
        """
        # Get identifier of the selected contract that is about to be removed
        ident = self.main_app.get_all_contracts()[PartialGUI.__lst_contracts.curselection()[0]].id

        # Use Yes/No message box to ask for confirmation of removal from the user
        if mb.askyesno(title="Are You Sure?", message="Do you really want to remove contract with Id: {0}".
            format(ident)):
            # Yes confirmed so remove the selected contract
            self.remove_contract(ident)

    def remove_contract(self, ident):
        """
        Remove the selected contractor by calling the remove_contractor() method of the main app

        :param ident: identifier of the contract to remove
        :return:
        """
        # Call the main app remove_contract() method using the id of the selected contract item in the contracts list
        #  box, this is one reason why the contracts list box widget reference has to be of class scope, note -
        # removal of the selected contract will fail if it is not completed and has an allocated contractor, if this
        # occurs show an error message box informing the user of this fact and abort
        success, msg = self.main_app.remove_contract(ident)

        # If removal was not successful then show error box
        if not success:
            mb.showerror(title="Cannot Remove Contract", message=msg)
            return

        # Reset the contracts list box items
        PartialGUI.__var_contracts.set(value=self.main_app.get_all_contracts())

        # Clear the existing contract selection from the contracts list box and clear the selected contractor data
        # display
        PartialGUI.__lst_contracts.selection_clear(0, tk.END)
        PartialGUI.__var_selected_contract_data.set("")

        # If there are contracts in the contracts list box then select the very first and update the selected contract
        # data display, otherwise disable the remove contract button
        if PartialGUI.__var_contracts.get():
            PartialGUI.__lst_contracts.select_set(0)
            PartialGUI.__var_selected_contract_data.set(self.main_app.get_all_contracts()
                                                        [PartialGUI.__lst_contracts.curselection()[0]].
                                                        make_displayable())
        else:
            PartialGUI.__btn_remove_contract.config(state="disabled")
