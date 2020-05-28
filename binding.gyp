{
  "targets": [{
    "target_name": "processlist",
    "sources": [
      "src/main.cpp"
      , "src/snapshot.cpp"
    ],
    "include_dirs":["src", "<!(node -e \"require('nan')\")"],
    "conditions": [
      ["OS=='win'", {

        "defines": [
          "UNICODE",
          "_UNICODE "
        ],
        "include_dirs":["C:\\Program Files (x86)\\Microsoft Visual Studio 14.0\\VC\\atlmfc\\include"],
        "sources": [
          "src/win/tasklist.cpp"
        ],
        "msvs_settings": {
          "VCCLCompilerTool": {
            "WarningLevel": 3,
            "ExceptionHandling": 1,
            "DisableSpecificWarnings": [4100, 4127, 4201, 4244, 4267, 4506, 4611, 4714, 4800, 4005]
          },
           "VCLinkerTool": {
              "AdditionalLibraryDirectories": [
                  "C:\\Program Files (x86)\\Microsoft Visual Studio 14.0\\VC\\atlmfc\\lib\\amd64"
              ]
            }
          }
        
      }],["OS!='mac' and OS!='win'", {
        "sources": [
          "src/unix/tasklist.cpp"
        ],
        "cflags_cc!": ["-fno-rtti", "-fno-exceptions"],
        "cflags_cc+": [
          "-fexceptions",
          "-std=c++0x",
          "-frtti"
        ]
      }]
    ]
  }]
}
