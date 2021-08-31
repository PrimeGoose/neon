{
    "targets": [{
        "target_name": "neon",
        "sources": [ "src/neon.cc" ],
        "include_dirs": [ "<!(node -e \"require('nan')\")" ],
        "variables": { "runtime%": "node" },
        'conditions': [
            ['runtime=="electron"', { 'defines': ['NODE_RUNTIME_ELECTRON=1'] }],
        ],
        'configurations': {
            'Release': {
                'msvs_settings': {
                    'VCCLCompilerTool': {
                        'WholeProgramOptimization': 'false'
                    },
                    'VCLinkerTool': {
                        'LinkTimeCodeGeneration': 0
                    }
                }
            },
            'Debug': {
                'msvs_settings': {
                    'VCCLCompilerTool': {
                        'RuntimeLibrary': '0',
                        'UndefinePreprocessorDefinitions': ['DEBUG', '_DEBUG'],
                        'PreprocessorDefinitions': ['NDEBUG']
                    },
                }
            }
        }
    }]
}
