import view
import model_export as exp
import model_import as imp

def start_click():
    sol = view.get_solution()
    if sol == 1:
        name = view.get_soname()
        imp.import_data(name)
    else:
        exp.export_data()