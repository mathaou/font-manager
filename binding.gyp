{
  "targets": [
    {
      "target_name": "fontmanager",
      "sources": [ "src/FontManager.cc" ],
      "conditions": [
        ['OS=="mac"', {
          "sources": ["src/FontManagerMac.mm"],
          "link_settings": {
            "libraries": ["CoreText.framework", "Foundation.framework"]
          }
        }],
        ['OS=="win"', {
          "sources": ["src/FontManagerWindows.cc"],
          "link_settings": {
            "libraries": ["Dwrite.lib"]
          }
        }]
      ]
    }
  ]
}
