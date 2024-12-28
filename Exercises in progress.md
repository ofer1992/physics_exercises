```dataview
TABLE book, 
description,
file.mtime as "Last Modified"
FROM ""
WHERE status = "in-progress"
SORT file.mtime desc
```
