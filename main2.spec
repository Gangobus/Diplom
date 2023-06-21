# # # -*- mode: python ; coding: utf-8 -*-
# # from kivy_deps import sdl2, glew, gstreamer


# # block_cipher = None


# # a = Analysis(
# #     ['main.py'],
# #     pathex=[],
# #     binaries=[],
# #     datas=[('MediaModule.py', '.'), ('TextModule.py', '.'), ('Window.py', '.'), ('Interfase.kv', '.')],
# #     hiddenimports=[],
# #     hookspath=[],
# #     hooksconfig={},
# #     runtime_hooks=[],
# #     excludes=[],
# #     win_no_prefer_redirects=False,
# #     win_private_assemblies=False,
# #     cipher=block_cipher,
# #     noarchive=True,
# # )
# # pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

# # exe = EXE(
# #     pyz,
# #     a.scripts,
# #     [('v', None, 'OPTION')],
# #     exclude_binaries=True,
# #     name='BelScribe33',
# #     debug=False,
# #     bootloader_ignore_signals=False,
# #     strip=False,
# #     upx=True,
# #     console=False,
# #     disable_windowed_traceback=False,
# #     argv_emulation=False,
# #     target_arch=None,
# #     codesign_identity=None,
# #     entitlements_file=None,
# #     icon=['icon.ico'],
# # )
# # coll = COLLECT(
# #     exe,
# #     a.binaries,
# #     a.zipfiles,
# #     a.datas,
# #     *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins + gstreamer.dep_bins)],

# #     strip=False,
# #     upx=True,
# #     upx_exclude=[],
# #     name='BelScribe33',
# # )
# # -*- mode: python ; coding: utf-8 -*-
# from kivy_deps import sdl2, glew, gstreamer


# block_cipher = None


# a = Analysis(
#     ['main.py'],
#     pathex=[],
#     binaries=[],
#     datas=[('MediaModule.py', '.'), ('TextModule.py', '.'), ('Window.py', '.'), ('Interfase.kv', '.')],
#     hiddenimports=[],
#     hookspath=[],
#     hooksconfig={},
#     runtime_hooks=[],
#     excludes=[],
#     win_no_prefer_redirects=False,
#     win_private_assemblies=False,
#     cipher=block_cipher,
#     noarchive=True,
# )
# pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

# exe = EXE(
#     pyz,
#     a.scripts,
#     [('v', None, 'OPTION')],
#     exclude_binaries=True,
#     name='BelScribe',
#     debug=False,
#     bootloader_ignore_signals=False,
#     strip=False,
#     upx=True,
#     console=False,
#     disable_windowed_traceback=False,
#     argv_emulation=False,
#     target_arch=None,
#     codesign_identity=None,
#     entitlements_file=None,
#     icon=['icon.ico'],
# )
# coll = COLLECT(
#     exe,
#     a.binaries,
#     a.zipfiles,
#     a.datas,
#     *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins + gstreamer.dep_bins)],

#     strip=False,
#     upx=True,
#     upx_exclude=[],
#     name='BelScribe1',
#     onefile=True
# )
# -*- mode: python ; coding: utf-8 -*-
from kivy_deps import sdl2, glew, gstreamer


block_cipher = None


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('MediaModule.py', '.'), ('TextModule.py', '.'), ('Window.py', '.'), ('Interfase.kv', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=True,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [('v', None, 'OPTION')],
    exclude_binaries=True,
    name='BelScribe44',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['icon.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins + gstreamer.dep_bins)],

    strip=False,
    upx=True,
    upx_exclude=[],
    name='BelScribe44',
)