# -*- mode: python -*-
import os.path
import wcwidth

a = Analysis(
    ['../capa/main.py'],
    pathex=['capa'],
    binaries=None,
    datas=[
        ('../rules', 'rules'),
        # capa.render.default uses tabulate that depends on wcwidth.
        # it seems wcwidth uses a json file `version.json`
        # and this doesn't get picked up by pyinstaller automatically.
        # so we manually embed the wcwidth resources here.
        #
        # ref: https://stackoverflow.com/a/62278462/87207
        (os.path.dirname(wcwidth.__file__), 'wcwidth')
    ],
    hiddenimports=[
        # vivisect does manual/runtime importing of its modules,
        # so declare the things that could be imported here.
        "pycparser",
        "vivisect",
        "vivisect.analysis",
        "vivisect.analysis.amd64",
        "vivisect.analysis.amd64",
        "vivisect.analysis.amd64.emulation",
        "vivisect.analysis.amd64.golang",
        "vivisect.analysis.crypto",
        "vivisect.analysis.crypto",
        "vivisect.analysis.crypto.constants",
        "vivisect.analysis.elf",
        "vivisect.analysis.elf",
        "vivisect.analysis.elf.elfplt",
        "vivisect.analysis.elf.libc_start_main",
        "vivisect.analysis.generic",
        "vivisect.analysis.generic",
        "vivisect.analysis.generic.codeblocks",
        "vivisect.analysis.generic.emucode",
        "vivisect.analysis.generic.entrypoints",
        "vivisect.analysis.generic.funcentries",
        "vivisect.analysis.generic.impapi",
        "vivisect.analysis.generic.mkpointers",
        "vivisect.analysis.generic.pointers",
        "vivisect.analysis.generic.pointertables",
        "vivisect.analysis.generic.relocations",
        "vivisect.analysis.generic.strconst",
        "vivisect.analysis.generic.switchcase",
        "vivisect.analysis.generic.thunks",
        "vivisect.analysis.i386",
        "vivisect.analysis.i386",
        "vivisect.analysis.i386.calling",
        "vivisect.analysis.i386.golang",
        "vivisect.analysis.i386.importcalls",
        "vivisect.analysis.i386.instrhook",
        "vivisect.analysis.i386.thunk_bx",
        "vivisect.analysis.ms",
        "vivisect.analysis.ms",
        "vivisect.analysis.ms.hotpatch",
        "vivisect.analysis.ms.localhints",
        "vivisect.analysis.ms.msvc",
        "vivisect.analysis.ms.msvcfunc",
        "vivisect.analysis.ms.vftables",
        "vivisect.analysis.pe",
        "vivisect.impapi.posix.amd64",
        "vivisect.impapi.posix.i386",
        "vivisect.impapi.windows",
        "vivisect.impapi.windows.amd64",
        "vivisect.impapi.windows.i386",
        "vivisect.parsers.blob",
        "vivisect.parsers.elf",
        "vivisect.parsers.ihex",
        "vivisect.parsers.macho",
        "vivisect.parsers.parse_pe",
        "vivisect.parsers.utils",
        "vivisect.storage",
        "vivisect.storage.basicfile",
        "vstruct.constants",
        "vstruct.constants.ntstatus",
        "vstruct.defs",
        "vstruct.defs.arm7",
        "vstruct.defs.bmp",
        "vstruct.defs.dns",
        "vstruct.defs.elf",
        "vstruct.defs.gif",
        "vstruct.defs.ihex",
        "vstruct.defs.inet",
        "vstruct.defs.java",
        "vstruct.defs.kdcom",
        "vstruct.defs.macho",
        "vstruct.defs.macho.const",
        "vstruct.defs.macho.fat",
        "vstruct.defs.macho.loader",
        "vstruct.defs.macho.stabs",
        "vstruct.defs.minidump",
        "vstruct.defs.pcap",
        "vstruct.defs.pe",
        "vstruct.defs.pptp",
        "vstruct.defs.rar",
        "vstruct.defs.swf",
        "vstruct.defs.win32",
        "vstruct.defs.windows",
        "vstruct.defs.windows.win_5_1_i386",
        "vstruct.defs.windows.win_5_1_i386.ntdll",
        "vstruct.defs.windows.win_5_1_i386.ntoskrnl",
        "vstruct.defs.windows.win_5_1_i386.win32k",
        "vstruct.defs.windows.win_5_2_i386",
        "vstruct.defs.windows.win_5_2_i386.ntdll",
        "vstruct.defs.windows.win_5_2_i386.ntoskrnl",
        "vstruct.defs.windows.win_5_2_i386.win32k",
        "vstruct.defs.windows.win_6_1_amd64",
        "vstruct.defs.windows.win_6_1_amd64.ntdll",
        "vstruct.defs.windows.win_6_1_amd64.ntoskrnl",
        "vstruct.defs.windows.win_6_1_amd64.win32k",
        "vstruct.defs.windows.win_6_1_i386",
        "vstruct.defs.windows.win_6_1_i386.ntdll",
        "vstruct.defs.windows.win_6_1_i386.ntoskrnl",
        "vstruct.defs.windows.win_6_1_i386.win32k",
        "vstruct.defs.windows.win_6_1_wow64",
        "vstruct.defs.windows.win_6_1_wow64.ntdll",
        "vstruct.defs.windows.win_6_2_amd64",
        "vstruct.defs.windows.win_6_2_amd64.ntdll",
        "vstruct.defs.windows.win_6_2_amd64.ntoskrnl",
        "vstruct.defs.windows.win_6_2_amd64.win32k",
        "vstruct.defs.windows.win_6_2_i386",
        "vstruct.defs.windows.win_6_2_i386.ntdll",
        "vstruct.defs.windows.win_6_2_i386.ntoskrnl",
        "vstruct.defs.windows.win_6_2_i386.win32k",
        "vstruct.defs.windows.win_6_2_wow64",
        "vstruct.defs.windows.win_6_2_wow64.ntdll",
        "vstruct.defs.windows.win_6_3_amd64",
        "vstruct.defs.windows.win_6_3_amd64.ntdll",
        "vstruct.defs.windows.win_6_3_amd64.ntoskrnl",
        "vstruct.defs.windows.win_6_3_i386",
        "vstruct.defs.windows.win_6_3_i386.ntdll",
        "vstruct.defs.windows.win_6_3_i386.ntoskrnl",
        "vstruct.defs.windows.win_6_3_wow64",
        "vstruct.defs.windows.win_6_3_wow64.ntdll",
    ],
    hookspath=['ci/hooks'],
    runtime_hooks=None,
    excludes=[
        # ignore packages that would otherwise be bundled with the .exe.
        # review: build/pyinstaller/xref-pyinstaller.html

        # we don't do any GUI stuff, so ignore these modules
        "tkinter",
        "_tkinter",
        "Tkinter",
        # tqdm provides renderers for ipython,
        # however, this drags in a lot of dependencies.
        # since we don't spawn a notebook, we can safely remove these.
        "IPython",
        "ipywidgets",
    ])

a.binaries = a.binaries - TOC([
 ('tcl85.dll', None, None),
 ('tk85.dll', None, None),
 ('_tkinter', None, None)])

pyz = PYZ(a.pure, a.zipped_data)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          exclude_binaries=False,
          name='capa',
          icon='logo.ico',
          debug=False,
          strip=None,
          upx=True,
          console=True )

# enable the following to debug the contents of the .exe
#
#coll = COLLECT(exe,
#               a.binaries,
#               a.zipfiles,
#               a.datas,
#               strip=None,
#               upx=True,
#               name='capa-dat')

