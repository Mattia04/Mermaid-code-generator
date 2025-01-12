# Root directory for generating the tree
dir_path = "./"  # Default: Current directory

# Styles for file extensions
extension_styles = {
    # Text Files
    "LICENSE": "classDef LICENSE fill:#f7f7f7,stroke:#6c757d,stroke-width:2px,color:#000,font-size:14px,font-family:'Arial',font-weight:bold;",
    "license": "classDef license fill:#f7f7f7,stroke:#6c757d,stroke-width:2px,color:#000,font-size:14px,font-family:'Arial',font-weight:bold;",
    "README.md": "classDef README.md fill:#f7f7f7,stroke:#6c757d,stroke-width:2px,color:#000,font-size:14px,font-family:'Arial',font-weight:bold;",
    "readme.md": "classDef readme.md fill:#f7f7f7,stroke:#6c757d,stroke-width:2px,color:#000,font-size:14px,font-family:'Arial',font-weight:bold;",
    "Makefile": "classDef Makefile fill:#c8e6c9,stroke:#388e3c,stroke-width:2px,color:#000,font-size:14px,font-family:'Arial',font-weight:normal;",
    ".txt": "classDef txt fill:#f7f7f7,stroke:#6c757d,stroke-width:1px,color:#000,font-size:14px,font-family:'Arial',font-weight:normal;",
    
    # Code Files
    ".py": "classDef py fill:#dff0d8,stroke:#5cb85c,stroke-width:2px,color:#000,font-size:14px,font-family:'Arial',font-weight:bold;",
    ".cpp": "classDef cpp fill:#dff0d8,stroke:#5cb85c,stroke-width:2px,color:#000,font-size:14px,font-family:'Arial',font-weight:bold;",
    ".hpp": "classDef hpp fill:#dff0d8,stroke:#5cb85c,stroke-width:1px,color:#000,font-size:14px,font-family:'Arial',font-weight:normal;",
    
    # Spreadsheet/Document Files
    ".csv": "classDef csv fill:#f9ebea,stroke:#c0392b,stroke-width:1px,color:#000,font-size:14px,font-family:'Arial',font-weight:normal;",
    ".xlsx": "classDef xlsx fill:#f9ebea,stroke:#c0392b,stroke-width:1px,color:#000,font-size:14px,font-family:'Arial',font-weight:normal;",
    
    # Image Files
    ".png": "classDef png fill:#eafaf1,stroke:#2ecc71,stroke-width:1px,color:#000,font-size:14px,font-family:'Arial',font-weight:normal;",
    ".jpeg": "classDef jpeg fill:#eafaf1,stroke:#2ecc71,stroke-width:1px,color:#000,font-size:14px,font-family:'Arial',font-weight:normal;",
    ".jpg": "classDef jpg fill:#eafaf1,stroke:#2ecc71,stroke-width:1px,color:#000,font-size:14px,font-family:'Arial',font-weight:normal;",
    ".svg": "classDef svg fill:#eafaf1,stroke:#2ecc71,stroke-width:1px,color:#000,font-size:14px,font-family:'Arial',font-weight:normal;",
    ".tiff": "classDef tiff fill:#eafaf1,stroke:#2ecc71,stroke-width:1px,color:#000,font-size:14px,font-family:'Arial',font-weight:normal;",
    
    # Compressed Files
    ".zip": "classDef zip fill:#d1c4e9,stroke:#673ab7,stroke-width:1px,color:#000,font-size:14px,font-family:'Arial',font-weight:normal;",
    ".tar": "classDef tar fill:#d1c4e9,stroke:#673ab7,stroke-width:1px,color:#000,font-size:14px,font-family:'Arial',font-weight:normal;",
    ".gz": "classDef gz fill:#d1c4e9,stroke:#673ab7,stroke-width:1px,color:#000,font-size:14px,font-family:'Arial',font-weight:normal;",
    ".7z": "classDef 7z fill:#d1c4e9,stroke:#673ab7,stroke-width:1px,color:#000,font-size:14px,font-family:'Arial',font-weight:normal;",

    # Executables
    ".exe": "classDef exe fill:#ffe0b2,stroke:#ff7043,stroke-width:1px,color:#000,font-size:14px,font-family:'Arial',font-weight:normal;",
    ".bat": "classDef bat fill:#ffe0b2,stroke:#ff7043,stroke-width:1px,color:#000,font-size:14px,font-family:'Arial',font-weight:normal;",
    
    # Audio/Video Files
    ".mp3": "classDef mp3 fill:#ede7f6,stroke:#5e35b1,stroke-width:1px,color:#000,font-size:14px,font-family:'Arial',font-weight:normal;",
    ".wav": "classDef wav fill:#ede7f6,stroke:#5e35b1,stroke-width:1px,color:#000,font-size:14px,font-family:'Arial',font-weight:normal;",    
    ".mp4": "classDef mp4 fill:#ede7f6,stroke:#5e35b1,stroke-width:1px,color:#000,font-size:14px,font-family:'Arial',font-weight:normal;",
    ".avi": "classDef avi fill:#ede7f6,stroke:#5e35b1,stroke-width:1px,color:#000,font-size:14px,font-family:'Arial',font-weight:normal;",
    ".mkv": "classDef mkv fill:#ede7f6,stroke:#5e35b1,stroke-width:1px,color:#000,font-size:14px,font-family:'Arial',font-weight:normal;",
}

# Icons for file extensions grouped by file typology
extension_icons = {
    # Text Files
    ".txt": "📝",
    ".md": "📝",
    "LICENSE": "📜",
    "README.md": "📖",
    "Makefile": "⚙️",

    # Code Files
    ".py": "🐍",
    ".cpp": "💻",
    ".hpp": "💻",
    ".json": "🔧",
    ".yaml": "🔧",
    ".yml": "🔧",

    # Spreadsheet/Document Files
    ".csv": "📊",
    ".xlsx": "📈",
    ".docx": "📄",
    ".doc": "📄",
    ".pptx": "📊",
    ".ppt": "📊",

    # Image Files
    ".png": "🖼️",
    ".jpg": "🖼️",
    ".jpeg": "🖼️",
    ".svg": "🖼️",
    ".tiff": "🖼️",

    # Audio Files
    ".mp3": "🎵",
    ".wav": "🎵",

    # Video Files
    ".mp4": "🎥",
    ".avi": "🎥",
    ".mkv": "🎥",

    # Compressed Files
    ".zip": "📦",
    ".tar": "📦",
    ".gz": "📦",
    ".7z": "📦",

    # Executables
    ".exe": "⚙️",
    ".bat": "⚙️",
    ".bin": "⚙️",
}
