# CLI spec

## Roll

Command for generic dice rolls. Supports multiple rolls and dice types. Format for rolls is `NdM` where `N` is the number of dice and `M` is the number of sides on the dice. If `N` is omitted it is assumed to be 1. `M` must be included.

### Examples

Single dice roll.

```bash
$ roll d20
d20
12
= 12
```

Multiple identical dice rolls.

```bash 
$ roll 2d6
2d6
3 + 3
= 6
```

Multiple identical dice rolls with set modifier.

```bash 
$ roll 2d6+4
2d6
3 + 3 + 4
= 10
```

Multiple different dice rolls.

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

Command for character creation, management and interaction. Each haracter is stored in a local file and can be accessed by name. The character files are located in `~/.char/`.

### Create, list and delete commands

#### Examples

Create a character.

```bash
$ char create
Creating a new character...
? what's your name?
...
```

List characters.

```bash
$ char list

Gandalf
Gimli
Legolas
```

List characters with details.

```bash
$ char list -v

Character   Class  Level
Gandalf     Wizard  10
Gimli       Dwarf   10
Legolas     Elf     10
```

Delete a character.

```bash
$ char delete Gandalf

Are you sure you want to delete Gandalf? [y/N] y

Character Gandalf has been deleted.
```

### Character inventory management commands

Commands to manage character inventory. This includes adding and removing items, as well as listing the inventory and equiping items.

Start by opening character inventory.

```bash
$ char Gandalf inventory
Item    quantity    equipped    stats
Sword   1           true        +2 to attack
Shield  1           false       +1 to defense
gold    100         false
<1/1> add a | remove r | next n | prev p | exit e | help h
```

Add an item to the inventory by entering 'a'.

```bash
$ a
Enter item name: Sword
Enter item quantity: 1
Equipped? [y/N] y
```

If item cannot be found in compendium, a custom item can be created.

```bash
$ a
Enter item name: Mjolinir
Item not found in compendium. Create a custom item? [y/N] y
Enter item quantity: 1
Equipped? [y/N] y
Enter item stats: +2 to attack
```

Remove an item from the inventory by entering 'r'.

```bash
$ r
Item    quantity    equipped    stats
Sword   1           true        +2 to attack <<
Shield  1           false       +1 to defense
gold    100         false
press enter to delete item
```

### Character stats and skills commands

Roll character stats and skills.

```bash
$ char Gandalf roll Perception
d20+7
12 + 7
= 19
```

Add additional modifiers to the roll.

```bash
$ char Gandalf roll Perception+3
d20+10
12 + 10
= 19
```

Roll a stat with advantage.

```bash
$ char Gandalf roll Perception -a
d20+7
12 + 7
= 19

d20+7
1 + 7
= 8
```

Roll a stat with disadvantage.

```bash
$ char Gandalf roll Perception -d
d20+7
12 + 7
= 19

d20+7
1 + 7
= 8
```
