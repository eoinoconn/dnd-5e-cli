# CLI spec

## Roll

Command for generic dice rolls. Supports multiple rolls and dice types. Format for rolls is `NdM` where `N` is the number of dice and `M` is the number of sides on the dice. If `N` is omitted it is assumed to be 1. `M` must be included.

### Examples

```bash
$ roll 1d20
1d20
12
= 12
```

```bash	
$ roll 2d6
2d6
3 + 3
= 6
```

```bash	
$ roll 2d6 4d17
2d6
1 + 5
= 6

4d17
8 + 5 + 12 + 12
= 37
```

## Char

#TODO: Char documentation.
