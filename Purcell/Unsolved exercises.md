## 1
```dataview
TABLE book, 
description,
difficulty,
file.mtime as "Last Modified"
FROM ""
WHERE status = "unsolved" and book = "Electricity and Magnetism" and file.folder = "Purcell/1"
SORT difficulty
```
## 2
```dataview
TABLE book, 
description,
difficulty,
file.mtime as "Last Modified"
FROM ""
WHERE status = "unsolved" and book = "Electricity and Magnetism" and file.folder = "Purcell/2"
SORT difficulty
```
