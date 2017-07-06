import htmlPy
import os
import json
import ipdb
import pandas as pd


class Backend(htmlPy.Object):

    @htmlPy.Slot(str, result=str)
    def show_table(self, file_path):
        df = pd.read_csv(file_path)
        
        return df.style.render()


if __name__ == '__main__':
    app = htmlPy.AppGUI(title=u"htmlPy Quickstart", maximized=False, developer_mode=True)

    app.template_path = os.path.abspath(".")
    app.static_path = os.path.abspath(".")

    app.template = ("index.html", {"username": "srf"})
    app.bind(Backend())
    app.start()