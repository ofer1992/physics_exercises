
```dataview
TABLE 
rows.book[0] as "Book",
    length(filter(rows, (f) => f.status = "solved")) * 100.0 / length(rows.file) + "%" as "Completion Rate",
    length(rows.file) as "Total Exercises",
    length(filter(rows, (f) => f.status = "solved")) as "Completed"
FROM ""
WHERE chapter AND status
GROUP BY chapter
SORT chapter ASC
```
