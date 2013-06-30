# -*- mode: python -*-
a = Analysis(['../main.py'],
             pathex=['C:\\Software\\pyinstaller'],
             hiddenimports=[],
             hookspath=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=os.path.join('dist', 'NoteWars.exe'),
          debug=False,
          strip=None,
          upx=True,
          console=False,
          icon='../media/icon.ico')
