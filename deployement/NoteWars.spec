# -*- mode: python -*-
a = Analysis(['../main.py'],
             pathex=['C:\\Software\\pyinstaller'],
             hiddenimports=[],
             hookspath=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=1,
          name=os.path.join('build\\pyi.win32\\main', 'NoteWars.exe'),
          debug=True,
          strip=None,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries + [('highscores.csv', '../highscores.csv', 'DATA')],
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name=os.path.join('dist', 'NoteWars'))
