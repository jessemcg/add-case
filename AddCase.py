#!/usr/bin/python3

import re
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, Gdk

# Assign variable to the concordance file path
k = '$HOME/add-case/concordance.sdi'

class ConcordanceFileApp(Gtk.ApplicationWindow):
    def __init__(self, app):
        super().__init__(application=app, title="Add Case")

        # Grid
        grid = Gtk.Grid()
        grid.set_column_spacing(40)
        grid.set_row_spacing(15)
        grid.set_margin_top(30)
        grid.set_margin_bottom(15)
        grid.set_margin_start(20)
        grid.set_margin_end(20)
        
        # Set the grid as the child of the window
        self.set_child(grid)
        
        # Create a ShortcutController
        shortcut_controller = Gtk.ShortcutController.new()
        self.add_controller(shortcut_controller)

        # Create a shortcut for Control+Q
        key_combination = Gtk.ShortcutTrigger.parse_string("<Control>q")
        shortcut = Gtk.Shortcut.new(key_combination, Gtk.CallbackAction.new(self.quit_app))
        shortcut_controller.add_shortcut(shortcut)

        # Input fields and their labels
        inputs = [
            ("Cal. Case", '-case_input-'),
            ("Slip Opn.", '-slip_input-'),
            ("Welf. & Inst. Code", '-welf_input-'),
            ("Pen. Code", '-pen_input-'),
            ("Fam. Code", '-fam_input-'),
            ("Evid. Code", '-evid_input-'),
            ("Code Civ. Proc.", '-proc_input-'),
            ("Rule of Court", '-rule_input-'),
            ("Fed. Code (entire cite)", '-fed_input-'),
            ("Const. (entire cite)", '-const_input-'),
        ]
        self.input_entries = {}
        for i, (label, key) in enumerate(inputs):
            self.input_entries[key] = Gtk.Entry()
            box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
            box.append(self.input_entries[key])
            grid.attach(box, 0, i, 1, 1)
            
            # Create label and set alignment to right
            label_widget = Gtk.Label.new(label)
            label_widget.set_halign(Gtk.Align.START)  # Align label to the right
            
            label_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
            label_box.append(label_widget)
            grid.attach(label_box, 1, i, 2, 1)
            
        # Submit button
        submit_button = Gtk.Button.new_with_label("Submit")
        submit_button.connect("clicked", self.submit)
        grid.attach(submit_button, 0, len(inputs), 3, 1)

        # Output label
        self.output_label = Gtk.Label.new("")
        grid.attach(self.output_label, 0, len(inputs) + 1, 3, 1)
        
        # Connect the Enter key for each entry field
        self.connect_entries()
        
    def connect_entries(self):
        for entry in self.input_entries.values():
            entry.connect("activate", self.submit)
        
    def submit(self, widget):
        values = {key: self.input_entries[key].get_text() for key in self.input_entries}

        if values['-case_input-']:
            self.add_case(values)
        if values['-slip_input-']:
            self.add_slip(values)
        if values['-welf_input-']:
            self.add_welf(values)
        if values['-pen_input-']:
            self.add_pen(values)
        if values['-fam_input-']:
            self.add_fam(values)
        if values['-evid_input-']:
            self.add_evid(values)
        if values['-proc_input-']:
            self.add_proc(values)
        if values['-rule_input-']:
            self.add_rule(values)
        if values['-fed_input-']:
            self.add_fed(values)
        if values['-const_input-']:
            self.add_const(values)

        self.output_label.set_text("submitted")

    def add_case(self, values):
        full_cite = values['-case_input-']
        short_cite = re.sub(r" \(\d{4}\) ", ",supra, ", full_cite)
        short_cite = re.sub("Cal.App.3rd.*", "Cal.App.3rd", short_cite)
        short_cite = re.sub("Cal.App.4th.*", "Cal.App.4th", short_cite)
        short_cite = re.sub("Cal.App.5th.*", "Cal.App.5th", short_cite)
        short_cite = re.sub("Cal.4th.*", "Cal.4th", short_cite)
        short_cite = re.sub("Cal.5th.*", "Cal.5th", short_cite)
        short_cite = re.sub("U.S.*", "U.S.", short_cite)
        line_1 = f"{full_cite};{full_cite};Cases;;0;0"
        line_2 = f"{short_cite};{full_cite};Cases;;0;0"
        with open(k, "a") as file:
            file.write("\n" + line_1)
            file.write("\n" + line_2)

    def add_slip(self, values):
        a = values['-slip_input-']
        line_1 = f"{a};{a};Cases;;0;0"
        with open(k, "a") as file:
            file.write("\n" + line_1)

    def add_welf(self, values):
        a = values['-welf_input-']
        line_1 = f"Welf. & Inst. Code, § {a};Welf. & Inst. Code, § {a};Statutes;;0;0"
        line_2 = f"Welfare and Institutions Code section {a};Welf. & Inst. Code, § {a};Statutes;;0;0"
        with open(k, "a") as file:
            file.write("\n" + line_1)
            file.write("\n" + line_2)
            
    def add_pen(self, values):
        a = values['-pen_input-']
        line_1 = f"Pen. Code, § {a};Pen. Code, § {a};Statutes;;0;0"
        line_2 = f"Penal Code section {a};Pen. Code, § {a};Statutes;;0;0"
        with open(k, "a") as file:
            file.write("\n" + line_1)
            file.write("\n" + line_2)

    def add_fam(self, values):
        a = values['-fam_input-']
        line_1 = f"Fam. Code, § {a};Fam. Code, § {a};Statutes;;0;0"
        line_2 = f"Family Code section {a};Fam. Code, § {a};Statutes;;0;0"
        with open(k, "a") as file:
            file.write("\n" + line_1)
            file.write("\n" + line_2)

    def add_evid(self, values):
        a = values['-evid_input-']
        line_1 = f"Evid. Code, § {a};Evid. Code, § {a};Statutes;;0;0"
        line_2 = f"Evidence Code section {a};Evid. Code, § {a};Statutes;;0;0"
        with open(k, "a") as file:
            file.write("\n" + line_1)
            file.write("\n" + line_2)

    def add_proc(self, values):
        a = values['-proc_input-']
        line_1 = f"Code Civ. Proc., § {a};Code Civ. Proc., § {a};Statutes;;0;0"
        line_2 = f"Code of Civil Procedure section {a};Code Civ. Proc., § {a};Statutes;;0;0"
        with open(k, "a") as file:
            file.write("\n" + line_1)
            file.write("\n" + line_2)

    def add_rule(self, values):
        a = values['-rule_input-']
        line_1 = f"Cal. Rules of Court, rule {a};Cal. Rules of Court, rule {a};Rules of Court;;0;0"
        line_2 = f"California Rules of Court, rule {a};Cal. Rules of Court, rule {a};Rules of Court;;0;0"
        with open(k, "a") as file:
            file.write("\n" + line_1)
            file.write("\n" + line_2)

    def add_fed(self, values):
        a = values['-fed_input-']
        line_1 = f"{a};{a};Statutes;;0;0"
        with open(k, "a") as file:
            file.write("\n" + line_1)

    def add_const(self, values):
        a = values['-const_input-']
        line_1 = f"{a};{a};Constitutions;;0;0"
        with open(k, "a") as file:
            file.write("\n" + line_1)
        
    def quit_app(self, *args):
        self.get_application().quit()
	
class ConcordanceFileApplication(Gtk.Application):
    def __init__(self):
        super().__init__()

    def do_activate(self):
        win = ConcordanceFileApp(self)
        win.present()  # Use present instead of show

app = ConcordanceFileApplication()
app.run()
