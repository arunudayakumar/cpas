# -*- python -*-
APPNAME = 'cpas'
VERSION = '1.08'

def set_options(ctx):
    ctx.tool_options('compiler_cc')

def configure(conf):
    conf.check_tool('compiler_cc')

def build(bld):
    # print bld.env
    bld.env.CCFLAGS.append('-DPREFIX_DIR="' + bld.env.PREFIX + '"')
    bld(features='cc cprogram',
        source='cpas.c',
        target='cpas')
    bld.install_files('${PREFIX}/include', ['stackdump.h', 'debug.h', 'eval.h', 'tsv.h', 'string_piece.h'])
    bld.install_files('${PREFIX}/bin', ['cppdoc'], chmod=0755)


