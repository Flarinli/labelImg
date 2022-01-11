# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['labelImg.py'],
             pathex=['libs', '../LabelImg'],
             binaries=[],
             datas=[('resources/strings/strings.properties', '.')],
             hiddenimports=['xml', 'xml.etree', 'xml.etree.ElementTree', 'lxml.etree'],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='LabelImg',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
