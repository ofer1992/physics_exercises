 ```dataview
LIST
FROM ""
WHERE status = "unsolved"
```

```dataview
TABLE file.mtime as "Last Modified"
FROM ""
WHERE status = "unsolved"
```

You can customize the TABLE version by adding any other properties you want to see as columns. Let me know if you'd like to see other variations of this query or add specific fields!

 Here's the query with a column showing the containing folder:

```dataview
TABLE file.path as "Location", 
description,
file.mtime as "Last Modified"
FROM ""
WHERE status = "unsolved"
```

Or if you prefer just the folder name without the full path:

```dataview
TABLE file.folder as "Folder", 
description,
file.mtime as "Last Modified"
FROM ""
WHERE status = "unsolved"
```

The `file.folder` will show just the immediate containing folder, while `file.path` shows the full path from the root of your vault. Choose whichever works better for your needs!