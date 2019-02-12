# FileSizeDisplay

This is a simple class to convert bytes to the mostly logical human readable size.

### Examples:

```python
>>> FileSizeDisplay(49785020687)
49.79 GB

>>> FileSizeDisplay(496997, short=False)
497.0 Kilobytes

>>> FileSizeDisplay(3569581187, short=False, output='MB')
3569.58 Megabytes

```

### Bugs:
- if the `output` kwarg is used, and the logical display output is smaller than the desired output, it will not show the desiered unit, but the logical one. 