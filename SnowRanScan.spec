# -*- mode: python -*-

block_cipher = None


a = Analysis(['SnowRanScan.py'],
             pathex=['/Users/programmer/Desktop/SnowRanScan'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='SnowRanScan',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='iconfavicon2.ico')
app = BUNDLE(exe,
             name='SnowRanScan.app',
             icon='iconfavicon2.ico',
             bundle_identifier=None)
