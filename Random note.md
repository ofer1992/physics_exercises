
```dataviewjs
let pages = dv.pages('').where(p => p.status == "unsolved");
let length = pages.length;
let numberToReturn = 1;

function getRandos(list, max, itemNum) {
  var items = [];
  for (var i=0; i<itemNum; i++) {
    let randomPage = list[Math.floor(Math.random() * max)];
    items.push(`${randomPage.file.link} (Chapter ${randomPage.chapter})`);
  }
  return items;
}

dv.list(getRandos(pages, length, numberToReturn));
```
