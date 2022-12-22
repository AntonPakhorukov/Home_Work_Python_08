import view
import model_export as exp
import model_import as imp

def start_click():
    sol = view.get_solution()
    if sol == 1:
        ftype = view.get_format()
        if ftype == 1:
            name = view.get_soname()
            imp.import_data_csv(name)
        else:
            name = view.get_soname()
            imp.import_data_txt(name)
    else:
        typef = view.get_format()
        if typef == 1:
            exp.export_data_csv()
        else:
            exp.export_data_txt()