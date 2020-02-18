## regular expression util scripts

### json_one_line_converter.pl
Perl script for converting human readable json structure to single line json string
for curl requests body.
#### example:
Convert source file source.json to result.txt
```json
{
  "name": "docs",
  "array":
    [
      "first",
      "second",
      "third"
    ],
  "additional":
  {
    "date": "18.02.20",
    "number": 473
  }
}
``` 
just run: 
```perl
perl json_one_line_converter.pl source.json > result.txt
``` 
output in result.txt:
```txt
{\"name\":\"docs\",\"array\":[\"first\",\"second\",\"third\"],\"additional\":{\"date\":\"18.02.20\",\"number\":473}}
``` 
