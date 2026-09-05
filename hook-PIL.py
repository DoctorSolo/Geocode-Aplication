from PyInstaller.utils.hooks import collect_data_files, collect_submodules

datas = collect_data_files('PIL')
hiddenimports = collect_submodules('PIL') + ['_tkinter', 'tkinter']